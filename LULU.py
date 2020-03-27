import sys
from antlr4 import *
from LULULexer import LULULexer
from LULUParser import LULUParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = LULULexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LULUParser(stream)
    tree = parser.program()


if __name__ == '__main__':
    main(sys.argv)
