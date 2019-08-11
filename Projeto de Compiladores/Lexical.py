from RE import REGEX_IDENTIFIER
from RE import REGEX_INTEGER
from RE import REGEX_FLOAT
from RE import REGEX_POINT_NUMBER_SPACE
from RE import REGEX_POINT_NUMBER_BEGIN
from RE import REGEX_REMAINING_SYMBOLS
from Tokens import Tokens
import re

class Lexical:

    def __init__(self,list):
        self.list = list
        self.tokens = []
        self.reserved_words = ('program', 'var', 'integer', 'real', 'boolean', 'procedure',
                               'begin', 'end', 'if', 'then', 'else', 'while', 'do', 'not')
        self.nSpaces = 0

    def get_tokens(self):
        return self.tokens
    
    #Ele vai receber a lista com as linhas e vai mandar add espaços e classificar linha por linha
    def table_creator(self):
        for i in range(len(self.list)): #Vai varrer linha por linha a fim de classificá-las

            if self.list[i] == '':
                continue

            #Adicionar espaço varrendo a lista atrás de matchs, achou o match add espaço
            self._isIdentifier(self.list[i], i)
            self._isFloat(self.list[i], i)
            self._isSymbol(self.list[i], i)
            self._classifier(self.list[i], i)

    def _classifier(self, line, index):
        print('LINHA: {}'.format(line))
        words = line.split(' ')

        for word in words:
            word = word.strip() #remover as tabulações
            if not word == '' or word == ' ': # O programa vai ignorar os espaços e os vazios
                cl = self.getClassification(word)
                new = Tokens(word, cl, int(index + 1))
                self.tokens.append(new)

    def getClassification(self, word):
        classe = ''

        if self._comparator(word, REGEX_IDENTIFIER, 0, False):
            if word in self.reserved_words:
                classe = "Palavra Reservada"
            else:
                classe = "Identificador"
        elif self._comparator(word, REGEX_FLOAT, 0, False):
            classe = "Número Real"
        elif self._comparator(word, REGEX_INTEGER, 0, False):
            classe = "Número Inteiro"
        elif self._comparator(word, '\>=|\<=|\:=|\<>', 0, False):
            if word == ':=':
                classe = 'Operador de Atribuição'
            else:
                classe = 'Operador Relacional'
        elif self._comparator(word, '\>|\<|\,|\+|\-|\*|\(|\)|\:(?!\=)|\.$|\;|\/', 0, False):
            if word == '>' or word == '<':
                classe = 'Relational Operator'
            elif word == '+' or word == '-':
                classe = 'Additive Operator'
            elif word == '*' or word == '/':
                classe = 'Multiplicative Operator'
            else:
                classe = 'Delimiter'
        else:
            classe = 'I could not classify'

        return classe

    def _isIdentifier(self, line, index):
        line = self._comparator(line, REGEX_IDENTIFIER, 0, True)
        self.list[index] = line

    def _isFloat(self, line, index):
        self.nSpaces = 0
        line = self._comparator(line, REGEX_FLOAT, 0, True)
        print('LINHA DO FLOAT: {}'.format(line))
        self.list[index] = line
        print('LINHA DO INDEX: {}'.format(self.list[index]))
        self._isPointNumber(line, index)

    
    def _isPointNumber(self, line, index):

        line = self._comparator(line, REGEX_POINT_NUMBER_SPACE, 2, True)
        line = self._comparator(line, REGEX_POINT_NUMBER_BEGIN, 1, True)
        self.list[index] = line

    def _isSymbol(self, line, index):
        line = self._comparator(line, REGEX_REMAINING_SYMBOLS, 0, True)
        self.list[index] = line

    def _comparator(self, line, p, other_offset, boolean):

        pattern = re.compile(p)
        match = pattern.finditer(line)

        #Haverá duas comparações uma para adicionar espaços entre os simbolos e as palavras
        #e a segunda para quando for classificar os tokens
        if boolean: #quando boolean for vdd haverá apenas uma comparação para adição de espaço
            self.nSpaces = 0

            for m in match: #ele vai comparar todo o conteúdo da lista a procura de um match
                line = self.add_space(line, m.start() + self.nSpaces + other_offset, m.end() + self.nSpaces)
            
            return line

        else: #usado quando for realmente classificar os tokens
            if pattern.findall(line):
                return True
            else:
                return False

    def add_space(self, line, begin, end):
        #Vamos adicionar espaço antes e depois das palavras, porém se o match ocorreu
        #adicionando espaço ao final de cada match
        line = line[:end] + " " + line[end:]
        self.nSpaces += 1

        #no primeiro indice não há necessidade de colocar espaço antes da palavra
        if begin > 0: #Se o começo do match não for no início
            line = line[:begin] + " " + line[begin:]
            self.nSpaces += 1

        return line    