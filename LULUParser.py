# Generated from LULU.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("G\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\63\n\5\3\6\3\6\3")
        buf.write("\7\7\78\n\7\f\7\16\7;\13\7\3\7\7\7>\n\7\f\7\16\7A\13\7")
        buf.write("\5\7C\n\7\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\7\3\2\3\b")
        buf.write("\3\2\t\13\3\2\f\16\3\2+/\3\2\62\64\2\\\2\20\3\2\2\2\4")
        buf.write("\22\3\2\2\2\6\24\3\2\2\2\b\62\3\2\2\2\n\64\3\2\2\2\fB")
        buf.write("\3\2\2\2\16D\3\2\2\2\20\21\t\2\2\2\21\3\3\2\2\2\22\23")
        buf.write("\t\3\2\2\23\5\3\2\2\2\24\25\t\4\2\2\25\7\3\2\2\2\26\63")
        buf.write("\7\17\2\2\27\63\7\20\2\2\30\63\7\21\2\2\31\63\7\22\2\2")
        buf.write("\32\63\7\23\2\2\33\63\7\24\2\2\34\63\7\25\2\2\35\63\7")
        buf.write("\26\2\2\36\63\7\27\2\2\37\63\7\30\2\2 \63\7\31\2\2!\63")
        buf.write("\7\32\2\2\"\63\7\33\2\2#\63\7\34\2\2$\63\7\35\2\2%\63")
        buf.write("\7\36\2\2&\63\7\37\2\2\'\63\7 \2\2(\63\7!\2\2)*\7\"\2")
        buf.write("\2*\63\7#\2\2+\63\7$\2\2,\63\7%\2\2-\63\7&\2\2.\63\7\'")
        buf.write("\2\2/\63\7(\2\2\60\63\7)\2\2\61\63\7*\2\2\62\26\3\2\2")
        buf.write("\2\62\27\3\2\2\2\62\30\3\2\2\2\62\31\3\2\2\2\62\32\3\2")
        buf.write("\2\2\62\33\3\2\2\2\62\34\3\2\2\2\62\35\3\2\2\2\62\36\3")
        buf.write("\2\2\2\62\37\3\2\2\2\62 \3\2\2\2\62!\3\2\2\2\62\"\3\2")
        buf.write("\2\2\62#\3\2\2\2\62$\3\2\2\2\62%\3\2\2\2\62&\3\2\2\2\62")
        buf.write("\'\3\2\2\2\62(\3\2\2\2\62)\3\2\2\2\62+\3\2\2\2\62,\3\2")
        buf.write("\2\2\62-\3\2\2\2\62.\3\2\2\2\62/\3\2\2\2\62\60\3\2\2\2")
        buf.write("\62\61\3\2\2\2\63\t\3\2\2\2\64\65\t\5\2\2\65\13\3\2\2")
        buf.write("\2\668\7\60\2\2\67\66\3\2\2\28;\3\2\2\29\67\3\2\2\29:")
        buf.write("\3\2\2\2:C\3\2\2\2;9\3\2\2\2<>\7\61\2\2=<\3\2\2\2>A\3")
        buf.write("\2\2\2?=\3\2\2\2?@\3\2\2\2@C\3\2\2\2A?\3\2\2\2B9\3\2\2")
        buf.write("\2B?\3\2\2\2C\r\3\2\2\2DE\t\6\2\2E\17\3\2\2\2\6\629?B")
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
                     "'/'", "'%'", "' '", "'\t'", "'\r'", "'\n'", "'\n\r'" ]

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
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "Digits", "Id", 
                      "Hex", "Int_const" ]

    RULE_ralation_op = 0
    RULE_bitwise_op = 1
    RULE_logic_op = 2
    RULE_keyword = 3
    RULE_arithmetic_op = 4
    RULE_whitespace = 5
    RULE_newline = 6

    ruleNames =  [ "ralation_op", "bitwise_op", "logic_op", "keyword", "arithmetic_op", 
                   "whitespace", "newline" ]

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
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    Digits=51
    Id=52
    Hex=53
    Int_const=54

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
            self.state = 14
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
            self.state = 16
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
            self.state = 18
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
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LULUParser.T__12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(LULUParser.T__12)
                pass
            elif token in [LULUParser.T__13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(LULUParser.T__13)
                pass
            elif token in [LULUParser.T__14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.match(LULUParser.T__14)
                pass
            elif token in [LULUParser.T__15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 23
                self.match(LULUParser.T__15)
                pass
            elif token in [LULUParser.T__16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 24
                self.match(LULUParser.T__16)
                pass
            elif token in [LULUParser.T__17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 25
                self.match(LULUParser.T__17)
                pass
            elif token in [LULUParser.T__18]:
                self.enterOuterAlt(localctx, 7)
                self.state = 26
                self.match(LULUParser.T__18)
                pass
            elif token in [LULUParser.T__19]:
                self.enterOuterAlt(localctx, 8)
                self.state = 27
                self.match(LULUParser.T__19)
                pass
            elif token in [LULUParser.T__20]:
                self.enterOuterAlt(localctx, 9)
                self.state = 28
                self.match(LULUParser.T__20)
                pass
            elif token in [LULUParser.T__21]:
                self.enterOuterAlt(localctx, 10)
                self.state = 29
                self.match(LULUParser.T__21)
                pass
            elif token in [LULUParser.T__22]:
                self.enterOuterAlt(localctx, 11)
                self.state = 30
                self.match(LULUParser.T__22)
                pass
            elif token in [LULUParser.T__23]:
                self.enterOuterAlt(localctx, 12)
                self.state = 31
                self.match(LULUParser.T__23)
                pass
            elif token in [LULUParser.T__24]:
                self.enterOuterAlt(localctx, 13)
                self.state = 32
                self.match(LULUParser.T__24)
                pass
            elif token in [LULUParser.T__25]:
                self.enterOuterAlt(localctx, 14)
                self.state = 33
                self.match(LULUParser.T__25)
                pass
            elif token in [LULUParser.T__26]:
                self.enterOuterAlt(localctx, 15)
                self.state = 34
                self.match(LULUParser.T__26)
                pass
            elif token in [LULUParser.T__27]:
                self.enterOuterAlt(localctx, 16)
                self.state = 35
                self.match(LULUParser.T__27)
                pass
            elif token in [LULUParser.T__28]:
                self.enterOuterAlt(localctx, 17)
                self.state = 36
                self.match(LULUParser.T__28)
                pass
            elif token in [LULUParser.T__29]:
                self.enterOuterAlt(localctx, 18)
                self.state = 37
                self.match(LULUParser.T__29)
                pass
            elif token in [LULUParser.T__30]:
                self.enterOuterAlt(localctx, 19)
                self.state = 38
                self.match(LULUParser.T__30)
                pass
            elif token in [LULUParser.T__31]:
                self.enterOuterAlt(localctx, 20)
                self.state = 39
                self.match(LULUParser.T__31)
                self.state = 40
                self.match(LULUParser.T__32)
                pass
            elif token in [LULUParser.T__33]:
                self.enterOuterAlt(localctx, 21)
                self.state = 41
                self.match(LULUParser.T__33)
                pass
            elif token in [LULUParser.T__34]:
                self.enterOuterAlt(localctx, 22)
                self.state = 42
                self.match(LULUParser.T__34)
                pass
            elif token in [LULUParser.T__35]:
                self.enterOuterAlt(localctx, 23)
                self.state = 43
                self.match(LULUParser.T__35)
                pass
            elif token in [LULUParser.T__36]:
                self.enterOuterAlt(localctx, 24)
                self.state = 44
                self.match(LULUParser.T__36)
                pass
            elif token in [LULUParser.T__37]:
                self.enterOuterAlt(localctx, 25)
                self.state = 45
                self.match(LULUParser.T__37)
                pass
            elif token in [LULUParser.T__38]:
                self.enterOuterAlt(localctx, 26)
                self.state = 46
                self.match(LULUParser.T__38)
                pass
            elif token in [LULUParser.T__39]:
                self.enterOuterAlt(localctx, 27)
                self.state = 47
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
            self.state = 50
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


    class WhitespaceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LULUParser.RULE_whitespace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhitespace" ):
                listener.enterWhitespace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhitespace" ):
                listener.exitWhitespace(self)




    def whitespace(self):

        localctx = LULUParser.WhitespaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whitespace)
        self._la = 0 # Token type
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LULUParser.T__45:
                    self.state = 52
                    self.match(LULUParser.T__45)
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LULUParser.T__46:
                    self.state = 58
                    self.match(LULUParser.T__46)
                    self.state = 63
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LULUParser.RULE_newline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewline" ):
                listener.enterNewline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewline" ):
                listener.exitNewline(self)




    def newline(self):

        localctx = LULUParser.NewlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_newline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LULUParser.T__47) | (1 << LULUParser.T__48) | (1 << LULUParser.T__49))) != 0)):
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





