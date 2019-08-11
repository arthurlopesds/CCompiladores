REGEX_IDENTIFIER = '[a-zA-Z]+\w*'
REGEX_FLOAT = '\d+\.\d*'
REGEX_REMAINING_SYMBOLS = '\>=|\<=|\:=|\<>|\>|\<|\,|\+|\-|\*|\(|\)|\:(?!\=)|\.$|\;|\/'
REGEX_POINT_NUMBER_SPACE = '\s\.\d+'
REGEX_POINT_NUMBER_BEGIN = '^\.\d+'
REGEX_INTEGER = '\d+'

'''
REGEX_IDENTIFIER = '[a-zA-Z]+\w*'
REGEX_INTEGER = '\d+'
REGEX_FLOAT = '\d+.\d'
REGEX_POINT_NUMBER_SPACE = '\s.\d+'
REGEX_POINT_NUMBER_BEGIN = '^.\d+'
REGEX_REMAINING_SYMBOLS = '\>=|\<=|\:=|\<>|\>|\<|\,|\+|\-|\*|\(|\)|\:(?!\=)|\.$|\;|\/'

SPACE = ' '
REGEX_IDENTIFIER = '[a-zA-Z]+\w*'
REGEX_FLOAT = '\d+\.\d*'
REGEX_REMAINING_SYMBOLS = '\>=|\<=|\:=|\<>|\>|\<|\,|\+|\-|\*|\(|\)|\:(?!\=)|\.$|\;|\/'
REGEX_POINT_NUMBER_SPACE = '\s\.\d+'
REGEX_POINT_NUMBER_BEGIN = '^\.\d+'
REGEX_INTEGER = '\d+'
elif self._comparator(word, REGEX_REMAINING_SYMBOLS, 0, False):
            if word == ':=':
                classe = "Operdor de Atribuição"
            elif word == '\<|\>|\=|\<=|\>=|\<>':
                classe = "Operador relacional"
            elif word == '\+|\-':
                classe = "Comando Aditivo"
            elif word == '\*|\/':
                classe = "Comando Multiplicativo"
            else:
                classe = "Delimitador"
        else:
            classe = "Não foi possível classificar o token"
'''