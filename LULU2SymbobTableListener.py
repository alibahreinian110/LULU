import sys
from antlr4 import *
from LULU2Parser import LULU2Parser
from LULU2Listener import LULU2Listener


class LULU2SymbolTableListener(LULU2Listener):
    def __init__(self, output):
        self.output = output

    def enterProgram(self, ctx:LULU2Parser.ProgramContext):
        output.write("----%s----"%ctx.getText())

    def exitProgram(self, ctx:LULU2Parser.ProgramContext):
        pass

    def enterFt_def(self, ctx:LULU2Parser.Ft_defContext):
        output.write("----%s----"%ctx.getText())

    def exitFt_def(self, ctx:LULU2Parser.Ft_defContext):
        pass

    def enterType_def(self, ctx:LULU2Parser.Type_defContext):
        output.write("----%s----"%ctx.ID()[0].getText())

    def exitType_def(self, ctx:LULU2Parser.Type_defContext):
        pass

    def enterComponent(self, ctx:LULU2Parser.ComponentContext):
        if ctx.block:
            self.output.write(f'----{ctx.getText()}----')

    def exitComponent(self, ctx:LULU2Parser.ComponentContext):
        pass

    def enterFun_def(self, ctx:LULU2Parser.Fun_defContext):
        output.write("----%s----"%ctx.ID().getText())

    def exitFun_def(self, ctx:LULU2Parser.Fun_defContext):
        pass

    def enterStmt(self, ctx:LULU2Parser.StmtContext):
        pass

    def exitStmt(self, ctx:LULU2Parser.StmtContext):
        pass

    def enterCond_stmt(self, ctx:LULU2Parser.Cond_stmtContext):
        pass

    def exitCond_stmt(self, ctx:LULU2Parser.Cond_stmtContext):
        pass

    def enterSwitch_body(self, ctx:LULU2Parser.Switch_bodyContext):
        output.write("----%s----"%ctx.getText())

    def exitSwitch_body(self, ctx:LULU2Parser.Switch_bodyContext):
        pass

    def enterLoop_stmt(self, ctx:LULU2Parser.Loop_stmtContext):
        pass

    def exitLoop_stmt(self, ctx:LULU2Parser.Loop_stmtContext):
        pass
