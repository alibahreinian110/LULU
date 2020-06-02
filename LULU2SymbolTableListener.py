import sys
from antlr4 import *
from LULU2Parser import LULU2Parser
from LULU2Listener import LULU2Listener


class LULU2SymbolTableListener(LULU2Listener):
    def __init__(self, output):
        self.output = output

    def indicateVariable(self,ctx):
       # for i in range(ctx.getChildCount()):
        #    if ctx.type_def():
         #       child = ctx.type_def()
          #      self.output.write(f'{child.ID().getText()}         {child.Type().getText()}         Width         Address')
           # elif ctx.var_def():
            #    child = ctx.var_def()
             #   self.output.wirte(f'{child.var_val().ref().ID().getText()}         {child.type_().getText()}         Width         Address')
            #elif ctx.fun_def():
             #   child = ctx.fun_def()
              #  self.output.wirte(f'{child.ID().getText()}         {child.Function().getText()}         Width         Address')
            #elif ctx.args_var():
             #   child.args_var()
              #  self.output.wirte(f'{child.ID().getText()}         {child.type_().getText()}         Width         Address')
        pass

    def enterProgram(self, ctx:LULU2Parser.ProgramContext):
        self.output.write("----program----\n")

    def exitProgram(self, ctx:LULU2Parser.ProgramContext):
        self.output.write('---End of program----\n')

    def enterFt_def(self, ctx:LULU2Parser.Ft_defContext):
        #self.output.write("----%s----\n"%ctx.getText())
        #self.output.write('Name    |    Type    |    Width    |    Address\n')

        #if ctx.type_def():
            
        #self.indicateVariable(ctx)
        pass

    def exitFt_def(self, ctx:LULU2Parser.Ft_defContext):
        #self.output.write("----End of %s----\n\n"%ctx.getText())
        pass

    def enterType_def(self, ctx:LULU2Parser.Type_defContext):
        self.output.write("----%s----\n"%ctx.ID()[0].getText())
        self.output.write('Name    |    Type    |    Width    |    Address\n')
        
        for component in ctx.component():
             if component.var_def():
                 for definition in component.var_def():

                     for value in definition.var_val():
                         self.output.write(f'{value.ref()[0].ID().getText()}         ')
                         self.output.write(f'{definition.type_().getText()}         ')

    def exitType_def(self, ctx:LULU2Parser.Type_defContext):
        self.output.write("----End of %s----\n\n"%ctx.ID()[0].getText())

    def enterComponent(self, ctx:LULU2Parser.ComponentContext):
        if ctx.block():
            self.output.write(f'----{ctx.getText()}----\n')
            self.output.write('Name    |    Type    |    Width    |    Address\n')
            self.indicateVariable(ctx)

    def exitComponent(self, ctx:LULU2Parser.ComponentContext):
        if ctx.block():
            self.output.write(f'----End of {ctx.getText()}----\n\n')

    def enterFun_def(self, ctx:LULU2Parser.Fun_defContext):
        self.output.write("----%s----\n"%ctx.ID().getText())
        self.output.write('Name    |    Type    |    Width    |    Address\n')
        self.indicateVariable(ctx)

    def exitFun_def(self, ctx:LULU2Parser.Fun_defContext):
        self.output.write("----End of %s----\n\n"%ctx.ID().getText())

    def enterStmt(self, ctx:LULU2Parser.StmtContext):
        if ctx.cond_stmt():
            child = None

            for item in ctx.cond_stmt():
                if isinstance(item, LULU2Parser.BlockContext):
                    child = item
                    break
                else:
                    continue

            if child:
                self.output.write(f'----{ctx.getText()}----\n')
                self.output.write('Name    |    Type    |    Width    |    Address\n')
                self.indicateVariable(ctx)

        elif ctx.loop_stmt():
            child = None

            for item in ctx.loop_stmt():
                if isinstance(item, LULU2Parser.BlockContext):
                    child = item
                    break
                else:
                    continue

            if child:
                self.output.write(f'----{ctx.getText()}----\n')
                self.output.write('Name    |    Type    |    Width    |    Address\n')
                self.indicateVariable(ctx)

    def exitStmt(self, ctx:LULU2Parser.StmtContext):
        if ctx.cond_stmt():
            child = None

            for item in ctx.cond_stmt():
                if isinstance(item, LULU2Parser.BlockContext):
                    self.output.write(f'----End of {ctx.getText()}----\n\n')
                    break
                else:
                    continue

        elif ctx.loop_stmt():
            child = None

            for item in ctx.loop_stmt():
                if isinstance(item, LULU2Parser.BlockContext):
                    self.output.write(f'----End of {ctx.getText()}----\n\n')
                    break
                else:
                    continue

    def enterCond_stmt(self, ctx:LULU2Parser.Cond_stmtContext):
        if ctx.block():
            self.output.write(f'----End of {ctx.getText()}----\n\n')
            self.output.write('Name    |    Type    |    Width    |    Address\n\n')
            self.indicateVariable(ctx)

    def exitCond_stmt(self, ctx:LULU2Parser.Cond_stmtContext):
        if ctx.block():
            self.output.write(f'----End of {ctx.getText()}----\n\n')

    def enterSwitch_body(self, ctx:LULU2Parser.Switch_bodyContext):
        self.output.write("----%s----\n\n"%ctx.getText())
        self.output.write('Name    |    Type    |    Width    |    Address\n')
        self.indicateVariable(ctx)

    def exitSwitch_body(self, ctx:LULU2Parser.Switch_bodyContext):
        self.output.write("----End of %s----\n\n"%ctx.getText())

    def enterLoop_stmt(self, ctx:LULU2Parser.Loop_stmtContext):
        if ctx.block():
            self.output.write(f'----{ctx.getText()}----\n')
            self.output.write('Name    |    Type    |    Width    |    Address\n')
            self.indicateVariable(ctx)

    def exitLoop_stmt(self, ctx:LULU2Parser.Loop_stmtContext):
        if ctx.block():
            self.output.write(f'----End of {ctx.getText}----\n\n')
