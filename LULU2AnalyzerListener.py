import sys
from antlr4 import *
from LULU2Parser import LULU2Parser
from LULU2Listener import LULU2Listener


class function:
    def __init__(self, name, input_types, output_types):
        self.name = name
        self.inputs = input_types
        self.outputs = output_types

    def __str__(self):
        return self.name


class LULU2AnalyzerListener(LULU2Listener):
    def __init__(self, output):
        self.output = output
        self.types = ['int', 'bool', 'float', 'string']
        self.variables = []
        self.functions = []

    def enterType_def(self, ctx:LULU2Parser.Type_defContext):
        if ctx.ID()[0].getText() not in self.types:
            self.types.append(ctx.ID()[0].getText())
        else:
            self.output.write(f'type with name {ctx.ID()[0].getText()} already exists')
        

    def enterFun_def(self, ctx:LULU2Parser.Fun_defContext):
        input_types = []
        output_types = []
        name = ctx.ID().getText()

        children = ctx.getChildren()
        flag = True

        for child in children:
            if isinstance(child, LULU2Parser.Args_varContext) and flag:
                output_types.append(child.getText())
            elif child.getText() == 'function':
                flag = False
            elif isinstance(child, LULU2Parser.Args_varContext) and not flag:
                input_types.append(child.getText())
        
        func = function(name, input_types, output_types)
        self.functions.append(func)
        
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

    def enterAssign(self, ctx:LULU2Parser.AssignContext):
        expr = ctx.expr()

        if isinstance(expr.func_call(), LULU2Parser.Func_callContext):
            function = None
            function_call = expr.func_call().handle_call()

            for func in self.functions:
                if function_call.ID().getText() == func.name:
                    function = func
                    break
            
            if function is not None:
                if function_call.params() is not None:
                    # TODO: find out the mechanism
                    pass
                else:
                    if not function.inputs == []:
                        self.output.write(f'function {function.name} gets arguments')
            else:
                self.output.write(f'function {functiona_call.ID().getText()} is not defined')

            for i in range(len(function.outputs)):
            
                variable = ctx.var()[i].ref()[0].ID().getText()
                if variable not in self.variables:
                    self.output.write('output variable is not defined')
            
            if len(function.outputs) != len(ctx.var()):
                self.output.write(f'function {function.name} expected {len(function.outputs)} but got {len(ctx.var())}')


    def enterHandle_call(self, ctx:LULU2Parser.Handle_callContext):
        function = None

        for func in self.functions:
            if func.name == ctx.ID().getText():
                function = func
        
        if function is not None:
            for i in range(len(function.inputs)):

                try:
                    parameter = ctx.params(i)
                    if function.inputs[i] == 'int':
                        if not parameter.expr().const_val().Int_const():
                            self.output.write(f'type int is needed but {parameter.expr().const_val().getText()} given')
                    elif function.inputs[i] == 'bool':
                        if not parameter.expr().const_val().Bool_const():
                            self.output.write(f'type bool is needed but {parameter.expr().const_val().getText()} given')
                    elif function.inputs[i] == 'float':
                        if not parameter.expr().const_val().Float_const():
                            self.output.write(f'type float is needed but {parameter.expr().const_val().getText()} given')
                    elif function.inputs[i] == 'string':
                        if not parameter.expr().const_val().String_const():
                            self.output.write(f'type string is needed but {parameter.expr().const_val().getText()} given')
                except:
                    self.output.write(f'function {function.name} gets {len(function.inputs)} but got less\n')

            #if len(function.inputs) > len(ctx.params()):
               # self.output.write(f'function {function.name} expected {len(function.inputs())} but got {len(ctx.params())}')

        else:
            self.output.write(f'function {ctx.ID().getText()} is not defined')
