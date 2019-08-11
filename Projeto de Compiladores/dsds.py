#Importações
import re

#Declaração de vars
nomearq = 'programa.txt'
qtde_linhas = 0
linha_atual = 0
elemento_atual = 0
reservadas = ['program', 'var', 'begin', 'end', 'integer', 'real']
p_reservadas = []
instrucoes_divididas = []
delimitadores = []
atribuicoes = []
inteiros = []
indentificadores = []
lista = []

#Efetuando a leitura do arquivo
with open(nomearq, "r") as arquivo:
    instrucoes = arquivo.readlines()
    qtde_linhas = len(instrucoes)

#Percorrendo o arquivo e efetuando um pré-processamento para separação de delimitadores
#Esse procedimento é importante para tornar possível a classificação dos mesmos
#Percorrendo A1 organizando e transformando em A2
while linha_atual < len(instrucoes):
    instrucoes_divididas.append(instrucoes[linha_atual].split(' '))

    elemento_atual = 0
    while elemento_atual < len(instrucoes_divididas[linha_atual]):
        #Algoritmo utilizado:
        #01.Ache a palavra com o delimitador e remova-o
        #02.Aplique .insert() e coloque o delimitador na posição elemento_atual + 1
        #03.Incremente elemento atual, saltando o delimitador para não haver loop infinito
        if(instrucoes_divididas[linha_atual][elemento_atual]._contains_(';')):
            instrucoes_divididas[linha_atual][elemento_atual] = instrucoes_divididas[linha_atual][elemento_atual].strip(';\n')
            instrucoes_divididas[linha_atual].insert(elemento_atual + 1, ';')
            elemento_atual += 1

        if (instrucoes_divididas[linha_atual][elemento_atual]._contains(':')) and not(instrucoes_divididas[linha_atual][elemento_atual].contains_(':=')):
            instrucoes_divididas[linha_atual][elemento_atual] = instrucoes_divididas[linha_atual][elemento_atual].strip(':\n')
            instrucoes_divididas[linha_atual].insert(elemento_atual + 1, ':')
            elemento_atual += 1

        if (instrucoes_divididas[linha_atual][elemento_atual]._contains('.') and not(instrucoes_divididas[linha_atual][elemento_atual].contains_(':='))):
            instrucoes_divididas[linha_atual][elemento_atual] = instrucoes_divididas[linha_atual][elemento_atual].strip('.\n')
            instrucoes_divididas[linha_atual].insert(elemento_atual + 1, '.')
            elemento_atual += 1

        elemento_atual += 1

    linha_atual += 1
#A1 Organizado com sucesso, segue a classificação

linha_atual = 0
elemento_atual = 0

#Percorrendo o arquivo A2 para então efetuar a classificação
while linha_atual < len(instrucoes):
    #Algoritmo utilizado:
    #01.Separe o arquivo por linhas e então as linhas por palavras
    #02.Classifique cada palavra pelo re e então adicione em sua respectiva lista
    instrucoes_divididas.append(instrucoes[linha_atual].split(' '))

    elemento_atual = 0
    while elemento_atual < len(instrucoes_divididas[linha_atual]):
        if instrucoes_divididas[linha_atual][elemento_atual].strip('\n') in reservadas:
            p_reservadas.append(instrucoes_divididas[linha_atual][elemento_atual].strip('\n'))
            p_reservadas.append(linha_atual + 1)
            #Modificação sex, 15/02
            lista.append(instrucoes_divididas[linha_atual][elemento_atual].strip('\n'))
            lista.append('p_reservada')
            lista.append(linha_atual + 1)

        elif re.match(r':|;|\.|,|\(|\)', instrucoes_divididas[linha_atual][elemento_atual].strip('\n')) \
                and instrucoes_divididas[linha_atual][elemento_atual] != ':=':
            delimitadores.append(instrucoes_divididas[linha_atual][elemento_atual].strip('\n'))
            delimitadores.append(linha_atual + 1)
            # Modificação sex, 15/02
            lista.append(instrucoes_divididas[linha_atual][elemento_atual].strip('\n'))
            lista.append('delimitador')
            lista.append(linha_atual + 1)

        elif instrucoes_divididas[linha_atual][elemento_atual] == ':=':
            atribuicoes.append(instrucoes_divididas[linha_atual][elemento_atual])
            atribuicoes.append(linha_atual + 1)
            # Modificação sex, 15/02
            lista.append(instrucoes_divididas[linha_atual][elemento_atual].strip('\n'))
            lista.append('atribuição')
            lista.append(linha_atual + 1)

        elif re.match(r'\d+', instrucoes_divididas[linha_atual][elemento_atual]) and '.' \
                not in instrucoes_divididas[linha_atual][elemento_atual]:
            inteiros.append(instrucoes_divididas[linha_atual][elemento_atual])
            inteiros.append(linha_atual + 1)
            # Modificação sex, 15/02
            lista.append(instrucoes_divididas[linha_atual][elemento_atual].strip('\n'))
            lista.append('inteiro')
            lista.append(linha_atual + 1)

        else:
            if '{' not in instrucoes_divididas[linha_atual][elemento_atual]:
                if '}' not in instrucoes_divididas[linha_atual][elemento_atual]:
                    indentificadores.append(instrucoes_divididas[linha_atual][elemento_atual])
                    indentificadores.append(linha_atual + 1)
                    # Modificação sex, 15/02
                    lista.append(instrucoes_divididas[linha_atual][elemento_atual].strip('\n'))
                    lista.append('identificador')
                    lista.append(linha_atual + 1)

        elemento_atual += 1

    linha_atual += 1
#A2 classificado, segue a saída de dados

#Saída de dados
#print('Reservadas: palavra/linha:')
#print(p_reservadas)
#print('Delimitadores: delimitador/linha:')
#print(delimitadores)
#print('Atribuições: atribuição/linha')
#print(atribuicoes)
#print('Inteiros: inteiro/linha')
#print(inteiros)
#print('Indentificadores: indentificador/linha')
#print(indentificadores)

#Modificação sex, 15/02
print(lista)