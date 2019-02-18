import re
from Tokens import Token
class Sintatico:

    def __init__(self,lista):
        self.lista = lista
        self.token_atual = Token('','',0)
        self.indice_token = 0

    #lembrar de perguntar a João pq que tinha colocado indice_token + 1
    def next_token(self):
        if self.indice_token < len(self.lista):
            self.token_atual = self.lista[self.indice_token]
        self.indice_token += 1

    def get_tokenn(self):
        return self.lista

    def print_tokens(self):
        for i in range(len(self.lista)):
            print(self.lista[i].get_classificacao())

    def programa(self):
        self.next_token()
        if self.token_atual.get_token() == 'program':
            self.next_token()
            if self.token_atual.get_classificacao() == 'Identificador':
                self.next_token()
                if self.token_atual.get_token() == ';':
                    self.next_token()
                else:
                    #print('Faltou um ; | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                #print('Faltou um identificador | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        else:
            #print('Faltou o program | Linha: {}'.format(self.token_atual.get_linha()))
            return False

        if self.decVar():
            if self.declaracoes_de_subs():
                if self.comando_composto():
                    if self.token_atual.get_token() == '.':
                        print('Deu Certo Parceiro')
                        return True
                    else:
                        # print('Faltou um .| Linha: {}'.format(self.token_atual.get_linha()))
                        return False
                else:
                    # print('ERRO COMANDCOMPOSTO | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                # print('ERRO DECSUBS | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        else:
            # print('ERRO DECVAR | Linha: {}'.format(self.token_atual.get_linha()))
            return False


    def decVar(self):
        if self.token_atual.get_token() == 'var':
            self.next_token()
            return self.lista_Declaracao_Var()
        elif self.token_atual.get_token() == '':
            self.next_token()
            return True
        else:
            return False

    def lista_Declaracao_Var(self):
        if self.lI():
            if self.token_atual.get_token() == ':':
                self.next_token()
                if self.tipo():
                    if self.token_atual.get_token()==';':
                        self.next_token()
                        return self.lista_Declaracao_Var_()
                    else:
                        #print('Faltou o ponto vírgula, Iron Man| Linha: {}'.format(self.token_atual.get_linha()))
                        return False
                else:
                    #print('Faltou o tipo, Iron Man | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                #print('Faltou o :, Iron Man | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        else:
            #print('Faltou o Identificador | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def lista_Declaracao_Var_(self):
        if self.lI():
            if self.token_atual.get_token() == ':':
                self.next_token()
                if self.tipo():
                    if self.token_atual.get_token()==';':
                        self.next_token()
                        return self.lista_Declaracao_Var_()
                    else:
                        #print('Faltou o ponto vírgula, Iron Man| Linha: {}'.format(self.token_atual.get_linha()))
                        return False
                else:
                    #print('Faltou o tipo, Iron Man | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                #print('Faltou o :, Iron Man | Linha: {}'.format(self.token_atual.get_linha()))
                return False

#        elif self.token_atual.get_token() == '':
 #           self.next_token()
  #          return True

        else:
            #print('Faltou o Identificador | Linha: {}'.format(self.token_atual.get_linha()))
            #self.next_token()
            return True


    def lI(self):
        if self.token_atual.get_classificacao()=='Identificador':
            self.next_token()
            return self.lI_()
        else:
            #print('Faltou o Identificador Iron Man| Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def lI_(self):
        if self.token_atual.get_token()==',':
            self.next_token()
            if self.token_atual.get_classificacao() == 'Identificador':
                self.next_token()
                return self.lI_()
            else:
                print('Faltou o Identificador Iron Man| Linha: {}'.format(self.token_atual.get_linha()))
                return False

        else:
            #print('ERRO DECLARAÇÂO DE LISTA DE IDENTIFICADORES | Linha: {}'.format(self.token_atual.get_linha()))
            return True

    def tipo(self):
        if self.token_atual.get_token() == 'integer' or self.token_atual.get_token()== 'real' or self.token_atual.get_token() == 'boolean':
            self.next_token()
            return True
        else:
            print('Faltou o Tipo | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def declaracoes_de_subs(self):
        if self.declaracoes_de_subs_():
            return True
        else:
            print('ERRO DECLARAÇÂO DE SUBS | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def declaracoes_de_subs_(self):
        if self.declaracao_de_sub():
            if self.token_atual.get_token() == ';':
                self.next_token()
                return self.declaracoes_de_subs_()
            else:
                print('Faltou o ; | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        #elif self.token_atual.get_token() == '':
         #   self.next_token()
          #  return True
        else:
            #print('ERRO DECLARAÇÃO DE SUB | Linha: {}'.format(self.token_atual.get_linha()))
            #self.next_token()
            return True

    def declaracao_de_sub(self):
        if self.token_atual.get_token() == 'procedure':
            self.next_token()
            if self.token_atual.get_classificacao() == 'Identificador':
                self.next_token()
                if self.argumentos():
                    if self.token_atual.get_token() == ';':
                        self.next_token()
                        if self.decVar():
                            if self.declaracoes_de_subs():
                                return self.comando_composto()
                            else:
                                #print('ERRO DECLARAÇÃO DE SUBS | Linha: {}'.format(self.token_atual.get_linha()))
                                return False
                        else:
                            #print('ERRO DECLARAÇÃO DE VARIÁVEL | Linha: {}'.format(self.token_atual.get_linha()))
                            return False
                    else:
                        #print('Faltou o ; | Linha: {}'.format(self.token_atual.get_linha()))
                        return False
                else:
                    #print('ERRO DE ARGUMENTOS | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                #print('Faltou o identificador | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        else:
            #print('Faltou o procedure | Linha: {}'.format(self.token_atual.get_linha()))
            return False
    def argumentos(self):
        if self.token_atual.get_token() == '(':
            self.next_token()
            if self.lista_de_parametros():
                if self.token_atual.get_token() == ')':
                    self.next_token()
                    return True
                else:
                    #print('Faltou o ) | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                #print('ERRO DE NA LISTA DE PARAMENTROS | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        #elif self.token_atual.get_token() == '':
         #   self.next_token()
          #  return True
        else:
         #   print('ERRO DE ARGUMENTOS | Linha: {}'.format(self.token_atual.get_linha()))
            #self.next_token()
            return True

    def lista_de_parametros(self):
        if self.lI():
            if self.token_atual.get_token()==':':
                self.next_token()
                if self.tipo():
                    return self.lista_de_parametros_()
                else:
                    #print('ERRO DE TIPO | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                #print('Faltou os : | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        else:
            #print('ERRO DE PARAMETRO | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def lista_de_parametros_(self):
        if self.token_atual.get_token() == ';':
            self.next_token()
            if self.lI():
                if self.token_atual.get_token()==':':
                    self.next_token()
                    if self.tipo():
                        return self.lista_de_parametros_()
                    else:
                        #print('ERRO DE TIPO | Linha: {}'.format(self.token_atual.get_linha()))
                        return False
                else:
                    #print('Faltou os : | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                #print('ERRO DE PARAMETRO | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        #elif self.token_atual.get_token()=='':
         #   self.next_token()
          #  return True
        else:
            #print('Faltou o ; | Linha: {}'.format(self.token_atual.get_linha()))
            #self.next_token()
            return True

    def comando_composto(self):
        if self.token_atual.get_token() == 'begin':
            self.next_token()
            if self.comandos_opcionais():
                if self.token_atual.get_token() == 'end':
                    self.next_token()
                    return True
                else:
                    #print('Faltou o end Iron Man| Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                #print('ERRO DE COMANDO | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        else:
            #print('Faltou o begin Iron Man | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def comandos_opcionais(self):
        if self.lista_de_comandos():
            return True
        #elif self.token_atual.get_token() == '':
         #   self.next_token()
          #  return True
        else:
            #print('ERRO DE COMANDO | Linha: {}'.format(self.token_atual.get_linha()))
            #self.next_token()
            return True

    def lista_de_comandos(self):
        if self.comando():
            return self.lista_de_comandos_()
        else:
            #print('ERRO DE COMANDO | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def lista_de_comandos_(self):
        if self.token_atual.get_token() == ';':
            self.next_token()
            if self.comando():
                return self.lista_de_comandos_()
            else:
                return False
        #elif self.token_atual.get_token() == '':
         #   self.next_token()
          #  return True
        else:
           # print('Faltou o ; | Linha: {}'.format(self.token_atual.get_linha()))
           #self.next_token()
            return True

    def comando(self):
        if self.variavel():
            if self.token_atual.get_token()==':=':
                self.next_token()
                return self.expressao()
            else:
                #print('Faltou o := | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        elif self.ativacao_de_procedimento():
            return True
        elif self.comando_composto():
            return True
        elif self.token_atual.get_token()=='if':
            self.next_token()
            if self.expressao():
                if self.token_atual.get_token()=='then':
                    self.next_token()
                    if self.comando():
                        return self.parte_else()
                    else:
                        #print('ERRO DE COMANDO | Linha: {}'.format(self.token_atual.get_linha()))
                        return False
                else:
                    #print('Faltou o then | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                #print('ERRO DE EXPRESSAO | Linha: {}'.format(self.token_atual.get_linha()))
                return False

        elif self.token_atual.get_token()=='while':
            self.next_token()
            if self.expressao():
                if self.token_atual.get_token()=='do':
                    self.next_token()
                    return self.comando()
                else:
                    #print('Faltou o do | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                #print('ERRO DE EXPRESSAO | Linha: {}'.format(self.token_atual.get_linha()))
                return False

        else:
            #print('ERRO DE COMANDO | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def parte_else(self):
        if self.token_atual.get_token() == 'else':
            self.next_token()
            return self._command()
        #elif self.token_atual.get_token() == '':
         #   self.next_token()
          #  return True
        else:
            #print('ERRO ELSE | Linha: {}'.format(self.token_atual.get_linha()))
            #self.next_token()
            return True

    def variavel(self):
        if self.token_atual.get_classificacao()=='Identificador':
            self.next_token()
            return True

    def ativacao_de_procedimento(self):

        if self.token_atual.get_classificacao() == 'Identificador':
            self.next_token()

            if self.token_atual.get_token() == '(':
                self.next_token()
                if self.lista_de_expressoes():
                    if self.token_atual.get_token() == ')':
                        self.next_token()
                        return True
                    else:
                        #print('Falta o ) | Linha: {}'.format(self.token_atual.get_linha()))
                        return False
                else:
                    #print('Faltou ) Iron Man | Linha: {}'.format(self.token_atual.get_linha()))
                    return False

            elif self.token_atual.get_token() == '':
                return True

            else:
                #print('Faltou o ( Iron Man | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        else:
            #print('Faltou o Identificador | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def lista_de_expressoes(self):
        if self.expressao():
            return self.lista_de_expressoes_()
        else:
            #print('ERRO DE EXPRESSAO | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def lista_de_expressoes_(self):
        if self.token_atual.get_token() == ',':
            self.next_token()
            if self.expressao():
                return self.lista_de_expressoes_()
        #elif self.token_atual.get_token()== '':
         #   self.next_token()
          #  return True
        else:
            #print('ERRO NA LISTA DE EXPRESSAO | Linha: {}'.format(self.token_atual.get_linha()))
            #self.next_token()
            return True

    def expressao(self):
        if self.expressao_simples():
            if self.op_relacional():
                return self.expressao_simples()
            else:
                return True
        else:
            #print('ERRO DE EXP SIMPLES | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def expressao_simples(self):
        if self.termo():
            return self.expressao_simples_()
        elif self.sinal():
            if self.termo():
                return self.expressao_simples_()
            else:
                return False
        else:
            return False

    def expressao_simples_(self):
        if self.op_aditivo():
            if self.termo():
                return self.expressao_simples_()
            else:
                #print('ERRO DE TERMO | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        #elif self.token_atual.get_token() == '':
         #   self.next_token()
          #  return True

        else:
           # print('ERRO OP ADITIVO | Linha: {}'.format(self.token_atual.get_linha()))
            #self.next_token()
            return True


    def termo(self):
        if self.fator():
            return self.termo_()
        else:
            #print('ERRO NO FATOR| Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def termo_(self):
        if self.op_multiplicativo():
            if self.fator():
                return self.termo_()
            else:
                #print('ERRO NO FATOR| Linha: {}'.format(self.token_atual.get_linha()))
                return False

        #elif self.token_atual.get_token() == '':
         #   self.next_token()
          #  return True
        else:
           # print('ERRO DE TERMO | Linha: {}'.format(self.token_atual.get_linha()))
            #self.next_token()
            return True

    def fator(self):
        if self.token_atual.get_classificacao() == 'Identificador':
            self.next_token()

            if self.token_atual.get_token() == '(':
                self.next_token()
                if self.lista_de_expressoes():
                    if self.token_atual.get_token() == ')':
                        self.next_token()
                        return True
                    else:
                        #print('Faltou o ) | Linha: {}'.format(self.token_atual.get_linha()))
                        return False
                else:
                    #print('ERRO NA LISTA DE EXPRESSAO | Linha: {}'.format(self.token_atual.get_linha()))
                    return False

            #elif self.token_atual.get_token() == '':
            #    self.next_token()
             #   return True

            else:
                #print('Faltou o ( Iron Man| Linha: {}'.format(self.token_atual.get_linha()))
                return True

        elif self.token_atual.get_classificacao() == 'Inteiro':
            self.next_token()
            return True

        elif self.token_atual.get_classificacao() == 'Float':
            self.next_token()
            return True

        elif self.token_atual.get_token() == 'true':
            self.next_token()
            return True

        elif self.token_atual.get_token() == 'false':
            self.next_token()
            return True

        elif self.token_atual.get_token() == '(':
            self.next_token()
            if self.expressao():
                if self.token_atual.get_token() == ')':
                    self.next_token()
                    return True
                else:
                    #print('Faltou o ) Iron Man| Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                #print('ERRO DE EXPRESSAO | Linha: {}'.format(self.token_atual.get_linha()))
                return False

        elif self.token_atual.get_token() == 'not':
            self.next_token()
            return self.fator()

        else:
            #print('ERRO DE FATOR | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def sinal(self):
        if self.token_atual.get_token()=='+':
            self.next_token()
            return True
        elif self.token_atual.get_token()=='-':
            self.next_token()
            return True
        else:
            #print('ERRO DE SINAL | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def op_relacional(self):
        if self.token_atual.get_token()=='=':
            self.next_token()
            return True
        elif self.token_atual.get_token()=='<':
            self.next_token()
            return True
        elif self.token_atual.get_token()=='>':
            self.next_token()
            return True
        elif self.token_atual.get_token()=='<=':
            self.next_token()
            return True
        elif self.token_atual.get_token()=='>=':
            self.next_token()
            return True
        elif self.token_atual.get_token()=='<>':
            self.next_token()
            return True
        else:
            #print('ERRO DE OP RELACIONAL | Linha: {}'.format(self.token_atual.get_linha()))
            return False


    def op_aditivo(self):
        if self.token_atual.get_token() == '+':
            self.next_token()
            return True
        elif self.token_atual.get_token() == '-':
            self.next_token()
            return True
        elif self.token_atual.get_token() == 'or':
            self.next_token()
            return True
        else:
            #print('ERRO DE OP ADITIVO | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def op_multiplicativo(self):
        if self.token_atual.get_token() == '*':
            self.next_token()
            return True
        elif self.token_atual.get_token() == '/':
            self.next_token()
            return True
        elif self.token_atual.get_token() == 'and':
            self.next_token()
            return True
        else:
            #print('ERRO DE OP MULTIPLICATIVO | Linha: {}'.format(self.token_atual.get_linha()))
            return False