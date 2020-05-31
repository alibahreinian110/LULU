import sys
from antlr4 import *
from LULU2Lexer import LULU2Lexer
from LULU2Parser import LULU2Parser
def main(argv):
    input = FileStream(argv[1])
    lexer = LULU2Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = LULU2Parser(stream)
    tree = parser.program()
    output = open("output.txt","w")

    # the costum listener defined by ourselver
    walker = ParseTreeWalker()
    walker.walk(htmlChat, tree)

    output.close()
if __name__ == '__main__':
    main(sys.argv)
