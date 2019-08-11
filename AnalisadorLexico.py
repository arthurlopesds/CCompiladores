import re
from Tokens import Token
from ExpressoesReg import REGEX_IDENTIFICADOR
from ExpressoesReg import REGEX_PONTO_NUMERO_ESPACO
from ExpressoesReg import REGEX_PONTO_NUMERO
from ExpressoesReg import REGEX_FLOAT
from ExpressoesReg import REGEX_INT
from ExpressoesReg import REGEX_SIMBOLOS_RESTANTES
from ExpressoesReg import ESPACO

class Lexico:
    def __init__(self,lista):

        self.lista = lista
        self._offset = 0
        self._tokens = []
        self.palavras_reservadas = ('program', 'var', 'integer', 'real', 'boolean', 'procedure', 'begin', 'end', 'if', 'then',
                              'else', 'while', 'do', 'not','true','false','case','of')

    def get_tokens(self):
        return self._tokens

    def criar_lista_token(self):
        for i in range(len(self.lista)):

            if self.lista[i] == '':
                continue

            self.identificador(self.lista[i], i)
            self.num_float(self.lista[i], i)
            self.simbolos_restantes(self.lista[i], i)
            self.set_classificacao(self.lista[i], i)

    def set_classificacao(self, linha, numero_linha):
        #print('LINHA: {}'.format(linha))
        tokens = linha.split(' ')
        #print('TOKENS = {}'.format(tokens))
        for palavra in tokens:
            if not palavra == '' or palavra == ' ':
                classificacao = self.get_classificacao(palavra)
                if classificacao == 'Nao foi possivel classificar':
                    print('Nao foi possivel classificar : {} | Linha: {}'.format(palavra,numero_linha+1))
                    continue
                else:
                    novo_Objeto = Token(palavra, classificacao, int(numero_linha + 1))
                    self._tokens.append(novo_Objeto)


    def get_classificacao(self, token):

        if self.funcao(token, REGEX_IDENTIFICADOR, 0, False):
            if token in self.palavras_reservadas:
                return 'Palavra Reservada'
            else:
                return 'Identificador'
        elif self.funcao(token, REGEX_FLOAT, 0, False):
            return 'Float'
        elif self.funcao(token, REGEX_INT, 0, False):
            return 'Inteiro'
        elif self.funcao(token, '\>=|\<=|\:=|\<>', 0, False):
            if token == ':=':
                return 'Atribuicao'
            else:
                return 'Operador Relacional'
        elif self.funcao(token, '\>|\<|\,|\+|\-|\*|\(|\)|\:(?!\=)|\.$|\;|\/', 0, False):
            if token == '>' or token == '<':
                return 'Operador Relacional'
            elif token == '+' or token == '-':
                return 'Operador Aditivo'
            elif token == '*' or token == '/':
                return 'Operator Multiplicativo'
            else:
                return 'Delimitador'
        else:
            return 'Nao foi possivel classificar'

    def funcao(self, linha, str_pattern, other_offset, boolean):

        pattern = re.compile(str_pattern)
        matches = pattern.finditer(linha) #Vê se a linha da match


        if boolean:
            self._offset = 0

            for match in matches: #se deu macth vem para o for para colocar os espaços
                s = match.start()

                e = match.end()

                linha = self._inserir_espaco(linha, match.start() + self._offset + other_offset, match.end() + self._offset)#colocando espaços

            return linha

        else:
            if pattern.findall(linha):
                return True
            else:
                return False

    def identificador(self, linha, index):

        linha = self.funcao(linha, REGEX_IDENTIFICADOR, 0, True)
        self.lista[index] = linha

    def num_float(self, linha, index):

        self._offset = 0
        linha = self.funcao(linha, REGEX_FLOAT, 0, True)
        self.lista[index] = linha
        self._point_number(linha, index)

    def _point_number(self, linha, index):

        linha = self.funcao(linha, REGEX_PONTO_NUMERO_ESPACO, 2, True)
        linha = self.funcao(linha, REGEX_PONTO_NUMERO, 1, True)
        self.lista[index] = linha

    def simbolos_restantes(self, linha, index):

        linha = self.funcao(linha, REGEX_SIMBOLOS_RESTANTES, 0, True)
        self.lista[index] = linha

    def _inserir_espaco(self, linha, inicio, end):


        linha = linha[:end] + ESPACO + linha[end:] #espaço entre as sentenças
        self._offset += 1

        if inicio > 0: #se nao for a primeira palavra, coloca espaço antes dela
            linha = linha[:inicio] + ESPACO + linha[inicio:]
            self._offset += 1

        return linha

