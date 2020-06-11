import sys
from antlr4 import *
from LULU2Parser import LULU2Parser
from LULU2Listener import LULU2Listener

class LULU2AnalyzerListener(LULU2Listener):
    def __init__(self, output):
        self.output = output
        self.types = ['int', 'bool', 'float', 'string']
        self.variables = []

    def exitType_def(self, ctx:LULU2Parser.Type_defContext):
        self.types.append(ctx.ID()[0].getText())

    def enterVar_def(self, ctx:LULU2Parser.Var_defContext):
        variable = None

        for value in ctx.var_val():
            variable = value.ref().ID().getText()

        self.variables.append(variable)

        name = ctx.type_().getText()
        if name not in self.types:
            self.output.write(f'{name} is not defined\n\n')

    def enterVar_val(self, ctx:LULU2Parser.Var_valContext):
        pass

    def enterArgs_var(self, ctx:LULU2Parser.Args_varContext):
        variable = ctx.ID().getText()
        self.variables.append(variable)

        name = ctx.type_().getText()
        if name not in self.types:
            self.output.write(f'{name} is not defined\n')

    def enterRef(self, ctx:LULU2Parser.RefContext):
        variable = ctx.ID().getText()
        if variable not in self.variables:
            self.output.write(f'reference to {variable} not found. may be you forgot to define it\n')


