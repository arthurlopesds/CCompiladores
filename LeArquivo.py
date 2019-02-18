class LeArquivo:
    global lin
    def __init__(self):
        self._lista = []
        self._nome = "codigo.txt"

    def LeArq(self):
        global lin
        with open(self._nome,"r") as arquivo:
            for linha in arquivo:
                self._separar(linha)
        comentario = False
        for i in range(len(self._lista)):

            for j in range(len(self._lista[i])):
                if self._lista[i][j] == '{':
                    comentario = True
                    lin = i+1
                if comentario and not self._lista[i][j] == '}':
                    str = list(self._lista[i])
                    #print(list(self._lista[i]))
                    str[j] = " "
                    #print('STR[J]:{}'.format(str[j]))

                    self._lista[i] = ''.join(str)
                    #print('STR:{}'.format(str))
                else:
                    if self._lista[i][j] == '}' and comentario:
                        str = list(self._lista[i])
                        str[j] = " "
                        self._lista[i] = ''.join(str)
                        comentario = False

                    elif self._lista[i][j] == '}' and not comentario:
                        print('ERRO 502 - Falta Abertura de Comentário começado na Linha {}\n'.format(i+1))

        if comentario == True:
            print('ERRO 502 - Falta Fechamento do Comentário começado na Linha {}\n'.format(lin))



    def _separar(self,linha):
        separar_linha = linha.split('\s')
        for palavra in separar_linha:
            #print('PALAVRA : {}'.format(palavra))
            palavra = palavra.strip()
            #print('PALAVRA STRIPADA: {}'.format(palavra))

            self._lista.append(palavra)


    def print_lista(self):
        for i in range(len(self._lista)):
            print(self._lista[i])

    def get_lista(self):
        return self._lista
