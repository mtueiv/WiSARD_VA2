import nltk
from nltk import tokenize
from nltk import stem
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer


from PreProcessamento import *
from Carregamento import *

from WiSARD  import *
from Discriminator import *
from Memory import *

#carregar exemplos de perguntas de arquivos 
print ('******** carregar exemplos de perguntas de arquivos','\n')
perg_data_obra = carregar_perguntas("perguntas_data_obra.txt")
perg_valor_obra = carregar_perguntas("perguntas_valor_obra.txt")
perg_presidente = carregar_perguntas("perguntas_presidente.txt")
perg_morte_autor = carregar_perguntas("perguntas_morte_autor.txt")
perg_nome_quadro = carregar_perguntas("perguntas_nome_quadro.txt")
perg_outros = carregar_perguntas("perguntas_outros.txt")

# pre-processamento perguntas
print ('******** pre-processamento perguntas','\n')
lista_data_obra = pre_processar(perg_data_obra)
lista_valor_obra = pre_processar(perg_valor_obra)
lista_presidente = pre_processar(perg_presidente)
lista_morte_autor =  pre_processar(perg_morte_autor)
lista_nome_quadro = pre_processar(perg_nome_quadro)
lista_outros = pre_processar(perg_outros)

### criando lista de palavras
print ('******** criando dicionario de palavras','\n')
lista_palavras = []
lista_palavras.append(lista_data_obra)
lista_palavras.append(lista_valor_obra)
lista_palavras.append(lista_presidente)
lista_palavras.append(lista_morte_autor)
lista_palavras.append(lista_nome_quadro)
lista_palavras.append(lista_outros)

### ordenando dicionario de palavras 
print ('******** criando dicionario de palavras','\n')
dicionario = criar_dicionario_ordenado(lista_palavras)
print ("\n**************** dicionario ********\n", dicionario)

### converter palavras das perguntas em posições do dicionario
print ('******** converter palavras das perguntas em posições do dicionario','\n')
conv_lista_data_obra = [] 
conv_lista_valor_obra= []
conv_lista_presidente = []
conv_lista_morte_autor = []
conv_lista_nome_quadro = []
conv_lista_outros = []
conv_lista_data_obra = converter_pos_dicionario(lista_data_obra,dicionario)
conv_lista_valor_obra = converter_pos_dicionario(lista_valor_obra,dicionario)
conv_lista_presidente = converter_pos_dicionario(lista_presidente,dicionario)
conv_lista_morte_autor = converter_pos_dicionario(lista_morte_autor,dicionario)
conv_lista_nome_quadro = converter_pos_dicionario(lista_nome_quadro,dicionario)
conv_lista_outros = converter_pos_dicionario(lista_outros,dicionario)

print("\n***************** conv_lista_nome_quadro ****************\n",conv_lista_nome_quadro)

#### transformar lista de posicoes em lista de binarios
### cada pergunta tem máximo de 5 palavras, sendo cada palavra 8 bits.  Logo cada pergunta = 40 bits.
conv_lista_data_obra_bin = []
conv_lista_valor_obra_bin = []
conv_lista_presidente_bin = []
conv_lista_morte_autor_bin = []
conv_lista_nome_quadro_bin = []
conv_lista_outros_bin = []
conv_lista_data_obra_bin = conv_lista_num_em_binario(conv_lista_data_obra)
conv_lista_valor_obra_bin = conv_lista_num_em_binario(conv_lista_valor_obra)
conv_lista_presidente_bin = conv_lista_num_em_binario(conv_lista_presidente)
conv_lista_morte_autor_bin = conv_lista_num_em_binario(conv_lista_morte_autor)
conv_lista_nome_quadro_bin = conv_lista_num_em_binario(conv_lista_nome_quadro)
conv_lista_outros_bin = conv_lista_num_em_binario(conv_lista_outros)
print("\n **************** conv_lista_nome_quadro_bin ****************\n",conv_lista_nome_quadro_bin)



XPerguntas = incluir_perguntas(conv_lista_data_obra_bin) + incluir_perguntas(conv_lista_valor_obra_bin)+ incluir_perguntas(conv_lista_presidente_bin)+ incluir_perguntas(conv_lista_morte_autor_bin )+incluir_perguntas(conv_lista_nome_quadro_bin )+incluir_perguntas(conv_lista_outros_bin )
print (XPerguntas)

# classificar
YClassificacao = []
YClassificacao=classificar('data_obra',len(conv_lista_data_obra_bin))
YClassificacao+=classificar('valor_obra',len(conv_lista_valor_obra_bin))
YClassificacao+=classificar('presidente',len(conv_lista_presidente_bin))
YClassificacao+=classificar('morte_autor',len(conv_lista_morte_autor_bin))
YClassificacao+=classificar('nome_quadro',len(conv_lista_nome_quadro_bin))
YClassificacao+=classificar('outros',len(conv_lista_outros_bin))

print ('\n ************************** Classificacao *************************** \n', len(YClassificacao), YClassificacao)

num_bits_addr = 6
bleaching = True

w = WiSARD(num_bits_addr, bleaching)

#training discriminators
w.fit(XPerguntas, YClassificacao)
### inserir arquivo com outras perguntas e classisficar como outros.  Ver o resultado
# predicting class
print('\n****** Início de Testes:')
X_test_data_obra =incluir_perguntas(conv_lista_num_em_binario(converter_pos_dicionario (pre_processar(carregar_perguntas("perguntas_data_obra_teste2.txt")),dicionario)))
result = w.predict(X_test_data_obra)  #  Result will be a dictionary using the classes as key and the WiSARD result as values
print ("**** Teste com Data Obra:",result,'\n')

X_test_morte_autor =incluir_perguntas(conv_lista_num_em_binario(converter_pos_dicionario (pre_processar(carregar_perguntas("perguntas_morte_autor_teste2.txt")),dicionario)))
result = w.predict(X_test_morte_autor)  #  Result will be a dictionary using the classes as key and the WiSARD result as values
print ("***** Teste com Morte Autor:",result,'\n')

X_test_nome_quadro =incluir_perguntas(conv_lista_num_em_binario(converter_pos_dicionario (pre_processar(carregar_perguntas("perguntas_nome_quadro_teste2.txt")),dicionario)))
result = w.predict(X_test_nome_quadro)  #  Result will be a dictionary using the classes as key and the WiSARD result as values
print ("***** Teste com Nome Quadro:",result,'\n')

X_test_presidente =incluir_perguntas(conv_lista_num_em_binario(converter_pos_dicionario (pre_processar(carregar_perguntas("perguntas_presidente_teste2.txt")),dicionario)))
result = w.predict(X_test_presidente)  #  Result will be a dictionary using the classes as key and the WiSARD result as values
print ("****** Teste com Presidente:",result,'\n')

X_test_valor_obra =incluir_perguntas(conv_lista_num_em_binario(converter_pos_dicionario (pre_processar(carregar_perguntas("perguntas_valor_obra_teste2.txt")),dicionario)))
result = w.predict(X_test_valor_obra)  #  Result will be a dictionary using the classes as key and the WiSARD result as values
print ("***** Teste com Valor Obra:",result,'\n')

X_test_outros =incluir_perguntas(conv_lista_num_em_binario(converter_pos_dicionario (pre_processar(carregar_perguntas("perguntas_outros_teste.txt")),dicionario)))
result = w.predict(X_test_outros)  #  Result will be a dictionary using the classes as key and the WiSARD result as values
print ("***** Teste com Outros:",result,'\n')


## Referencias
# https://pt.slideshare.net/andreschwerz/lucene-12290739
# http://nilc.icmc.usp.br/nlpnet/
# http://www.nltk.org/book/
# http://www.nltk.org/howto/portuguese_en.html
# http://www.nltk.org/nltk_data/
# http://www.nltk.org/api/nltk.stem.html#nltk.stem.rslp.RSLPStemmer
# https://github.com/python/cpython/blob/3.6/Lib/tokenize.py
# http://nltk.sourceforge.net/doc/pt-br/tokenize.html
# http://www.inf.ufrgs.br/~viviane/rslp/

#github
# https://github.com/fogodev/voicer
# https://github.com/firmino/PyWANN
# https://github.com/fabiorangel/SS_WiSARD
# https://github.com/aluiziolimafilho/wisard
# https://github.com/aluiziolimafilho/wisard/tree/master/source_python
# https://github.com/firmino/libwann
# https://github.com/fabiorangel/SS_WiSARD
# https://github.com/giordamaug/WisardClassifier
