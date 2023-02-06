import pandas as pd
import os
#extrair dados dos relatórios finais 2022 enviado via Forms

words = ['DOCENTES','Nome','TÉCNICOS ADMINISTRATIVOS (servidores e/ou terceirizados)','ALUNOS BOLSISTAS']
way = os.listdir('PLN') #Diretório contendo todas as planihas

#Extrair Nome e Siape Docentes
name = []
siape = []
for i in range(len(way)):
  df = pd.read_excel('PLN/'+way[i], sheet_name='equipe_extensionista')
  for i in range(2,df.shape[0]):
    if(df.at[i,'Unnamed: 0']!=words[2] and str(df.at[i,'Unnamed: 0'])!='nan'):
      name.append(str(df.at[i,'Unnamed: 0']))
      siape.append(df.at[i,'Unnamed: 4'])
    if(df.at[i,'Unnamed: 0']==words[2]):
      break
print(len(siape)==len(name))
#salvando em csv
data = {'nome':name,'siape':siape}
data_frame = pd.DataFrame(data)
data_frame.to_csv('docentes.csv')

#Extrair Nome e Siape Técnicos Adminstrativos
name = []
siape = []
func = []
for i in range(len(way)):
  dframe = pd.read_excel('PLN/'+way[i], sheet_name='equipe_extensionista')
  control=True
  j,ref0,ref1=0,0,0
  while(control):
      if(dframe.at[j,'Unnamed: 0']==words[2]):
        ref0=j+2
      if(dframe.at[j,'Unnamed: 0']==words[3]):
        ref1=j
        control=False
      j+=1
  for z in range(ref0,ref1):
    if(dframe.at[z,'Unnamed: 0']!=words[2] and str(dframe.at[z,'Unnamed: 0'])!='nan'):
        name.append(str(dframe.at[z,'Unnamed: 0']))
        siape.append(dframe.at[z,'Unnamed: 1'])
        func.append(dframe.at[z,'Unnamed: 2'])
print(len(siape)==len(name))
#salvando em csv
data = {'nome':name,'siape':siape,'função':func}
data_frame = pd.DataFrame(data)
data_frame.to_csv('tecnicos.csv')