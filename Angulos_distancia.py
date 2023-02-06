import numpy as np
import pandas as pd
import math as mt
#Distancia entre os pontos e a UFCA e seu respectivo ângulo
#v1.1


def main():
  pln = pd.read_excel('DATA_BASE_GEORREF_POWERBI.xlsx', index_col=None)#Arquivo com cordenadas geográficas
  dataFrame = pd.DataFrame(pln)

  #dataFrame.at[0,'longitude'] retornar primeira linha da coluna longitude
  numero_linhas = dataFrame.shape[0]
  numero_colunas = dataFrame.shape[1]

  #dataFrame = dataFrame.assign(city = ['','','','','','','','']) #criar coluna vazia exemplo
  #dataFrame.loc[:,"Posição"] = 0                                 #criar coluna vazia
  dataFrame['Posicao'] = str(np.nan)                             #criar coluna vazia
  dataFrame['Angulo'] = np.nan
  dataFrame['Distancia'] = np.nan                                  #criar coluna vazia

  #coordenadas da UFCA campus juazeiro
  longitude_ufca = -39.30497
  latitude_ufca = -7.25678

  #display(dataFrame) #opcional

  for i in range(numero_linhas):
    latitude_ponto = dataFrame.at[i,'latitude']
    longitude_ponto = dataFrame.at[i,'longitude']

    #calculo do angulo usando arcotangente
    angulo = mt.atan(abs(latitude_ponto-latitude_ufca)/abs(longitude_ponto-longitude_ufca)) #radianos
    angulo = np.degrees(angulo) #convertendo radianos para graus
    #distancia entre dois pontos
    a = np.array((longitude_ufca, latitude_ufca))
    b = np.array((longitude_ponto, latitude_ponto))
    dataFrame.at[i,'Distancia'] = np.linalg.norm(a-b)*111.11
    
    #verificar localização do ponto em relação aos pontos cardeais e colaterais
    if(latitude_ponto==latitude_ufca):
      if(longitude_ponto>longitude_ufca):
        #Leste
        dataFrame.at[i,'Posicao'] = 'Leste'
        dataFrame.at[i,'Angulo'] = 0
      elif(longitude_ponto<longitude_ufca):
        #Oeste
        dataFrame.at[i,'Posicao'] = 'Oeste'
        dataFrame.at[i,'Angulo'] = 180
    elif(latitude_ponto<latitude_ufca):
      if(longitude_ponto==longitude_ufca):
        #Sul
        dataFrame.at[i,'Posicao'] = 'Sul'
        dataFrame.at[i,'Angulo'] = 270
      elif(longitude_ponto<longitude_ufca):
        #Sudoeste
        dataFrame.at[i, 'Angulo'] = angulo +180
        dataFrame.at[i,'Posicao'] = 'Sudoeste'
      elif(longitude_ponto>longitude_ufca):
        #Sudeste
        dataFrame.at[i, 'Angulo'] = 360 - angulo
        dataFrame.at[i,'Posicao'] = 'Sudeste'
    elif(latitude_ponto>latitude_ufca):
      if(longitude_ponto==longitude_ufca):
        #Norte
        dataFrame.at[i,'Posicao'] = 'Norte'
        dataFrame.at[i,'Angulo'] = 90
      elif(longitude_ponto>longitude_ufca):
        #Nordeste
        dataFrame.at[i,'Posicao'] = 'Nordeste'
        dataFrame.at[i, 'Angulo'] = angulo
      elif(longitude_ponto<longitude_ufca):
        #Noroeste
        dataFrame.at[i, 'Angulo'] = 180 - angulo 
        dataFrame.at[i,'Posicao'] = 'Noroeste'

  #display(dataFrame)
  dataFrame.to_excel("Angulos.xlsx",index=False) #salvando em xlsx


if __name__=="__main__":
  main()