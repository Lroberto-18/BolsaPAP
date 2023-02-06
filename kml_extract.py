import os
from os import listdir


def main():
  folder = 'ArquivosKML/' #Pasta com todos os arquivos kml
  files = listdir(folder)

  header =['<kml xmlns','</StyleMap>']
  point =['<Placemark>','</Placemark>']
  years = ['<value>2018','<value>2019','<value>2020','<value>2021']
  remove = '<description>'


  for i in range(len(files)):
    file_kml = open(folder+files[i],'r')
    data =[]
    data_2018 =[]
    data_2019 =[]
    data_2020 =[]
    data_2021 =[]
    #salvar arquivo em vetor
    for line in file_kml:
        data.append(line.strip('\n'))
    #remover os dados da tag '<description>'
    control = True
    index=0
    while(control):
        line = data[index]
        if remove in line:
            del data[index]
        index+=1
        if(index>=len(data)):
            control=False
    #adicionar primeiras linhas Header Cabeçalho
    control1 = True
    t1 = False
    t2 = False
    index = 0
    ref1 =[]
    while(control1):
      linha = data[index]
      if header[0] in linha:
        ref1.append(index)
        t1= True
      if header[1] in linha:
        ref1.append(index)
        t2 = True
      if(t1==True and t2==True):
        control1 = False
      index += 1
    for j in range(0, ref1[1]+1):
      data_2018.append(data[j])
      data_2019.append(data[j])
      data_2020.append(data[j])
      data_2021.append(data[j])
    #Dividir por anos
    control2 = True
    t1 = False
    t2 = False
    index = 0
    while(control2):
      linha = data[index]
      if point[0] in linha:
        ref3 = index
        t1= True
      if point[1] in linha:
        ref4 = index
        t2 = True
      if(t1==True and t2==True):
        for j in range(ref3+1, ref4):
          d = data[j]
          if years[0] in d:
            for j in range(ref3, ref4+1):
              data_2018.append(data[j])
          if years[1] in d:
            for j in range(ref3, ref4+1):
              data_2019.append(data[j])
          if years[2] in d:
            for j in range(ref3, ref4+1):
              data_2020.append(data[j])
          if years[3] in d:
            for j in range(ref3, ref4+1):
              data_2021.append(data[j])
      if(index==len(data)-1):
          control2 = False
      index += 1
    #Fechar tag
    data_2018.append(data[len(data)-2])
    data_2019.append(data[len(data)-2])
    data_2020.append(data[len(data)-2])
    data_2021.append(data[len(data)-2])
    data_2018.append(data[len(data)-1])
    data_2019.append(data[len(data)-1])
    data_2020.append(data[len(data)-1])
    data_2021.append(data[len(data)-1])    
    name = files[i].replace('.kml',"")
    #Salvar arquivos kml
    with open(name+'2018'+'.kml', 'w') as kml:
      for line in data_2018:
        kml.write('{}\n'.format(line))
    with open(name+'2019'+'.kml', 'w') as kml:
      for line in data_2019:
        kml.write('{}\n'.format(line))
    with open(name+'2020'+'.kml', 'w') as kml:
      for line in data_2020:
        kml.write('{}\n'.format(line))
    with open(name+'2021'+'.kml', 'w') as kml:
      for line in data_2021:
        kml.write('{}\n'.format(line))


if __name__=="__name__":
  main()