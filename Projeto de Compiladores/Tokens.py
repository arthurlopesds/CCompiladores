class Tokens:

    def __init__(self, word, classif, line):
        self.word = word
        self.classif = classif
        self.line = line

    def get_token(self):
        return 'Token = {:<10} Classification = {:<25} Line = {:<20}'.format(self.word, self.classif, self.line)

    def get_word(self):
        return self.word

    def get_class(self):
        return self.classif
    
    def get_line(self):
        return self.line