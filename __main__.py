# Importando os módulos 
import os
from modules.conectorsql import Interface_sql
import pandas as pd
import numpy as np
import time


def tratamento(dataf):
    """Recebe o Dataframe para converter em array e fazer os tratamentos no corpo do texto, retornando o texto mais limpo.

    Args:
        dataf (DataFrame): Dataframe Pandas

    Returns:
        DataFrame: Retorna o array com os tratamentos do texto feitos.
    """
    dataf = np.asarray(dataf)
    for texto in dataf:
        texto[3] = texto[3].replace('<p>', '').replace('<a href="', '').replace('"">', '').replace('>', ' ').replace('</a>', '').replace('<p class=""translated_stamp_subtext"">versão original', '').replace('</p>', '').replace('<p class="translated_stamp_text">', '').replace('_blank" rel="noopener">', '').replace('<p class="translated_stamp_subtext">', '').replace('https://www.cnnbrasil.com.br/', '"')
    
    for new in dataf:
        new[2] = new[2][:11]
    dataf = pd.DataFrame(dataf, columns=["url","titulo","publicacao","texto","tags"])

    return dataf

# Intanciando a conexão com o MySQL
news = Interface_sql("root", "root", "127.0.0.1", "noticias")

# Iniciando as Spiders para cada um dos sites e gerando os CSV's com os dados retornados
try:    
    os.system("scrapy runspider bbc.py -O bbc.csv")
    os.system("scrapy runspider cnn.py -O cnn.csv")
    os.system("scrapy runspider metropoles.py -O metropoles.csv")
    os.system("scrapy runspider uol.py -O uol.csv")
except Exception as e:
    print(e)

# Importando os csv's como DataFrame Pandas e dropando possíveis dados nulos.
try:
    bbc = pd.read_csv("bbc.csv")
    bbc = bbc.dropna()
    cnn = pd.read_csv("cnn.csv")
    cnn = cnn.dropna()
    uol = pd.read_csv("uol.csv")
    uol = uol.dropna()
    metropoles = pd.read_csv("metropoles.csv")    
    metropoles = metropoles.dropna()
except Exception as e:
    print(e)

# Chamando a função tratamento para tratar os dados recebidos da cnn
try:
    cnn = tratamento(cnn)
except Exception as e:
    print(e)

# Convertendo o tipo de dado para datetime em todos os DF
try:   
    bbc['publicacao'] = pd.to_datetime(bbc['publicacao'])
    cnn['publicacao'] = pd.to_datetime(cnn['publicacao'])
    metropoles['publicacao'] = pd.to_datetime(metropoles['publicacao'])
    uol['publicacao'] = pd.to_datetime(uol['publicacao'])
except Exception as e:
    print(e)


# Fazendo as insserções no DB MySQL

# Inserindo os dados da BBC
try:
    bbc = np.asarray(bbc)
    for item in bbc:
        query = f"insert into bbc (url, titulo, publicacao, texto, tags) values {tuple(item)}"
        news.action(query)
except Exception as e:
    print(e)

# Inserindo os dados da UOL
try:
    uol = np.asarray(uol)
    for item in uol:
        query = f"insert into uol (url, titulo, publicacao, texto) values {tuple(item)}"
        news.action(query)
except Exception as e:
    print(e)

# Inserindo os dados da Metropoles
try:
    metropoles = np.asarray(metropoles)
    for item in metropoles:
        query = f"insert into metropoles (url, titulo, publicacao, texto, tags) values {tuple(item)}"
        news.action(query)
except Exception as e:
    print(e)

# Inserindo os dados da CNN
try:
    cnn = np.asarray(cnn)
    for item in cnn:
        query = f"insert into cnn (url, titulo, publicacao, texto, tags) values {tuple(item)}"
        news.action(query)
except Exception as e:
    print(e)
