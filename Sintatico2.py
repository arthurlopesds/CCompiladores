import re
from Tokens import Token


class Sintatico:

    def __init__(self, lista):
        self.lista = lista
        self.token_atual = Token('', '', 0)
        self.indice_token = 0
        self.pilha = []
        self.x = 0
        self.nomeprog = ''
        #self.tipos = []

    def next_token(self):
        if self.indice_token < len(self.lista):
            self.token_atual = self.lista[self.indice_token]
        self.indice_token += 1

    def get_tokenn(self):
        return self.lista

    def print_tokens(self):
        for i in range(len(self.lista)):
            print(self.lista[i].get_classificacao())

    def perc_pilha(self):
        k = len(self.pilha) - 1
        i = self.pilha[k][0]

        while i != '$':
            if self.pilha[k][0] == self.token_atual.get_token():
                return True
            k -= 1
            i = self.pilha[k][0]
        return False

    def esvazia_pilha(self):
        if self.x == 0:
            k = len(self.pilha) - 1
            i = self.pilha[k][0]

            while i != '$':
                self.pilha.pop()
                k = len(self.pilha) - 1
                i = self.pilha[k][0]
            self.pilha.pop()

    def pega_tipo(self, controle, tipo):
        k = len(self.pilha) - 1

        if controle:
            if tipo == 'st':
                self.pilha.append([self.token_atual.get_token(), 'st'])
            elif tipo == '$':
                self.pilha.append(['$', 'st'])
            else:
                self.pilha.append([self.token_atual.get_token(), ''])
        else:
             while self.pilha[k][1] == '':
                self.pilha[k][1] = tipo
                k -= 1


    def varre_pilha(self):
        for i in range(len(self.pilha) -1, 0 , -1):
            if self.token_atual.get_token() == self.pilha[i][0]:
                return False

        return True


    def programa(self):
        self.next_token()
        if self.token_atual.get_token() == 'program':
            self.pega_tipo(True, '$')
            ############################################################33
            self.next_token()
            if self.token_atual.get_classificacao() == 'Identificador':
                self.pega_tipo(True, 'st')
                self.nomeprog = self.token_atual.get_token()
                self.next_token()
                if self.token_atual.get_token() == ';':
                    self.next_token()
                else:
                    print('Faltou um ; | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                print('Faltou um identificador | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        else:
            print('Faltou o program | Linha: {}'.format(self.token_atual.get_linha()))
            return False

        if self.decVar():

            if self.declaracoes_de_subs():
                if self.comando_composto():
                    if self.token_atual.get_token() == '.':
                        print('Deu Certo Parceiro')
                    else:
                        print('Faltou um .| Linha: {}'.format(self.token_atual.get_linha()))
                        return False
                else:
                    return False
                    # print('ERRO COMANDCOMPOSTO | Linha: {}'.format(self.token_atual.get_linha()))
            else:
                return False
                # print('ERRO DECSUBS | Linha: {}'.format(self.token_atual.get_linha()))

    def decVar(self):
        if self.token_atual.get_token() == 'var':
            self.next_token()
            return self.lista_Declaracao_Var()
        else:
            return True

    def lista_Declaracao_Var(self):
        if self.lI():
            if self.token_atual.get_token() == ':':
                self.next_token()
                if self.tipo():
                    if self.token_atual.get_token() == ';':
                        self.next_token()
                        if self.lista_Declaracao_Var_():
                            return True
                        else:
                            return False
                    else:
                        # print('Faltou o ponto vírgula, Iron Man| Linha: {}'.format(self.token_atual.get_linha()))
                        return False
                else:
                    # print('Faltou o tipo, Iron Man | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                # print('Faltou o :, Iron Man | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        else:
            # print('Faltou o Identificador | Linha: {}'.format(self.token_atual.get_linha()))
            return True

    def lista_Declaracao_Var_(self):
        if self.lI():
            if self.token_atual.get_token() == ':':
                self.next_token()
                if self.tipo():
                    if self.token_atual.get_token() == ';':
                        self.next_token()
                        return self.lista_Declaracao_Var_()
                    else:
                        # print('Faltou o ponto vírgula, Iron Man| Linha: {}'.format(self.token_atual.get_linha()))
                        return False
                else:
                    # print('Faltou o tipo, Iron Man | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                # print('Faltou o :, Iron Man | Linha: {}'.format(self.token_atual.get_linha()))
                return False

        #        elif self.token_atual.get_token() == '':
        #           self.next_token()
        #          return True

        else:
            # print('Faltou o Identificador | Linha: {}'.format(self.token_atual.get_linha()))
            # self.next_token()
            return True

    def lI(self):
        if self.token_atual.get_classificacao() == 'Identificador':
            if self.x == 0:
                if self.token_atual.get_token() != self.nomeprog:
                    if self.perc_pilha():  # semantico
                        print('Variavel Existente, não é possível declarar novamente. | Linha: {} '.format(
                            self.token_atual.get_linha()))
                        return False
                    else:
                        #self.pilha.append(self.token_atual.get_token())
                        self.pega_tipo(True, '')
                        self.next_token()
                        return self.lI_()
                else:
                    print('Não é possível declarar a variável, pois este é o nome do programa. | Linha: {}'.format(
                        self.token_atual.get_linha()))
                    return False
            else:
                if self.varre_pilha():
                    print('Variavel {} não declarada | Linha: {} '.format(self.token_atual.get_token(),
                                                                          self.token_atual.get_linha()))
                    return False
        else:
            # print('Faltou o Identificador Iron Man| Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def lI_(self):
        if self.token_atual.get_token() == ',':
            self.next_token()

            if self.token_atual.get_classificacao() == 'Identificador':
                if self.x == 0:
                    if self.token_atual.get_token() != self.nomeprog:
                        if self.perc_pilha():  # semantico
                            print('Variavel Existente, não é possível declarar novamente. | Linha: {} '.format(
                                self.token_atual.get_linha()))
                            return False
                        else:
                            #self.pilha.append(self.token_atual.get_token())
                            self.pega_tipo(True, '')
                            self.next_token()
                            return self.lI_()
                    else:
                        print('Não é possível declarar a variável, pois este é o nome do programa. | Linha: {}'.format(
                            self.token_atual.get_linha()))
                        return False
                else:
                    if self.varre_pilha():
                        print('Variavel {} não declarada | Linha: {} '.format(self.token_atual.get_token(),
                                                                              self.token_atual.get_linha()))
                        return False
            else:
                # print('Faltou o Identificador | Linha: {}'.format(self.token_atual.get_linha()))
                return False

        else:
            # print('ERRO DECLARAÇÂO DE LISTA DE IDENTIFICADORES | Linha: {}'.format(self.token_atual.get_linha()))
            return True

    def tipo(self):
        if self.token_atual.get_token() == 'integer':
            self.pega_tipo(False, self.token_atual.get_token())
            self.next_token()
            return True
        elif self.token_atual.get_token() == 'real':
            self.pega_tipo(False, self.token_atual.get_token())
            self.next_token()
            return True
        elif self.token_atual.get_token() == 'boolean':
            self.pega_tipo(False, self.token_atual.get_token())
            self.next_token()
            return True
        else:
            print('Faltou o Tipo | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def declaracoes_de_subs(self):
        if self.declaracoes_de_subs_():
            return True

        return True

    def declaracoes_de_subs_(self):
        if self.declaracao_de_sub():
            if self.token_atual.get_token() == ';':
                self.next_token()
                return self.declaracoes_de_subs_()
            else:
                print('Faltou o ; | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        # elif self.token_atual.get_token() == '':
        #   self.next_token()
        #  return True
        else:
            # print('ERRO DECLARAÇÃO DE SUB | Linha: {}'.format(self.token_atual.get_linha()))
            # self.next_token()
            return True

    def declaracao_de_sub(self):
        if self.token_atual.get_token() == 'procedure':
            self.next_token()
            if self.token_atual.get_classificacao() == 'Identificador':
                if self.x == 0:
                    if self.token_atual.get_token() != self.nomeprog:
                        if self.perc_pilha():  # semantico
                            print('Variavel Existente, não é possível declarar novamente. | Linha: {} '.format(
                                self.token_atual.get_linha()))
                            return False
                        else:
                            self.pega_tipo(True, 'st')
                            self.pega_tipo(True, '$')
                            self.next_token()
                            if self.argumentos():  # ESSA PARTE FOI IDENTADA 1 VEZ
                                if self.token_atual.get_token() == ';':
                                    self.next_token()
                                    if self.decVar():
                                        if self.declaracoes_de_subs():
                                            return self.comando_composto()
                                        else:
                                            # print('ERRO DECLARAÇÃO DE SUBS | Linha: {}'.format(self.token_atual.get_linha()))
                                            return False
                                    else:
                                        # print('ERRO DECLARAÇÃO DE VARIÁVEL | Linha: {}'.format(self.token_atual.get_linha()))
                                        return False
                                else:
                                    # print('Faltou o ; | Linha: {}'.format(self.token_atual.get_linha()))
                                    return False
                            else:
                                # print('ERRO DE ARGUMENTOS | Linha: {}'.format(self.token_atual.get_linha()))
                                return False
                    else:
                        print('Não é possível declarar a variável, pois este é o nome do programa. | Linha: {}'.format(
                            self.token_atual.get_linha()))
                        return False
                else:
                    if self.varre_pilha():
                        print('Variavel {} não declarada | Linha: {} '.format(self.token_atual.get_token(),
                                                                              self.token_atual.get_linha()))
                    return False
            else:
                # print('Faltou o identificador | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        else:
            # print('Faltou o procedure | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def argumentos(self):
        if self.token_atual.get_token() == '(':
            self.next_token()
            if self.lista_de_parametros():
                if self.token_atual.get_token() == ')':
                    self.next_token()
                    return True
                else:
                    # print('Faltou o ) | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                # print('ERRO DE NA LISTA DE PARAMENTROS | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        # elif self.token_atual.get_token() == '':
        #   self.next_token()
        #  return True
        else:
            #   print('ERRO DE ARGUMENTOS | Linha: {}'.format(self.token_atual.get_linha()))
            # self.next_token()
            return True

    def lista_de_parametros(self):
        if self.lI():
            if self.token_atual.get_token() == ':':
                self.next_token()
                if self.tipo():
                    return self.lista_de_parametros_()
                else:
                    # print('ERRO DE TIPO | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                # print('Faltou os : | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        else:
            # print('ERRO DE PARAMETRO | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def lista_de_parametros_(self):
        if self.token_atual.get_token() == ';':
            self.next_token()
            if self.lI():
                if self.token_atual.get_token() == ':':
                    self.next_token()
                    if self.tipo():
                        return self.lista_de_parametros_()
                    else:
                        # print('ERRO DE TIPO | Linha: {}'.format(self.token_atual.get_linha()))
                        return False
                else:
                    # print('Faltou os : | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                # print('ERRO DE PARAMETRO | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        # elif self.token_atual.get_token()=='':
        #   self.next_token()
        #  return True
        else:
            # print('Faltou o ; | Linha: {}'.format(self.token_atual.get_linha()))
            # self.next_token()
            return True

    def comando_composto(self):

        if self.token_atual.get_token() == 'begin':
            self.x += 1  # semantico , variaveis usadas
            self.next_token()

            if self.comandos_opcionais():
                if self.token_atual.get_token() == 'end':
                    self.x -= 1  # semantico , variaveis usadas
                    self.esvazia_pilha()
                    self.next_token()
                    return True
                else:
                    # print('Faltou o end Iron Man| Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                # print('ERRO DE COMANDO | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        else:
            # print('Faltou o begin Iron Man | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def comandos_opcionais(self):
        if self.token_atual.get_token() == 'end':
            self.x -= 1  # semantico , variaveis usadas
            self.esvazia_pilha()
            return True

        if self.lista_de_comandos():
            return True
        else:
            return False

    def lista_de_comandos(self):
        if self.comando() and self.lista_de_comandos_():
            return True
        else:
            # print('ERRO DE COMANDO | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def lista_de_comandos_(self):
        if self.token_atual.get_token() == ';':
            self.next_token()
            if self.comando():
                if self.lista_de_comandos_():
                    return True
                else:
                    return False
        return True

    def comando(self):
        if self.variavel():
            if self.token_atual.get_token() == ':=':
                self.next_token()
                if self.expressao():
                    return True
                else:
                    return False
            elif self.ativacao_de_procedimento():
                return True
            else:
                print("Erro na atribuição em comando.")
                return False
        elif self.token_atual.get_token() == 'if':
            self.next_token()
            if self.expressao():
                if self.token_atual.get_token() == 'then':
                    self.next_token()
                    if self.comando():
                        if self.parte_else():
                            self.next_token()
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif self.token_atual.get_token() == 'while':
            self.next_token()
            if self.expressao():
                if self.token_atual.get_token() == 'do':
                    self.next_token()
                    if self.comando():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        #################################################################3
        elif self.token_atual.get_token() == 'case':
            self.next_token()
            if self.seletor():
                if self.token_atual.get_token() == 'of':
                    self.next_token()
                    if self.seletores():
                        return self.parte_else()
                    else:
                        return False
                else:
                    return False
            else:
                return False

        if self.comando_composto():
            return True
        else:
            return False

    def seletor(self):
        if self.token_atual.get_classificacao() == 'Inteiro' or self.token_atual.get_classificacao() == 'real':
            self.next_token()
            return True
        else:
            return False

    def seletores(self):
        if self.seletor():
            if self.token_atual.get_token() == ':':
                self.next_token()
                if self.comando():
                    if self.token_atual.get_token() == ';':
                        self.next_token()
                        return self.seletores_()
                    else:
                        False
                else:
                    return False
            else:
                return True
        else:
            return False

    def seletores_(self):
        if self.seletor():
            if self.token_atual.get_token() == ':':
                self.next_token()
                if self.comando():
                    if self.token_atual.get_token() == ';':
                        self.next_token()
                        return self.seletores_()
                    else:
                        False
                else:
                    return False
            else:
                return True
        else:
            return True

    #########################################################################

    def parte_else(self):
        if self.token_atual.get_token() == 'else':
            self.next_token()
            return self.comando()
        # elif self.token_atual.get_token() == '':
        #   self.next_token()
        #  return True
        else:
            # print('ERRO ELSE | Linha: {}'.format(self.token_atual.get_linha()))
            # self.next_token()
            return True

    def variavel(self):
        if self.token_atual.get_classificacao() == 'Identificador':
            if self.x == 0:
                if self.perc_pilha():  # semantico
                    print('Variavel Existente, não é possível declarar novamente. | Linha: {} '.format(
                        self.token_atual.get_linha()))
                    return False
                else:
                    self.pilha.append(self.token_atual.get_token())
                    self.pega_tipo(True, '')
            else:
                if self.varre_pilha():
                    print('Variavel {} não declarada | Linha: {} '.format(self.token_atual.get_token(),
                                                                          self.token_atual.get_linha()))
                    return False
            self.next_token()
            return True
        else:
            return False

    def ativacao_de_procedimento(self):

        # if self.token_atual.get_classificacao() == 'Identificador':
        # self.next_token()

        if self.token_atual.get_token() == '(':
            self.next_token()
            if self.lista_de_expressoes():
                if self.token_atual.get_token() == ')':
                    self.next_token()
                    return True
                else:
                    # print('Falta o ) | Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                # print('Faltou ) Iron Man | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        else:
            # print('Faltou o ( Iron Man | Linha: {}'.format(self.token_atual.get_linha()))
            return True

    # else:
    # print('Faltou o Identificador | Linha: {}'.format(self.token_atual.get_linha()))
    #  return False

    def lista_de_expressoes(self):
        if self.expressao():
            if self.lista_de_expressoes_():
                return True
        else:
            # print('ERRO DE EXPRESSAO | Linha: {}'.format(self.token_atual.get_linha()))
            return False

        return True

    def lista_de_expressoes_(self):
        if self.token_atual.get_token() == ',':
            self.next_token()
            if self.expressao():
                return self.lista_de_expressoes_()
        # elif self.token_atual.get_token()== '':
        #   self.next_token()
        #  return True
        else:
            # print('ERRO NA LISTA DE EXPRESSAO | Linha: {}'.format(self.token_atual.get_linha()))
            # self.next_token()
            return True

    def expressao(self):
        if self.expressao_simples():
            if self.op_relacional() and self.expressao_simples():
                return True
            else:
                return True
        else:
            # print('ERRO DE EXP SIMPLES | Linha: {}'.format(self.token_atual.get_linha()))
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
                # print('ERRO DE TERMO | Linha: {}'.format(self.token_atual.get_linha()))
                return False
        # elif self.token_atual.get_token() == '':
        #   self.next_token()
        #  return True

        else:
            # print('ERRO OP ADITIVO | Linha: {}'.format(self.token_atual.get_linha()))
            # self.next_token()
            return True

    def termo(self):
        if self.fator() and self.termo_():
            return True
        else:
            # print('ERRO NO FATOR| Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def termo_(self):
        if self.op_multiplicativo():
            if self.fator():
                return self.termo_()
            else:
                # print('ERRO NO FATOR| Linha: {}'.format(self.token_atual.get_linha()))
                return False

        # elif self.token_atual.get_token() == '':
        #   self.next_token()
        #  return True
        else:
            # print('ERRO DE TERMO | Linha: {}'.format(self.token_atual.get_linha()))
            # self.next_token()
            return True

    def fator(self):
        if self.token_atual.get_classificacao() == 'Identificador':
            self.next_token()

            if self.token_atual.get_token() == '(':
                self.next_token()  # CUIDADO AQUI MZR
                if self.lista_de_expressoes():
                    if self.token_atual.get_token() == ')':
                        self.next_token()
                        return True
                    else:
                        # print('Faltou o ) | Linha: {}'.format(self.token_atual.get_linha()))
                        return False
                else:
                    # print('ERRO NA LISTA DE EXPRESSAO | Linha: {}'.format(self.token_atual.get_linha()))
                    return False

            # elif self.token_atual.get_token() == '':
            #    self.next_token()
            #   return True

            else:
                # print('Faltou o ( Iron Man| Linha: {}'.format(self.token_atual.get_linha()))
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
                    # print('Faltou o ) Iron Man| Linha: {}'.format(self.token_atual.get_linha()))
                    return False
            else:
                # print('ERRO DE EXPRESSAO | Linha: {}'.format(self.token_atual.get_linha()))
                return False

        elif self.token_atual.get_token() == 'not':
            self.next_token()
            return self.fator()

        else:
            # print('ERRO DE FATOR | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def sinal(self):
        if self.token_atual.get_token() == '+':
            self.next_token()
            return True
        elif self.token_atual.get_token() == '-':
            self.next_token()
            return True
        else:
            # print('ERRO DE SINAL | Linha: {}'.format(self.token_atual.get_linha()))
            return False

    def op_relacional(self):
        if self.token_atual.get_token() == '=':
            self.next_token()
            return True
        elif self.token_atual.get_token() == '<':
            self.next_token()
            return True
        elif self.token_atual.get_token() == '>':
            self.next_token()
            return True
        elif self.token_atual.get_token() == '<=':
            self.next_token()
            return True
        elif self.token_atual.get_token() == '>=':
            self.next_token()
            return True
        elif self.token_atual.get_token() == '<>':
            self.next_token()
            return True
        else:
            # print('ERRO DE OP RELACIONAL | Linha: {}'.format(self.token_atual.get_linha()))
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
            # print('ERRO DE OP ADITIVO | Linha: {}'.format(self.token_atual.get_linha()))
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
            # print('ERRO DE OP MULTIPLICATIVO | Linha: {}'.format(self.token_atual.get_linha()))
            return False

