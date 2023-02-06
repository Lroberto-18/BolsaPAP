import pandas as pd
import os
#extrair dados dos relatórios finais 2022 enviado via Google Forms


def teachers(keywords, path_team):
  name = []
  siape = []

  for i in range(len(path_team)):
    df = pd.read_excel('equipe/'+path_team[i], sheet_name='equipe_extensionista')

    for i in range(2,df.shape[0]):
      if(df.at[i,'Unnamed: 0']!=keywords[2] and str(df.at[i,'Unnamed: 0'])!='nan'):
        name.append(str(df.at[i,'Unnamed: 0']).upper())
        siape.append(df.at[i,'Unnamed: 4'])
      if(df.at[i,'Unnamed: 0']==keywords[2]):
        break

  data = {'nome':name,'siape':siape}
  data_frame = pd.DataFrame(data)
  data_frame.to_csv('docentes.csv')


def technical(keywords, path_team):
  name = []
  siape = []
  func = []

  for i in range(len(path_team)):
    dframe = pd.read_excel('equipe/'+path_team[i], sheet_name='equipe_extensionista')
    control=True
    j,ref0,ref1=0,0,0

    while(control):
        if(dframe.at[j,'Unnamed: 0']==keywords[2]):
          ref0=j+2
        if(dframe.at[j,'Unnamed: 0']==keywords[3]):
          ref1=j
          control=False
        j+=1

    for z in range(ref0,ref1):
      if(dframe.at[z,'Unnamed: 0']!=keywords[2] and str(dframe.at[z,'Unnamed: 0'])!='nan'):
          name.append(str(dframe.at[z,'Unnamed: 0']).upper())
          siape.append(dframe.at[z,'Unnamed: 1'])
          func.append(dframe.at[z,'Unnamed: 2'])


  data = {'nome':name,'siape':siape,'função':func}
  data_frame = pd.DataFrame(data)
  data_frame.to_csv('tecnicos.csv')


def social_media(path_social_media):
  link = []
  qtd = []

  for i in range(len(path_social_media)):
    df = pd.read_excel('redes/'+path_social_media[i], sheet_name='Planilha1')

    for i in range(2,df.shape[0]):
      link.append(str(df.at[i,'Unnamed: 0']))
      qtd.append(df.at[i,'Unnamed: 1'])

  data = {'link':link,'qtd':qtd}
  data_frame = pd.DataFrame(data)
  data_frame.to_csv('redes.csv')


def locations(path_locations):
  atv = []
  nome = []
  uf = []
  cidade = []
  bairro = []

  for i in range(len(path_locations)):
    df = pd.read_excel('locais/'+path_locations[i], sheet_name='locais')
    
    for i in range(2,df.shape[0]):
      atv.append(str(df.at[i,'Unnamed: 0']))
      nome.append(str(df.at[i,'Unnamed: 1']))
      uf.append(str(df.at[i,'Unnamed: 2']))
      cidade.append(str(df.at[i,'Unnamed: 3']))
      bairro.append(str(df.at[i,'Unnamed: 4']))

  data = {'atv':atv,'nome':nome,'uf':uf,'cidade':cidade,'bairro':bairro}
  data_frame = pd.DataFrame(data)
  data_frame.to_csv('locais.csv')


def main():
  keywords = ['DOCENTES','Nome','TÉCNICOS ADMINISTRATIVOS (servidores e/ou terceirizados)','ALUNOS BOLSISTAS']
  path_team = os.listdir('equipe')
  path_social_media = os.listdir('redes')
  path_locations = os.listdir('locais')

  teachers(keywords, path_team)
  technical(keywords, path_team)
  social_media(path_social_media)
  locations(path_locations)


if __name__=="__main__":
  main()