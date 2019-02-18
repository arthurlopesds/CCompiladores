from LeArquivo import LeArquivo
from AnalisadorLexico import Lexico
from Sintatico import Sintatico


leituraArq = LeArquivo()
leituraArq.LeArq()

lex = Lexico(leituraArq.get_lista())
lex.criar_lista_token()
tokens = lex.get_tokens()
sintat = Sintatico(tokens)

for index in range(len(tokens)):
    print(tokens[index].get_token_info())

sintat.programa()


