import numpy as np
import pandas as pd

#v4.0

dados = pd.read_excel("GEO.xlsx",index_col=None) #arquivo com angulos e distância  Ano	Temática	Posição	Ângulo	Distância
dataFrame = pd.DataFrame(dados)
distancia_max = dataFrame.max(skipna = False) #distancia máxima até a UFCA
d_max = int(distancia_max[6])

#criando DATAFRAME de saída
dOut = {'km': np.arange(d_max+2)}
dataOut = pd.DataFrame(data=dOut)
dataOut['Raio'] = np.arange(1,d_max+3)

pontos = np.array(['(NE)', '(NO)', '(SE)', '(SO)'])
tematica = np.array(['Saúde','Educação','Tecnologia','Meio ambiente','Trabalho','Comunicação','Direitos Humanos e Justiça'])

for i in range(len(pontos)):  
  dataOut[pontos[i]] = np.zeros(d_max+2)#criar coluna vazia
for i in range(len(tematica)):       
  for j in range(len(pontos)):                        
    dataOut[tematica[i]+' '+pontos[j]] = np.zeros(d_max+2)#criar coluna vazia
#contabilizar lugares beneficiados pelas ações dividindo por pontos cardeais e colaterais, também por temática e por pontos cardeais e colaterais
for j in range(dataOut.shape[0]):
  for i in range(dataFrame.shape[0]):
    if(dataFrame.loc[i,'Distância'] >= dataOut.loc[j,'km'] and dataFrame.loc[i,'Distância'] < dataOut.loc[j+1,'km']):
        for z in range(len(pontos)):
          if(dataFrame.loc[i,'Posição']==pontos[z]):
              dataOut.at[j,pontos[z]] = 1 + dataOut.at[j,pontos[z]]
              for x in range(dataOut.shape[1]):
                if(dataOut.columns[x]==dataFrame.loc[i,'Temática']+' '+dataFrame.loc[i,'Posição']):
                  dataOut.at[j,dataOut.columns[x]] = dataOut.at[j,dataOut.columns[x]] +1

dataOut.to_excel("TESTE1.xlsx", index=None)