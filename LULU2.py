import sys
from antlr4 import *
from LULU2Lexer import LULU2Lexer
from LULU2Parser import LULU2Parser
from LULU2SymbolTableListener import LULU2SymbolTableListener
from LULU2AnalyzerListener import LULU2AnalyzerListener


def main(argv):
    input = FileStream(argv[1])
    lexer = LULU2Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = LULU2Parser(stream)
    tree = parser.program()
    output = open("output.txt","w")

    analyzer = LULU2AnalyzerListener(output)
    symbol_table = LULU2SymbolTableListener(output)
    walker = ParseTreeWalker()
    walker.walk(analyzer, tree)
    walker.walk(symbol_table, tree)

    output.close()
if __name__ == '__main__':
    main(sys.argv)
