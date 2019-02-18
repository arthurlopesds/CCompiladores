#s = ("Eu sou", "burra", "demais armaria {burra}")
s=[]
print(type(s))
s = ["Eu sou", "burra", "demais armaria {burra","demais} burra"]

def clean(list):
        coment = False
        nl = 0
        linha = ''

        for i in range(len(list)):
            linha = ''
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
                        linha = linha + list[i][j]

            list[i] = linha

        if coment:
            print('Erro pq não fechou')


        return list

clean(s)
print(s)