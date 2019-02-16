class Token:

    def __init__(self, token, classificacao, linha):
        self._token = token
        self._classificacao = classificacao
        self._linha = linha

    def get_token_info(self):
        return 'Token = {:<20} Classificacao = {:<20} Linha = {:<20}'.format(self._token, self._classificacao, self._linha)

    def get_token(self):
        return self._token

    def get_classificacao(self):
        return self._classificacao
