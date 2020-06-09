import sys
from antlr4 import *
from LULU2Parser import LULU2Parser
from LULU2Listener import LULU2Listener

def alocate_array_width(array):
    if type(array) == str:
        return len(array)*2+2
    else:
        return len(array)


def alocate_width(ctx):

    # for use in fun_def()
    if isinstance(ctx, LULU2Parser.Fun_defContext):
        return 30

    # for use in type_def()
    elif isinstance(ctx, LULU2Parser.Type_defContext):
        return 20

    # for use in var_def() and args_var()
    elif isinstance(ctx, LULU2Parser.Var_defContext) or isinstance(ctx, LULU2Parser.Args_varContext):
        if ctx.type_().Int():
            return 4
        elif ctx.type_().Bool():
            return 1
        elif ctx.type_().Float():
            return 8
        elif ctx.type_().String():
            return 2
        else:
            return 0


class LULU2SymbolTableListener(LULU2Listener):
    def __init__(self, output):
        self.output = output
        self.address_stack = []
        self.global_offset = 0

    def enterProgram(self, ctx:LULU2Parser.ProgramContext):
        self.output.write("----program----\n")
        self.address_stack.append(self.global_offset)

    def exitProgram(self, ctx:LULU2Parser.ProgramContext):
        self.output.write(f'width = {self.global_offset}\n')
        self.output.write('---End of program----\n')

    def enterFt_def(self, ctx:LULU2Parser.Ft_defContext):
        pass

    def exitFt_def(self, ctx:LULU2Parser.Ft_defContext):
        pass

    def enterType_def(self, ctx:LULU2Parser.Type_defContext):
        self.address_stack.append(self.global_offset)
        self.output.write("----%s----\n"%ctx.ID()[0].getText())
        self.output.write('Name    |    Type    |    Width    |    Address\n')
        for component in ctx.component():
            if component.fun_def():
                for value in component.fun_def():
                     self.output.write(f'{value.ID().getText()}         ')
                     self.output.write("function         ")

    def exitType_def(self, ctx:LULU2Parser.Type_defContext):
        width = alocate_width(ctx)
        start = self.address_stack.pop()
        final = self.global_offset - start
        width += final
        self.output.write(f'width = {width}\n')
        self.output.write("----End of %s----\n\n"%ctx.ID()[0].getText())

    def enterVar_def(self, ctx:LULU2Parser.Var_defContext):
        addon = 0
        multon = 0
        width = alocate_width(ctx)

        for value in ctx.var_val():
            # calculating string const
            if ctx.type_().String():
                if value.expr().const_val():
                    addon = alocate_array_width(value.expr().getText())

            # calculation of arrays
            if value.ref().expr():
                multon = alocate_array_width(value.ref().expr().getText())

            self.output.write(f'{value.ref().ID().getText()}         ')
            self.output.write(f'{ctx.type_().getText()}         ')
            if addon:
                self.output.write(f'{width + addon}        \n')
                self.global_offset += width+addon
                addon = 0

            elif multon:
                self.output.write(f'{width * multon}         \n')
                self.global_offset += width+multon
                multon = 0

            else:
                self.output.write(f'{width}         \n')
                self.global_offset += width

    def enterComponent(self, ctx:LULU2Parser.ComponentContext):
        pass

    def exitComponent(self, ctx:LULU2Parser.ComponentContext):
        pass

    def enterFun_def(self, ctx:LULU2Parser.Fun_defContext):
        self.address_stack.append(self.global_offset)
        self.output.write("----%s----\n"%ctx.ID().getText())
        self.output.write('Name    |    Type    |    Width    |    Address\n')

        definition = ctx.block()
        if definition.stmt():
            for statement in definition.stmt():
                if statement.cond_stmt():
                    self.output.write("if         ")
                    self.output.write("conditional scope         \n")
                elif statement.loop_stmt():
                    self.output.write("loop         ")
                    self.output.write("loop scope         \n")

    def exitFun_def(self, ctx:LULU2Parser.Fun_defContext):
        width = alocate_width(ctx)
        start = self.address_stack.pop()
        final = self.global_offset - start
        width += final
        self.output.write(f'width = {width}\n')
        self.output.write("----End of %s----\n\n"%ctx.ID().getText())

    def enterArgs_var(self, ctx:LULU2Parser.Args_varContext):
        width = alocate_width(ctx)

        self.output.write(f'{ctx.ID().getText()}         ')
        self.output.write(f'{ctx.type_().getText()}         ')
        self.output.write(f'{width}         \n')
        self.global_offset += width

    def enterStmt(self, ctx:LULU2Parser.StmtContext):
        pass

    def exitStmt(self, ctx:LULU2Parser.StmtContext):
        pass

    def enterCond_stmt(self, ctx:LULU2Parser.Cond_stmtContext):
        if ctx.block():
            self.address_stack.append(self.global_offset)
            self.output.write(f'----End of {ctx.getText()}----\n\n')
            self.output.write('Name    |    Type    |    Width    |    Address\n\n')

    def exitCond_stmt(self, ctx:LULU2Parser.Cond_stmtContext):
        if ctx.block():
            start = self.address_stack.pop()
            final = self.global_offset - start
            self.output.Write(f' width = {final}\n')
            self.output.write(f'----End of {ctx.getText()}----\n\n')

    def enterSwitch_body(self, ctx:LULU2Parser.Switch_bodyContext):
        self.address_stack.append(self.global_offset)
        self.output.write("----%s----\n\n"%ctx.getText())
        self.output.write('Name    |    Type    |    Width    |    Address\n')

    def exitSwitch_body(self, ctx:LULU2Parser.Switch_bodyContext):
        start = self.address_stack.pop()
        final = self.global_offset - start
        self.output.write(f' width = {final}\n')
        self.output.write("----End of %s----\n\n"%ctx.getText())

    def enterLoop_stmt(self, ctx:LULU2Parser.Loop_stmtContext):
        if ctx.block():
            self.address_stack.append(self.global_offset)
            self.output.write(f'----{ctx.getText()}----\n')
            self.output.write('Name    |    Type    |    Width    |    Address\n')

    def exitLoop_stmt(self, ctx:LULU2Parser.Loop_stmtContext):
        if ctx.block():
            start = self.address_stack.pop()
            final = self.global_offset - start
            self.output.write(f' width = {final}\n')
            self.output.write(f'----End of {ctx.getText}----\n\n')
