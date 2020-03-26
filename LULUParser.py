# Generated from LULU.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3$")
        buf.write("\'\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\5\2#\n\2\3\3\3\3\3\3\2\2\4\2\4")
        buf.write("\2\3\3\2\37#\2>\2\"\3\2\2\2\4$\3\2\2\2\6#\7\3\2\2\7#\7")
        buf.write("\4\2\2\b#\7\5\2\2\t#\7\6\2\2\n#\7\7\2\2\13#\7\b\2\2\f")
        buf.write("#\7\t\2\2\r#\7\n\2\2\16#\7\13\2\2\17#\7\f\2\2\20#\7\r")
        buf.write("\2\2\21#\7\16\2\2\22#\7\17\2\2\23#\7\20\2\2\24#\7\21\2")
        buf.write("\2\25#\7\22\2\2\26#\7\23\2\2\27#\7\24\2\2\30#\7\25\2\2")
        buf.write("\31\32\7\26\2\2\32#\7\27\2\2\33#\7\30\2\2\34#\7\31\2\2")
        buf.write("\35#\7\32\2\2\36#\7\33\2\2\37#\7\34\2\2 #\7\35\2\2!#\7")
        buf.write("\36\2\2\"\6\3\2\2\2\"\7\3\2\2\2\"\b\3\2\2\2\"\t\3\2\2")
        buf.write("\2\"\n\3\2\2\2\"\13\3\2\2\2\"\f\3\2\2\2\"\r\3\2\2\2\"")
        buf.write("\16\3\2\2\2\"\17\3\2\2\2\"\20\3\2\2\2\"\21\3\2\2\2\"\22")
        buf.write("\3\2\2\2\"\23\3\2\2\2\"\24\3\2\2\2\"\25\3\2\2\2\"\26\3")
        buf.write("\2\2\2\"\27\3\2\2\2\"\30\3\2\2\2\"\31\3\2\2\2\"\33\3\2")
        buf.write("\2\2\"\34\3\2\2\2\"\35\3\2\2\2\"\36\3\2\2\2\"\37\3\2\2")
        buf.write("\2\" \3\2\2\2\"!\3\2\2\2#\3\3\2\2\2$%\t\2\2\2%\5\3\2\2")
        buf.write("\2\3\"")
        return buf.getvalue()


class LULUParser ( Parser ):

    grammarFileName = "LULU.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'allocate'", "'bool'", "'break'", "'caseof'", 
                     "'const'", "'continue'", "'default'", "'destruct'", 
                     "'else'", "'false'", "'function'", "'float'", "'for'", 
                     "'if'", "'int'", "'nill'", "'true'", "'type'", "'while'", 
                     "'write'", "'private'", "'protected'", "'public'", 
                     "'read'", "'string'", "'super'", "'switch'", "'this'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID" ]

    RULE_keyword = 0
    RULE_arithmetic_op = 1

    ruleNames =  [ "keyword", "arithmetic_op" ]

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
    ID=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




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
        self.enterRule(localctx, 0, self.RULE_keyword)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LULUParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.match(LULUParser.T__0)
                pass
            elif token in [LULUParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 5
                self.match(LULUParser.T__1)
                pass
            elif token in [LULUParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 6
                self.match(LULUParser.T__2)
                pass
            elif token in [LULUParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 7
                self.match(LULUParser.T__3)
                pass
            elif token in [LULUParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 8
                self.match(LULUParser.T__4)
                pass
            elif token in [LULUParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 9
                self.match(LULUParser.T__5)
                pass
            elif token in [LULUParser.T__6]:
                self.enterOuterAlt(localctx, 7)
                self.state = 10
                self.match(LULUParser.T__6)
                pass
            elif token in [LULUParser.T__7]:
                self.enterOuterAlt(localctx, 8)
                self.state = 11
                self.match(LULUParser.T__7)
                pass
            elif token in [LULUParser.T__8]:
                self.enterOuterAlt(localctx, 9)
                self.state = 12
                self.match(LULUParser.T__8)
                pass
            elif token in [LULUParser.T__9]:
                self.enterOuterAlt(localctx, 10)
                self.state = 13
                self.match(LULUParser.T__9)
                pass
            elif token in [LULUParser.T__10]:
                self.enterOuterAlt(localctx, 11)
                self.state = 14
                self.match(LULUParser.T__10)
                pass
            elif token in [LULUParser.T__11]:
                self.enterOuterAlt(localctx, 12)
                self.state = 15
                self.match(LULUParser.T__11)
                pass
            elif token in [LULUParser.T__12]:
                self.enterOuterAlt(localctx, 13)
                self.state = 16
                self.match(LULUParser.T__12)
                pass
            elif token in [LULUParser.T__13]:
                self.enterOuterAlt(localctx, 14)
                self.state = 17
                self.match(LULUParser.T__13)
                pass
            elif token in [LULUParser.T__14]:
                self.enterOuterAlt(localctx, 15)
                self.state = 18
                self.match(LULUParser.T__14)
                pass
            elif token in [LULUParser.T__15]:
                self.enterOuterAlt(localctx, 16)
                self.state = 19
                self.match(LULUParser.T__15)
                pass
            elif token in [LULUParser.T__16]:
                self.enterOuterAlt(localctx, 17)
                self.state = 20
                self.match(LULUParser.T__16)
                pass
            elif token in [LULUParser.T__17]:
                self.enterOuterAlt(localctx, 18)
                self.state = 21
                self.match(LULUParser.T__17)
                pass
            elif token in [LULUParser.T__18]:
                self.enterOuterAlt(localctx, 19)
                self.state = 22
                self.match(LULUParser.T__18)
                pass
            elif token in [LULUParser.T__19]:
                self.enterOuterAlt(localctx, 20)
                self.state = 23
                self.match(LULUParser.T__19)
                self.state = 24
                self.match(LULUParser.T__20)
                pass
            elif token in [LULUParser.T__21]:
                self.enterOuterAlt(localctx, 21)
                self.state = 25
                self.match(LULUParser.T__21)
                pass
            elif token in [LULUParser.T__22]:
                self.enterOuterAlt(localctx, 22)
                self.state = 26
                self.match(LULUParser.T__22)
                pass
            elif token in [LULUParser.T__23]:
                self.enterOuterAlt(localctx, 23)
                self.state = 27
                self.match(LULUParser.T__23)
                pass
            elif token in [LULUParser.T__24]:
                self.enterOuterAlt(localctx, 24)
                self.state = 28
                self.match(LULUParser.T__24)
                pass
            elif token in [LULUParser.T__25]:
                self.enterOuterAlt(localctx, 25)
                self.state = 29
                self.match(LULUParser.T__25)
                pass
            elif token in [LULUParser.T__26]:
                self.enterOuterAlt(localctx, 26)
                self.state = 30
                self.match(LULUParser.T__26)
                pass
            elif token in [LULUParser.T__27]:
                self.enterOuterAlt(localctx, 27)
                self.state = 31
                self.match(LULUParser.T__27)
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
        self.enterRule(localctx, 2, self.RULE_arithmetic_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LULUParser.T__28) | (1 << LULUParser.T__29) | (1 << LULUParser.T__30) | (1 << LULUParser.T__31) | (1 << LULUParser.T__32))) != 0)):
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





