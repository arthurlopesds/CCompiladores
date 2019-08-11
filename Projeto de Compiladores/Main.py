from FileManipulator import FileManipulator
from Lexical import Lexical
#from Tokens import Tokens
#from Syntactic import Syntactic

r = FileManipulator()
r.reader()
r.print_lines()

lex = Lexical(r.get_lineslist())
lex.table_creator()

tokens = lex.get_tokens()
for i in range(len(tokens)):
    print(tokens[i].get_token())
