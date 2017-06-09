

def carregar_perguntas(nome_arq):  
	perguntas = []
	with open(nome_arq) as file:
		for line in file:
			line = line.strip()
			print(line)
			perguntas.append(line)
	return perguntas

def criar_dicionario_ordenado(lista):
	# tornar matriz trid em lista de palavras
	lista_unica_palavras = []
	j=0	
	while (j < len(lista)):
		i=0
		while (i < len(lista[j])):
			k=0
			while (k < len(lista[j][i])):
				lista_unica_palavras.append(lista[j][i][k])
				k=k+1
			i=i+1
		j=j+1
	print("****lista_unica_palavras",lista_unica_palavras, "tamanho:", len(lista_unica_palavras))


	dicionario = []
	for palavra in lista_unica_palavras:
		if palavra not in dicionario:
			dicionario.append(palavra)
	print ("***** dicionario", dicionario, "tamanho:", len(dicionario))		
	return  dicionario


def pos_dicionario(palavra, dicionario):
	i = 0;
	while (i < len(dicionario)):
		if (palavra == dicionario[i]):
			return i
		i=i+1
	return -1

def converter_pos_dicionario(lista,dic):
	conv_lista = []	
	for pergunta in lista:
		conv_pergunta = []
		for palavra in pergunta:
			conv_pergunta.append(pos_dicionario(palavra,dic))
		conv_lista.append(conv_pergunta)		
	return conv_lista

def conv_lista_num_em_binario(lista):
	conv_lista = []	
	for pergunta in lista:
		conv_pergunta = ''
		for palavra in pergunta:
			nro_bin = "{0:b}".format(palavra)
			tam_nro_bin = len(nro_bin)
			nro_tot_bin = '' 
			i=0
			while (i<(6-tam_nro_bin)):   # preencher com zeros na frente caso tamanho da palavra seja menor do que o max
				nro_tot_bin += '0'
				i=i+1
			nro_tot_bin += nro_bin			
			conv_pergunta+=nro_tot_bin
		conv_lista.append(conv_pergunta)

		conv_lista_preenchida =[]
		# preencher perguntas com zero na frente caso nao tenham o tamanho maximo: usando maximo de 5 palavras em cada pergunta, cada palavra 6 bits, logo cada pergunta deveria ter 30 bits
		for pergunta in conv_lista:
			tam_nro_bin = len(pergunta)
			i=0				
			while (i<(30-tam_nro_bin)):   # preencher com zeros no final caso tamanho da palavra seja menor do que o max
				pergunta += '0'
				i=i+1
			conv_lista_preenchida.append(pergunta)
	return conv_lista_preenchida

def incluir_perguntas(lista_bin):
	#converter em array de bits
	conv_lista = []
	for pergunta in lista_bin:
		pergunta_bits = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]	
		i=0
		while (i<30):
			if pergunta[i]=='1':
				pergunta_bits[i]=1
			i+=1 
		conv_lista.append(pergunta_bits)
	return conv_lista

def classificar(classificador, nro_vezes):
	lista = []
	i=0
	while (i<nro_vezes):
		lista.append(classificador)
		i+=1
	return lista