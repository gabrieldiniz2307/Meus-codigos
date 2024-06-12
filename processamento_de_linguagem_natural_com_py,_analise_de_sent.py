# -*- coding: utf-8 -*-
"""Cópia de Processamento de Linguagem natural com PY, Analise de sent

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uQYS2pHnlBJcXsV3K04ge1yQ3-Ros2Ox
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install unidecode
# %pip install nltk
# %pip install spacy

#Tratamento de Dados
import pandas as pd
import numpy as np

#NLP
from unidecode import unidecode
import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#Preparar as libs de NLP
!python -m spacy download 'pt_core_news_sm'
nlp = spacy.load('pt_core_news_sm')
nltk.download('stopwords')
nltk.download('punkt')

"""### Carregar Dados

"""

df_resenha = pd.read_csv('/content/imdb-reviews-pt-br.csv', encoding='utf-8')
df_resenha.head()

df_resenha = df_resenha[['text_pt',	'sentiment']].sample(frac=0.2, random_state=42).reset_index(drop=True).copy()

"""### Funçoes de apoio

"""

# Criação do vetor de stopwords sem acento
stopwords_sem_acento = [unidecode(palavra) for palavra in stopwords.words('portuguese')]

#Letras minusculas
letras_minusculas = [chr(letra) for letra in range(97,123)]

# remover stopwords
def remover_stop_words(tokens, stopwords):
  tokens = [palavra for palavra in tokens if palavra not in stopwords_sem_acento]
  return tokens

#Transformar texto em tokens
def tokenizacao(texto):
  tokens = word_tokenize(texto, language='portuguese')
  return tokens

# Remoção das letras isoladas
def remover_letras_isoladas(tokens, letras):
  tokens = [palavra for palavra in tokens if palavra not in letras_minusculas]
  return tokens

def lematizar(frase):
  doc = nlp(frase)
  lemmas = [token.lemma_ for token in doc]
  return ' '.join(lemmas)

# Transformar token para texto
def token_para_texto(tokens):
  if len(tokens)> 0:
    return ' '.join(tokens)
  return ''

"""### Tratar o texto"""

# Verificar quantidade de NaN
df_resenha['text_pt'].isna().sum()

#Deixar as palavras em minusculo
df_resenha['texto-tratado'] = df_resenha['text_pt'].str.lower()

#df_resenha['texto_tratado'] = df_resenha['texto_tratado'].apply(lematizar)

# Remover acentuação
df_resenha['texto-tratado'] = df_resenha['texto-tratado'].apply(unidecode)

#Remover caracteres especiais
df_resenha['texto-tratado'] = df_resenha['texto-tratado'].str.replace('[^\w\s]','', regex=True)

# Tokenização das palavras
df_resenha['texto-tratado'] = df_resenha['texto-tratado'].apply(tokenizacao)

#Remover stopwords
df_resenha['texto-tratado'] = df_resenha['texto-tratado'].apply(remover_stop_words,stopwords = stopwords_sem_acento)

#Remover letras isoladas
df_resenha['texto-tratado'] = df_resenha['texto-tratado'].apply(remover_letras_isoladas ,letras = letras_minusculas)

#Tokens para texto
df_resenha['texto-tratado'] = df_resenha['texto-tratado'].apply(token_para_texto)

df_resenha['texto-tratado'].head()

#Transformar as informaçoes da coluna sentimento para 0 e 1
df_resenha['sentimento'] = df_resenha['sentiment'].map({'pos':1, 'neg':0})

#Contar as informaçoes da colunas
df_resenha['sentimento'].value_counts()

"""### Importar para tratamento de texto"""

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X_treino, X_teste, y_treino, y_teste = train_test_split(df_resenha['texto-tratado'],
                                                        df_resenha['sentimento'],  test_size=0.2, random_state=42)

del df_resenha, nlp

vetorizador = TfidfVectorizer()
palavras_treino = vetorizador.fit_transform(X_treino)
palavras_teste = vetorizador.transform(X_teste)
X_treino = pd.DataFrame(palavras_treino.toarray(), columns=vetorizador.get_feature_names_out())
X_teste = pd.DataFrame(palavras_teste.toarray(), columns=vetorizador.get_feature_names_out())

regressao_logistica = LogisticRegression()
regressao_logistica.fit(X_treino, y_treino)

y_pred = regressao_logistica.predict(X_teste)

accuracy_score(y_teste, y_pred)