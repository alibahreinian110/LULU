import sys
from antlr4 import *
from LULU2Parser import LULU2Parser
from LULU2Listener import LULU2Listener

class LULU2AnalyzerListener(LULU2Listener):
    def __init__(self, output):
        self.output = output
        self.types = ['int', 'bool', 'float', 'string']

    def exitType_def(self, ctx:LULU2Parser.Type_defContext):
        self.types.append(ctx.ID()[0].getText())

    def enterVar_def(self, ctx:LULU2Parser.Var_defContext):
        name = ctx.type_().getText()
        if name not in self.types:
            self.output.write(f'{name} is not defined\n\n')

    def enterArgs_var(self, ctx:LULU2Parser.Args_varContext):
        name = ctx.type_().getText()
        if name not in self.types:
            self.output.write(f'{name} is not defined\n')

