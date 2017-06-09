import re
import nltk
from nltk import tokenize
from nltk import stem
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer


def normalizacao(str):  #normalizacao - remover  caracteres especiais e transformar em minúsculas
	str1 = re.sub(r'[?|$|.|!]',r'',str)
	return str1


def remover_stop_words(str):
	stopwordsexec = ['quando', 'quem', 'como', 'quem', 'qual']
	stopw=nltk.corpus.stopwords.words('portuguese')
	stopw2 = [w for w in stopw if not w in stopwordsexec ]
	stopresult = [w for w in str if not w in stopw2]
	return stopresult

def gerar_stemmer(str):
	stemmer = nltk.stem.RSLPStemmer()
	filt_stem = []
	for i in str:
		filt_stem.append(stemmer.stem(i))
	return filt_stem
	
def transformar_pergunta_binario(str):  
	lista_str = []
	lista_bin_letra = []
	lista_bin_palavra = []
	lista_bin_pergunta = []

	for palavras in str:
		lista_str.append( ''.join(format(ord(x), 'b') for x in palavras)     )
		print("lista_str",lista_str)
	
	cont_palavra=0
	for palavras in lista_str:
		for i in range(0, len(palavras)):
			lista_bin_palavra.append(int(lista_str[cont_palavra][i]))
		cont_palavra+=1	
		lista_bin_pergunta.append(lista_bin_palavra)
		print("lista_bin_palavra",lista_bin_palavra)
		print("lista_bin_pergunta",lista_bin_pergunta)
		lista_bin_palavra=[]
	return lista_bin_pergunta




def pre_processar(lista):
	lista_processada = []
	for str0 in lista:
		str0=normalizacao(str0)  # normalizacao - remover  caracteres especiais e transformar em minúsculas
		str0=word_tokenize(str0)  #tokenizacao
		str0=remover_stop_words(str0)   # remocao de stopwords
		str0=gerar_stemmer(str0)
		lista_processada.append(str0)
	return lista_processada