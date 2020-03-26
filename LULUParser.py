# Generated from LULU.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write(" \4\2\t\2\3\2\3\2\3\2\3\2\7\2\t\n\2\f\2\16\2\f\13\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2\25\n\2\f\2\16\2\30\13\2")
        buf.write("\3\2\7\2\33\n\2\f\2\16\2\36\13\2\3\2\2\3\2\3\2\2\2\2!")
        buf.write("\2\4\3\2\2\2\4\5\b\2\1\2\5\n\7\t\2\2\6\7\7\3\2\2\7\t\7")
        buf.write("\4\2\2\b\6\3\2\2\2\t\f\3\2\2\2\n\b\3\2\2\2\n\13\3\2\2")
        buf.write("\2\13\r\3\2\2\2\f\n\3\2\2\2\r\16\7\13\2\2\16\34\3\2\2")
        buf.write("\2\17\20\f\3\2\2\20\21\7\5\2\2\21\26\7\t\2\2\22\23\7\3")
        buf.write("\2\2\23\25\7\4\2\2\24\22\3\2\2\2\25\30\3\2\2\2\26\24\3")
        buf.write("\2\2\2\26\27\3\2\2\2\27\31\3\2\2\2\30\26\3\2\2\2\31\33")
        buf.write("\7\13\2\2\32\17\3\2\2\2\33\36\3\2\2\2\34\32\3\2\2\2\34")
        buf.write("\35\3\2\2\2\35\3\3\2\2\2\36\34\3\2\2\2\5\n\26\34")
        return buf.getvalue()


class LULUParser ( Parser ):

    grammarFileName = "LULU.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "DIGITS", "LOWERCASE", "UPERCASE", "TYPE", "ACCESS_MODIFIER", 
                      "ID", "RALATION_OP", "BITWISE_OP", "LOGIC_OP", "ARITHMATIC_OP", 
                      "WHITESPACE", "NEWLINE", "HEX_DIGITS", "HEX_NUMBERS", 
                      "INT_CONST", "REAL_CONST", "BOOL_CONST", "CONST_VAL" ]

    RULE_args_var = 0

    ruleNames =  [ "args_var" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    DIGITS=4
    LOWERCASE=5
    UPERCASE=6
    TYPE=7
    ACCESS_MODIFIER=8
    ID=9
    RALATION_OP=10
    BITWISE_OP=11
    LOGIC_OP=12
    ARITHMATIC_OP=13
    WHITESPACE=14
    NEWLINE=15
    HEX_DIGITS=16
    HEX_NUMBERS=17
    INT_CONST=18
    REAL_CONST=19
    BOOL_CONST=20
    CONST_VAL=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Args_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(LULUParser.TYPE, 0)

        def ID(self):
            return self.getToken(LULUParser.ID, 0)

        def args_var(self):
            return self.getTypedRuleContext(LULUParser.Args_varContext,0)


        def getRuleIndex(self):
            return LULUParser.RULE_args_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs_var" ):
                listener.enterArgs_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs_var" ):
                listener.exitArgs_var(self)



    def args_var(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LULUParser.Args_varContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_args_var, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3
            self.match(LULUParser.TYPE)
            self.state = 8
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LULUParser.T__0:
                self.state = 4
                self.match(LULUParser.T__0)
                self.state = 5
                self.match(LULUParser.T__1)
                self.state = 10
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 11
            self.match(LULUParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LULUParser.Args_varContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_args_var)
                    self.state = 13
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 14
                    self.match(LULUParser.T__2)
                    self.state = 15
                    self.match(LULUParser.TYPE)
                    self.state = 20
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==LULUParser.T__0:
                        self.state = 16
                        self.match(LULUParser.T__0)
                        self.state = 17
                        self.match(LULUParser.T__1)
                        self.state = 22
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 23
                    self.match(LULUParser.ID) 
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.args_var_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def args_var_sempred(self, localctx:Args_varContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




