from NewLexical.LeArquivo import  LeArquivo
from NewLexical.AnalisadorLexico import Lexico

leituraArq = LeArquivo()
leituraArq.LeArq()

lex = Lexico(leituraArq.get_lista())
lex.criar_lista_token()
tokens = lex.get_tokens()


for index in range(len(tokens)):
    print(tokens[index].get_token_info())