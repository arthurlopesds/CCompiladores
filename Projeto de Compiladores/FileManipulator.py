class FileManipulator:

    #Definindo os atributos da classe
    def __init__(self):
        self._lineslist = []                            #Essa classe vai me fornecer uma lista de linhas contida no programa
        self._arq = 'programa.txt'                      #Caminho para o arquivo que será lido

    def reader(self):
        with open(self._arq, 'r') as ref:               #Ler o arquivo e chamar o método que separa as palavras
            for line in ref:
                self.separator(line)
                self.clean(self.get_lineslist())

    def separator(self, line):
        separate_lines = line.split('\s')               #Separa pelos espaços em branco usando RE

        for word in separate_lines:
            word = word.strip()
            self._lineslist.append(word)
    
    def clean(self, list):
        coment = False
        nl = 0
        line = ''

        for i in range(len(list)):
            line = ''
            for j in range(len(list[i])):

                if list[i][j] == '{':                   #Início do Comentário
                    coment = True
                    nl = i
                if not list[i][j] == '}' and coment:    #Se a chave não fechou e a linha acabou
                    continue
                else:
                    if list[i][j] == '}' and coment:    #Se há comentário e fechamento
                        coment = False
                        continue
                    elif list[i][j] == '}' and not coment: #Se houve fechemento porém não há comentário erro
                        print('ERRO Falta Abertura de Comentário começado na Linha {}\n'.format(i+1))
                    else:                                   #Se não é comentário add
                        line = line + list[i][j]

            list[i] = line

        if coment:
            print('Erro pq não fechou')
        return list

    def get_lineslist(self):
        return self._lineslist

    def print_lines(self):
        for i in range(len(self._lineslist)):
            print(self._lineslist[i])