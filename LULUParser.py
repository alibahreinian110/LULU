# Generated from LULU.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3")
        buf.write("\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5/\n\5\3\6\3\6\3\6\2\2\7\2\4\6\b")
        buf.write("\n\2\6\3\2\3\b\3\2\t\13\3\2\f\16\3\2+/\2G\2\f\3\2\2\2")
        buf.write("\4\16\3\2\2\2\6\20\3\2\2\2\b.\3\2\2\2\n\60\3\2\2\2\f\r")
        buf.write("\t\2\2\2\r\3\3\2\2\2\16\17\t\3\2\2\17\5\3\2\2\2\20\21")
        buf.write("\t\4\2\2\21\7\3\2\2\2\22/\7\17\2\2\23/\7\20\2\2\24/\7")
        buf.write("\21\2\2\25/\7\22\2\2\26/\7\23\2\2\27/\7\24\2\2\30/\7\25")
        buf.write("\2\2\31/\7\26\2\2\32/\7\27\2\2\33/\7\30\2\2\34/\7\31\2")
        buf.write("\2\35/\7\32\2\2\36/\7\33\2\2\37/\7\34\2\2 /\7\35\2\2!")
        buf.write("/\7\36\2\2\"/\7\37\2\2#/\7 \2\2$/\7!\2\2%&\7\"\2\2&/\7")
        buf.write("#\2\2\'/\7$\2\2(/\7%\2\2)/\7&\2\2*/\7\'\2\2+/\7(\2\2,")
        buf.write("/\7)\2\2-/\7*\2\2.\22\3\2\2\2.\23\3\2\2\2.\24\3\2\2\2")
        buf.write(".\25\3\2\2\2.\26\3\2\2\2.\27\3\2\2\2.\30\3\2\2\2.\31\3")
        buf.write("\2\2\2.\32\3\2\2\2.\33\3\2\2\2.\34\3\2\2\2.\35\3\2\2\2")
        buf.write(".\36\3\2\2\2.\37\3\2\2\2. \3\2\2\2.!\3\2\2\2.\"\3\2\2")
        buf.write("\2.#\3\2\2\2.$\3\2\2\2.%\3\2\2\2.\'\3\2\2\2.(\3\2\2\2")
        buf.write(".)\3\2\2\2.*\3\2\2\2.+\3\2\2\2.,\3\2\2\2.-\3\2\2\2/\t")
        buf.write("\3\2\2\2\60\61\t\5\2\2\61\13\3\2\2\2\3.")
        return buf.getvalue()


class LULUParser ( Parser ):

    grammarFileName = "LULU.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'=='", "'!='", "'<='", "'>='", "'>'", 
                     "'<'", "'~'", "'|'", "'&'", "'!'", "'||'", "'&&'", 
                     "'allocate'", "'bool'", "'break'", "'caseof'", "'const'", 
                     "'continue'", "'default'", "'destruct'", "'else'", 
                     "'false'", "'function'", "'float'", "'for'", "'if'", 
                     "'int'", "'nill'", "'true'", "'type'", "'while'", "'write'", 
                     "'private'", "'protected'", "'public'", "'read'", "'string'", 
                     "'super'", "'switch'", "'this'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID" ]

    RULE_ralation_op = 0
    RULE_bitwise_op = 1
    RULE_logic_op = 2
    RULE_keyword = 3
    RULE_arithmetic_op = 4

    ruleNames =  [ "ralation_op", "bitwise_op", "logic_op", "keyword", "arithmetic_op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    ID=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Ralation_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LULUParser.RULE_ralation_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRalation_op" ):
                listener.enterRalation_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRalation_op" ):
                listener.exitRalation_op(self)




    def ralation_op(self):

        localctx = LULUParser.Ralation_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ralation_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LULUParser.T__0) | (1 << LULUParser.T__1) | (1 << LULUParser.T__2) | (1 << LULUParser.T__3) | (1 << LULUParser.T__4) | (1 << LULUParser.T__5))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bitwise_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LULUParser.RULE_bitwise_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitwise_op" ):
                listener.enterBitwise_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitwise_op" ):
                listener.exitBitwise_op(self)




    def bitwise_op(self):

        localctx = LULUParser.Bitwise_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bitwise_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LULUParser.T__6) | (1 << LULUParser.T__7) | (1 << LULUParser.T__8))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LULUParser.RULE_logic_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_op" ):
                listener.enterLogic_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_op" ):
                listener.exitLogic_op(self)




    def logic_op(self):

        localctx = LULUParser.Logic_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_logic_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LULUParser.T__9) | (1 << LULUParser.T__10) | (1 << LULUParser.T__11))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LULUParser.RULE_keyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyword" ):
                listener.enterKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyword" ):
                listener.exitKeyword(self)




    def keyword(self):

        localctx = LULUParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_keyword)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LULUParser.T__12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(LULUParser.T__12)
                pass
            elif token in [LULUParser.T__13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.match(LULUParser.T__13)
                pass
            elif token in [LULUParser.T__14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 18
                self.match(LULUParser.T__14)
                pass
            elif token in [LULUParser.T__15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 19
                self.match(LULUParser.T__15)
                pass
            elif token in [LULUParser.T__16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 20
                self.match(LULUParser.T__16)
                pass
            elif token in [LULUParser.T__17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 21
                self.match(LULUParser.T__17)
                pass
            elif token in [LULUParser.T__18]:
                self.enterOuterAlt(localctx, 7)
                self.state = 22
                self.match(LULUParser.T__18)
                pass
            elif token in [LULUParser.T__19]:
                self.enterOuterAlt(localctx, 8)
                self.state = 23
                self.match(LULUParser.T__19)
                pass
            elif token in [LULUParser.T__20]:
                self.enterOuterAlt(localctx, 9)
                self.state = 24
                self.match(LULUParser.T__20)
                pass
            elif token in [LULUParser.T__21]:
                self.enterOuterAlt(localctx, 10)
                self.state = 25
                self.match(LULUParser.T__21)
                pass
            elif token in [LULUParser.T__22]:
                self.enterOuterAlt(localctx, 11)
                self.state = 26
                self.match(LULUParser.T__22)
                pass
            elif token in [LULUParser.T__23]:
                self.enterOuterAlt(localctx, 12)
                self.state = 27
                self.match(LULUParser.T__23)
                pass
            elif token in [LULUParser.T__24]:
                self.enterOuterAlt(localctx, 13)
                self.state = 28
                self.match(LULUParser.T__24)
                pass
            elif token in [LULUParser.T__25]:
                self.enterOuterAlt(localctx, 14)
                self.state = 29
                self.match(LULUParser.T__25)
                pass
            elif token in [LULUParser.T__26]:
                self.enterOuterAlt(localctx, 15)
                self.state = 30
                self.match(LULUParser.T__26)
                pass
            elif token in [LULUParser.T__27]:
                self.enterOuterAlt(localctx, 16)
                self.state = 31
                self.match(LULUParser.T__27)
                pass
            elif token in [LULUParser.T__28]:
                self.enterOuterAlt(localctx, 17)
                self.state = 32
                self.match(LULUParser.T__28)
                pass
            elif token in [LULUParser.T__29]:
                self.enterOuterAlt(localctx, 18)
                self.state = 33
                self.match(LULUParser.T__29)
                pass
            elif token in [LULUParser.T__30]:
                self.enterOuterAlt(localctx, 19)
                self.state = 34
                self.match(LULUParser.T__30)
                pass
            elif token in [LULUParser.T__31]:
                self.enterOuterAlt(localctx, 20)
                self.state = 35
                self.match(LULUParser.T__31)
                self.state = 36
                self.match(LULUParser.T__32)
                pass
            elif token in [LULUParser.T__33]:
                self.enterOuterAlt(localctx, 21)
                self.state = 37
                self.match(LULUParser.T__33)
                pass
            elif token in [LULUParser.T__34]:
                self.enterOuterAlt(localctx, 22)
                self.state = 38
                self.match(LULUParser.T__34)
                pass
            elif token in [LULUParser.T__35]:
                self.enterOuterAlt(localctx, 23)
                self.state = 39
                self.match(LULUParser.T__35)
                pass
            elif token in [LULUParser.T__36]:
                self.enterOuterAlt(localctx, 24)
                self.state = 40
                self.match(LULUParser.T__36)
                pass
            elif token in [LULUParser.T__37]:
                self.enterOuterAlt(localctx, 25)
                self.state = 41
                self.match(LULUParser.T__37)
                pass
            elif token in [LULUParser.T__38]:
                self.enterOuterAlt(localctx, 26)
                self.state = 42
                self.match(LULUParser.T__38)
                pass
            elif token in [LULUParser.T__39]:
                self.enterOuterAlt(localctx, 27)
                self.state = 43
                self.match(LULUParser.T__39)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LULUParser.RULE_arithmetic_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic_op" ):
                listener.enterArithmetic_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic_op" ):
                listener.exitArithmetic_op(self)




    def arithmetic_op(self):

        localctx = LULUParser.Arithmetic_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arithmetic_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LULUParser.T__40) | (1 << LULUParser.T__41) | (1 << LULUParser.T__42) | (1 << LULUParser.T__43) | (1 << LULUParser.T__44))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





