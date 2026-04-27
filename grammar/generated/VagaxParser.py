# Generated from grammar/VagaxParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,58,260,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,74,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,84,8,2,1,
        3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,99,8,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,8,1,8,5,8,123,8,8,10,8,12,8,126,9,8,1,8,1,8,1,9,1,
        9,1,9,1,9,3,9,134,8,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,5,10,143,8,
        10,10,10,12,10,146,9,10,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,3,12,161,8,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,205,
        8,12,10,12,12,12,208,9,12,1,13,1,13,1,13,3,13,213,8,13,1,13,1,13,
        1,14,1,14,1,14,5,14,220,8,14,10,14,12,14,223,9,14,1,15,1,15,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,3,16,244,8,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,
        1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,0,1,24,20,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,0,2,1,0,14,21,1,0,22,24,277,
        0,43,1,0,0,0,2,73,1,0,0,0,4,83,1,0,0,0,6,85,1,0,0,0,8,87,1,0,0,0,
        10,91,1,0,0,0,12,102,1,0,0,0,14,109,1,0,0,0,16,120,1,0,0,0,18,129,
        1,0,0,0,20,139,1,0,0,0,22,147,1,0,0,0,24,160,1,0,0,0,26,209,1,0,
        0,0,28,216,1,0,0,0,30,224,1,0,0,0,32,243,1,0,0,0,34,245,1,0,0,0,
        36,250,1,0,0,0,38,255,1,0,0,0,40,42,3,2,1,0,41,40,1,0,0,0,42,45,
        1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,
        46,47,5,0,0,1,47,1,1,0,0,0,48,49,3,4,2,0,49,50,5,35,0,0,50,74,1,
        0,0,0,51,52,3,8,4,0,52,53,5,35,0,0,53,74,1,0,0,0,54,55,3,34,17,0,
        55,56,5,35,0,0,56,74,1,0,0,0,57,58,3,36,18,0,58,59,5,35,0,0,59,74,
        1,0,0,0,60,61,3,38,19,0,61,62,5,35,0,0,62,74,1,0,0,0,63,74,3,10,
        5,0,64,74,3,12,6,0,65,74,3,14,7,0,66,74,3,18,9,0,67,68,3,22,11,0,
        68,69,5,35,0,0,69,74,1,0,0,0,70,71,3,24,12,0,71,72,5,35,0,0,72,74,
        1,0,0,0,73,48,1,0,0,0,73,51,1,0,0,0,73,54,1,0,0,0,73,57,1,0,0,0,
        73,60,1,0,0,0,73,63,1,0,0,0,73,64,1,0,0,0,73,65,1,0,0,0,73,66,1,
        0,0,0,73,67,1,0,0,0,73,70,1,0,0,0,74,3,1,0,0,0,75,76,3,6,3,0,76,
        77,5,25,0,0,77,78,5,32,0,0,78,79,3,24,12,0,79,84,1,0,0,0,80,81,3,
        6,3,0,81,82,5,25,0,0,82,84,1,0,0,0,83,75,1,0,0,0,83,80,1,0,0,0,84,
        5,1,0,0,0,85,86,7,0,0,0,86,7,1,0,0,0,87,88,5,25,0,0,88,89,5,32,0,
        0,89,90,3,24,12,0,90,9,1,0,0,0,91,92,5,1,0,0,92,93,5,37,0,0,93,94,
        3,24,12,0,94,95,5,38,0,0,95,98,3,16,8,0,96,97,5,2,0,0,97,99,3,16,
        8,0,98,96,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,101,5,11,0,0,
        101,11,1,0,0,0,102,103,5,3,0,0,103,104,5,37,0,0,104,105,3,24,12,
        0,105,106,5,38,0,0,106,107,3,16,8,0,107,108,5,11,0,0,108,13,1,0,
        0,0,109,110,5,4,0,0,110,111,5,37,0,0,111,112,3,8,4,0,112,113,5,35,
        0,0,113,114,3,24,12,0,114,115,5,35,0,0,115,116,3,8,4,0,116,117,5,
        38,0,0,117,118,3,16,8,0,118,119,5,11,0,0,119,15,1,0,0,0,120,124,
        5,41,0,0,121,123,3,2,1,0,122,121,1,0,0,0,123,126,1,0,0,0,124,122,
        1,0,0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,128,
        5,42,0,0,128,17,1,0,0,0,129,130,5,6,0,0,130,131,5,25,0,0,131,133,
        5,37,0,0,132,134,3,20,10,0,133,132,1,0,0,0,133,134,1,0,0,0,134,135,
        1,0,0,0,135,136,5,38,0,0,136,137,3,16,8,0,137,138,5,11,0,0,138,19,
        1,0,0,0,139,144,5,25,0,0,140,141,5,34,0,0,141,143,5,25,0,0,142,140,
        1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,21,1,
        0,0,0,146,144,1,0,0,0,147,148,5,7,0,0,148,149,3,24,12,0,149,23,1,
        0,0,0,150,151,6,12,-1,0,151,152,5,51,0,0,152,161,3,24,12,5,153,154,
        5,37,0,0,154,155,3,24,12,0,155,156,5,38,0,0,156,161,1,0,0,0,157,
        161,3,26,13,0,158,161,3,30,15,0,159,161,5,25,0,0,160,150,1,0,0,0,
        160,153,1,0,0,0,160,157,1,0,0,0,160,158,1,0,0,0,160,159,1,0,0,0,
        161,206,1,0,0,0,162,163,10,19,0,0,163,164,5,31,0,0,164,205,3,24,
        12,20,165,166,10,18,0,0,166,167,5,28,0,0,167,205,3,24,12,19,168,
        169,10,17,0,0,169,170,5,29,0,0,170,205,3,24,12,18,171,172,10,16,
        0,0,172,173,5,30,0,0,173,205,3,24,12,17,174,175,10,15,0,0,175,176,
        5,26,0,0,176,205,3,24,12,16,177,178,10,14,0,0,178,179,5,27,0,0,179,
        205,3,24,12,15,180,181,10,13,0,0,181,182,5,43,0,0,182,205,3,24,12,
        14,183,184,10,12,0,0,184,185,5,44,0,0,185,205,3,24,12,13,186,187,
        10,11,0,0,187,188,5,47,0,0,188,205,3,24,12,12,189,190,10,10,0,0,
        190,191,5,48,0,0,191,205,3,24,12,11,192,193,10,9,0,0,193,194,5,45,
        0,0,194,205,3,24,12,10,195,196,10,8,0,0,196,197,5,46,0,0,197,205,
        3,24,12,9,198,199,10,7,0,0,199,200,5,50,0,0,200,205,3,24,12,8,201,
        202,10,6,0,0,202,203,5,49,0,0,203,205,3,24,12,7,204,162,1,0,0,0,
        204,165,1,0,0,0,204,168,1,0,0,0,204,171,1,0,0,0,204,174,1,0,0,0,
        204,177,1,0,0,0,204,180,1,0,0,0,204,183,1,0,0,0,204,186,1,0,0,0,
        204,189,1,0,0,0,204,192,1,0,0,0,204,195,1,0,0,0,204,198,1,0,0,0,
        204,201,1,0,0,0,205,208,1,0,0,0,206,204,1,0,0,0,206,207,1,0,0,0,
        207,25,1,0,0,0,208,206,1,0,0,0,209,210,5,25,0,0,210,212,5,37,0,0,
        211,213,3,28,14,0,212,211,1,0,0,0,212,213,1,0,0,0,213,214,1,0,0,
        0,214,215,5,38,0,0,215,27,1,0,0,0,216,221,3,24,12,0,217,218,5,34,
        0,0,218,220,3,24,12,0,219,217,1,0,0,0,220,223,1,0,0,0,221,219,1,
        0,0,0,221,222,1,0,0,0,222,29,1,0,0,0,223,221,1,0,0,0,224,225,7,1,
        0,0,225,31,1,0,0,0,226,227,5,52,0,0,227,228,5,37,0,0,228,229,3,24,
        12,0,229,230,5,34,0,0,230,231,3,24,12,0,231,232,5,38,0,0,232,233,
        5,35,0,0,233,244,1,0,0,0,234,235,5,54,0,0,235,236,5,37,0,0,236,237,
        5,24,0,0,237,238,5,38,0,0,238,244,5,35,0,0,239,240,5,53,0,0,240,
        241,5,37,0,0,241,242,5,38,0,0,242,244,5,35,0,0,243,226,1,0,0,0,243,
        234,1,0,0,0,243,239,1,0,0,0,244,33,1,0,0,0,245,246,5,8,0,0,246,247,
        5,25,0,0,247,248,5,32,0,0,248,249,3,24,12,0,249,35,1,0,0,0,250,251,
        5,9,0,0,251,252,5,37,0,0,252,253,5,25,0,0,253,254,5,38,0,0,254,37,
        1,0,0,0,255,256,5,10,0,0,256,257,5,37,0,0,257,258,5,38,0,0,258,39,
        1,0,0,0,13,43,73,83,98,124,133,144,160,204,206,212,221,243
    ]

class VagaxParser ( Parser ):

    grammarFileName = "VagaxParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ifvag'", "'elsevag'", "'whilevag'", 
                     "'forvag'", "'invag'", "'functionvag'", "'returnvag'", 
                     "'allocvag'", "'freevag'", "'memvag'", "'endvag'", 
                     "'importvag'", "'asvag'", "'intvag'", "'floatvag'", 
                     "'boolvag'", "'stringvag'", "'listvag'", "'diccvag'", 
                     "'matrixvag'", "'dataframevag'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'^'", "'='", "':'", "','", "';'", "'.'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "'=='", "'!='", 
                     "'<='", "'>='", "'<'", "'>'", "'||'", "'&&'", "'!'", 
                     "'plotvag'", "'showvag'", "'titlevag'", "'xlabelvag'", 
                     "'ylabelvag'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "WHILE", "FOR", "IN", "FUNCTION", 
                      "RETURN", "ALLOCVAG", "FREEVAG", "MEMVAG", "END", 
                      "IMPORT", "AS", "INT", "FLOAT", "BOOL_T", "STRING_T", 
                      "LIST", "DICC", "MATRIX", "DATAFRAME", "BOOL_LIT", 
                      "NUMBER", "STRING", "ID", "PLUS", "MINUS", "MUL", 
                      "DIV", "MOD", "POW", "ASSIGN", "COLON", "COMMA", "SEMI", 
                      "DOT", "LPAREN", "RPAREN", "LBRACK", "RBRACK", "LBRACE", 
                      "RBRACE", "EQ", "NEQ", "LE", "GE", "LT", "GT", "OR", 
                      "AND", "NOT", "PLOTVAG", "SHOWVAG", "TITLEVAG", "XLABELVAG", 
                      "YLABELVAG", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_varDecl = 2
    RULE_type = 3
    RULE_assignment = 4
    RULE_ifStatement = 5
    RULE_whileStatement = 6
    RULE_forStatement = 7
    RULE_block = 8
    RULE_functionDecl = 9
    RULE_paramList = 10
    RULE_returnStmt = 11
    RULE_expr = 12
    RULE_functionCall = 13
    RULE_argList = 14
    RULE_literal = 15
    RULE_instruccionGrafica = 16
    RULE_allocStmt = 17
    RULE_freeStmt = 18
    RULE_memStmt = 19

    ruleNames =  [ "program", "statement", "varDecl", "type", "assignment", 
                   "ifStatement", "whileStatement", "forStatement", "block", 
                   "functionDecl", "paramList", "returnStmt", "expr", "functionCall", 
                   "argList", "literal", "instruccionGrafica", "allocStmt", 
                   "freeStmt", "memStmt" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    WHILE=3
    FOR=4
    IN=5
    FUNCTION=6
    RETURN=7
    ALLOCVAG=8
    FREEVAG=9
    MEMVAG=10
    END=11
    IMPORT=12
    AS=13
    INT=14
    FLOAT=15
    BOOL_T=16
    STRING_T=17
    LIST=18
    DICC=19
    MATRIX=20
    DATAFRAME=21
    BOOL_LIT=22
    NUMBER=23
    STRING=24
    ID=25
    PLUS=26
    MINUS=27
    MUL=28
    DIV=29
    MOD=30
    POW=31
    ASSIGN=32
    COLON=33
    COMMA=34
    SEMI=35
    DOT=36
    LPAREN=37
    RPAREN=38
    LBRACK=39
    RBRACK=40
    LBRACE=41
    RBRACE=42
    EQ=43
    NEQ=44
    LE=45
    GE=46
    LT=47
    GT=48
    OR=49
    AND=50
    NOT=51
    PLOTVAG=52
    SHOWVAG=53
    TITLEVAG=54
    XLABELVAG=55
    YLABELVAG=56
    COMMENT=57
    WS=58

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(VagaxParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VagaxParser.StatementContext)
            else:
                return self.getTypedRuleContext(VagaxParser.StatementContext,i)


        def getRuleIndex(self):
            return VagaxParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = VagaxParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2251937319733210) != 0):
                self.state = 40
                self.statement()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(VagaxParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(VagaxParser.VarDeclContext,0)


        def SEMI(self):
            return self.getToken(VagaxParser.SEMI, 0)

        def assignment(self):
            return self.getTypedRuleContext(VagaxParser.AssignmentContext,0)


        def allocStmt(self):
            return self.getTypedRuleContext(VagaxParser.AllocStmtContext,0)


        def freeStmt(self):
            return self.getTypedRuleContext(VagaxParser.FreeStmtContext,0)


        def memStmt(self):
            return self.getTypedRuleContext(VagaxParser.MemStmtContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(VagaxParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(VagaxParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(VagaxParser.ForStatementContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(VagaxParser.FunctionDeclContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(VagaxParser.ReturnStmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(VagaxParser.ExprContext,0)


        def getRuleIndex(self):
            return VagaxParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = VagaxParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.varDecl()
                self.state = 49
                self.match(VagaxParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.assignment()
                self.state = 52
                self.match(VagaxParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.allocStmt()
                self.state = 55
                self.match(VagaxParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.freeStmt()
                self.state = 58
                self.match(VagaxParser.SEMI)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.memStmt()
                self.state = 61
                self.match(VagaxParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 63
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 64
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 65
                self.forStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 66
                self.functionDecl()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 67
                self.returnStmt()
                self.state = 68
                self.match(VagaxParser.SEMI)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 70
                self.expr(0)
                self.state = 71
                self.match(VagaxParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(VagaxParser.TypeContext,0)


        def ID(self):
            return self.getToken(VagaxParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(VagaxParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(VagaxParser.ExprContext,0)


        def getRuleIndex(self):
            return VagaxParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = VagaxParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDecl)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.type_()
                self.state = 76
                self.match(VagaxParser.ID)
                self.state = 77
                self.match(VagaxParser.ASSIGN)
                self.state = 78
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.type_()
                self.state = 81
                self.match(VagaxParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(VagaxParser.INT, 0)

        def FLOAT(self):
            return self.getToken(VagaxParser.FLOAT, 0)

        def BOOL_T(self):
            return self.getToken(VagaxParser.BOOL_T, 0)

        def STRING_T(self):
            return self.getToken(VagaxParser.STRING_T, 0)

        def LIST(self):
            return self.getToken(VagaxParser.LIST, 0)

        def MATRIX(self):
            return self.getToken(VagaxParser.MATRIX, 0)

        def DICC(self):
            return self.getToken(VagaxParser.DICC, 0)

        def DATAFRAME(self):
            return self.getToken(VagaxParser.DATAFRAME, 0)

        def getRuleIndex(self):
            return VagaxParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = VagaxParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4177920) != 0)):
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VagaxParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(VagaxParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(VagaxParser.ExprContext,0)


        def getRuleIndex(self):
            return VagaxParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = VagaxParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(VagaxParser.ID)
            self.state = 88
            self.match(VagaxParser.ASSIGN)
            self.state = 89
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(VagaxParser.IF, 0)

        def LPAREN(self):
            return self.getToken(VagaxParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(VagaxParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(VagaxParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VagaxParser.BlockContext)
            else:
                return self.getTypedRuleContext(VagaxParser.BlockContext,i)


        def END(self):
            return self.getToken(VagaxParser.END, 0)

        def ELSE(self):
            return self.getToken(VagaxParser.ELSE, 0)

        def getRuleIndex(self):
            return VagaxParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = VagaxParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(VagaxParser.IF)
            self.state = 92
            self.match(VagaxParser.LPAREN)
            self.state = 93
            self.expr(0)
            self.state = 94
            self.match(VagaxParser.RPAREN)
            self.state = 95
            self.block()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 96
                self.match(VagaxParser.ELSE)
                self.state = 97
                self.block()


            self.state = 100
            self.match(VagaxParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(VagaxParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(VagaxParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(VagaxParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(VagaxParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(VagaxParser.BlockContext,0)


        def END(self):
            return self.getToken(VagaxParser.END, 0)

        def getRuleIndex(self):
            return VagaxParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = VagaxParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(VagaxParser.WHILE)
            self.state = 103
            self.match(VagaxParser.LPAREN)
            self.state = 104
            self.expr(0)
            self.state = 105
            self.match(VagaxParser.RPAREN)
            self.state = 106
            self.block()
            self.state = 107
            self.match(VagaxParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(VagaxParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(VagaxParser.LPAREN, 0)

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VagaxParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(VagaxParser.AssignmentContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(VagaxParser.SEMI)
            else:
                return self.getToken(VagaxParser.SEMI, i)

        def expr(self):
            return self.getTypedRuleContext(VagaxParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(VagaxParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(VagaxParser.BlockContext,0)


        def END(self):
            return self.getToken(VagaxParser.END, 0)

        def getRuleIndex(self):
            return VagaxParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = VagaxParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(VagaxParser.FOR)
            self.state = 110
            self.match(VagaxParser.LPAREN)
            self.state = 111
            self.assignment()
            self.state = 112
            self.match(VagaxParser.SEMI)
            self.state = 113
            self.expr(0)
            self.state = 114
            self.match(VagaxParser.SEMI)
            self.state = 115
            self.assignment()
            self.state = 116
            self.match(VagaxParser.RPAREN)
            self.state = 117
            self.block()
            self.state = 118
            self.match(VagaxParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(VagaxParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(VagaxParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VagaxParser.StatementContext)
            else:
                return self.getTypedRuleContext(VagaxParser.StatementContext,i)


        def getRuleIndex(self):
            return VagaxParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = VagaxParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(VagaxParser.LBRACE)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2251937319733210) != 0):
                self.state = 121
                self.statement()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self.match(VagaxParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(VagaxParser.FUNCTION, 0)

        def ID(self):
            return self.getToken(VagaxParser.ID, 0)

        def LPAREN(self):
            return self.getToken(VagaxParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(VagaxParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(VagaxParser.BlockContext,0)


        def END(self):
            return self.getToken(VagaxParser.END, 0)

        def paramList(self):
            return self.getTypedRuleContext(VagaxParser.ParamListContext,0)


        def getRuleIndex(self):
            return VagaxParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = VagaxParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(VagaxParser.FUNCTION)
            self.state = 130
            self.match(VagaxParser.ID)
            self.state = 131
            self.match(VagaxParser.LPAREN)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 132
                self.paramList()


            self.state = 135
            self.match(VagaxParser.RPAREN)
            self.state = 136
            self.block()
            self.state = 137
            self.match(VagaxParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(VagaxParser.ID)
            else:
                return self.getToken(VagaxParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(VagaxParser.COMMA)
            else:
                return self.getToken(VagaxParser.COMMA, i)

        def getRuleIndex(self):
            return VagaxParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = VagaxParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(VagaxParser.ID)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 140
                self.match(VagaxParser.COMMA)
                self.state = 141
                self.match(VagaxParser.ID)
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(VagaxParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(VagaxParser.ExprContext,0)


        def getRuleIndex(self):
            return VagaxParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = VagaxParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(VagaxParser.RETURN)
            self.state = 148
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(VagaxParser.NOT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VagaxParser.ExprContext)
            else:
                return self.getTypedRuleContext(VagaxParser.ExprContext,i)


        def LPAREN(self):
            return self.getToken(VagaxParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(VagaxParser.RPAREN, 0)

        def functionCall(self):
            return self.getTypedRuleContext(VagaxParser.FunctionCallContext,0)


        def literal(self):
            return self.getTypedRuleContext(VagaxParser.LiteralContext,0)


        def ID(self):
            return self.getToken(VagaxParser.ID, 0)

        def POW(self):
            return self.getToken(VagaxParser.POW, 0)

        def MUL(self):
            return self.getToken(VagaxParser.MUL, 0)

        def DIV(self):
            return self.getToken(VagaxParser.DIV, 0)

        def MOD(self):
            return self.getToken(VagaxParser.MOD, 0)

        def PLUS(self):
            return self.getToken(VagaxParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(VagaxParser.MINUS, 0)

        def EQ(self):
            return self.getToken(VagaxParser.EQ, 0)

        def NEQ(self):
            return self.getToken(VagaxParser.NEQ, 0)

        def LT(self):
            return self.getToken(VagaxParser.LT, 0)

        def GT(self):
            return self.getToken(VagaxParser.GT, 0)

        def LE(self):
            return self.getToken(VagaxParser.LE, 0)

        def GE(self):
            return self.getToken(VagaxParser.GE, 0)

        def AND(self):
            return self.getToken(VagaxParser.AND, 0)

        def OR(self):
            return self.getToken(VagaxParser.OR, 0)

        def getRuleIndex(self):
            return VagaxParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = VagaxParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 151
                self.match(VagaxParser.NOT)
                self.state = 152
                self.expr(5)
                pass

            elif la_ == 2:
                self.state = 153
                self.match(VagaxParser.LPAREN)
                self.state = 154
                self.expr(0)
                self.state = 155
                self.match(VagaxParser.RPAREN)
                pass

            elif la_ == 3:
                self.state = 157
                self.functionCall()
                pass

            elif la_ == 4:
                self.state = 158
                self.literal()
                pass

            elif la_ == 5:
                self.state = 159
                self.match(VagaxParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 204
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = VagaxParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 162
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 163
                        self.match(VagaxParser.POW)
                        self.state = 164
                        self.expr(20)
                        pass

                    elif la_ == 2:
                        localctx = VagaxParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 165
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 166
                        self.match(VagaxParser.MUL)
                        self.state = 167
                        self.expr(19)
                        pass

                    elif la_ == 3:
                        localctx = VagaxParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 168
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 169
                        self.match(VagaxParser.DIV)
                        self.state = 170
                        self.expr(18)
                        pass

                    elif la_ == 4:
                        localctx = VagaxParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 171
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 172
                        self.match(VagaxParser.MOD)
                        self.state = 173
                        self.expr(17)
                        pass

                    elif la_ == 5:
                        localctx = VagaxParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 174
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 175
                        self.match(VagaxParser.PLUS)
                        self.state = 176
                        self.expr(16)
                        pass

                    elif la_ == 6:
                        localctx = VagaxParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 177
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 178
                        self.match(VagaxParser.MINUS)
                        self.state = 179
                        self.expr(15)
                        pass

                    elif la_ == 7:
                        localctx = VagaxParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 180
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 181
                        self.match(VagaxParser.EQ)
                        self.state = 182
                        self.expr(14)
                        pass

                    elif la_ == 8:
                        localctx = VagaxParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 183
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 184
                        self.match(VagaxParser.NEQ)
                        self.state = 185
                        self.expr(13)
                        pass

                    elif la_ == 9:
                        localctx = VagaxParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 186
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 187
                        self.match(VagaxParser.LT)
                        self.state = 188
                        self.expr(12)
                        pass

                    elif la_ == 10:
                        localctx = VagaxParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 189
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 190
                        self.match(VagaxParser.GT)
                        self.state = 191
                        self.expr(11)
                        pass

                    elif la_ == 11:
                        localctx = VagaxParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 192
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 193
                        self.match(VagaxParser.LE)
                        self.state = 194
                        self.expr(10)
                        pass

                    elif la_ == 12:
                        localctx = VagaxParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 195
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 196
                        self.match(VagaxParser.GE)
                        self.state = 197
                        self.expr(9)
                        pass

                    elif la_ == 13:
                        localctx = VagaxParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 198
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 199
                        self.match(VagaxParser.AND)
                        self.state = 200
                        self.expr(8)
                        pass

                    elif la_ == 14:
                        localctx = VagaxParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 201
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 202
                        self.match(VagaxParser.OR)
                        self.state = 203
                        self.expr(7)
                        pass

             
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VagaxParser.ID, 0)

        def LPAREN(self):
            return self.getToken(VagaxParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(VagaxParser.RPAREN, 0)

        def argList(self):
            return self.getTypedRuleContext(VagaxParser.ArgListContext,0)


        def getRuleIndex(self):
            return VagaxParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = VagaxParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(VagaxParser.ID)
            self.state = 210
            self.match(VagaxParser.LPAREN)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2251937315553280) != 0):
                self.state = 211
                self.argList()


            self.state = 214
            self.match(VagaxParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VagaxParser.ExprContext)
            else:
                return self.getTypedRuleContext(VagaxParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(VagaxParser.COMMA)
            else:
                return self.getToken(VagaxParser.COMMA, i)

        def getRuleIndex(self):
            return VagaxParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = VagaxParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.expr(0)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 217
                self.match(VagaxParser.COMMA)
                self.state = 218
                self.expr(0)
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(VagaxParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(VagaxParser.STRING, 0)

        def BOOL_LIT(self):
            return self.getToken(VagaxParser.BOOL_LIT, 0)

        def getRuleIndex(self):
            return VagaxParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = VagaxParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
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


    class InstruccionGraficaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLOTVAG(self):
            return self.getToken(VagaxParser.PLOTVAG, 0)

        def LPAREN(self):
            return self.getToken(VagaxParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VagaxParser.ExprContext)
            else:
                return self.getTypedRuleContext(VagaxParser.ExprContext,i)


        def COMMA(self):
            return self.getToken(VagaxParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(VagaxParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(VagaxParser.SEMI, 0)

        def TITLEVAG(self):
            return self.getToken(VagaxParser.TITLEVAG, 0)

        def STRING(self):
            return self.getToken(VagaxParser.STRING, 0)

        def SHOWVAG(self):
            return self.getToken(VagaxParser.SHOWVAG, 0)

        def getRuleIndex(self):
            return VagaxParser.RULE_instruccionGrafica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccionGrafica" ):
                listener.enterInstruccionGrafica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccionGrafica" ):
                listener.exitInstruccionGrafica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionGrafica" ):
                return visitor.visitInstruccionGrafica(self)
            else:
                return visitor.visitChildren(self)




    def instruccionGrafica(self):

        localctx = VagaxParser.InstruccionGraficaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_instruccionGrafica)
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(VagaxParser.PLOTVAG)
                self.state = 227
                self.match(VagaxParser.LPAREN)
                self.state = 228
                self.expr(0)
                self.state = 229
                self.match(VagaxParser.COMMA)
                self.state = 230
                self.expr(0)
                self.state = 231
                self.match(VagaxParser.RPAREN)
                self.state = 232
                self.match(VagaxParser.SEMI)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(VagaxParser.TITLEVAG)
                self.state = 235
                self.match(VagaxParser.LPAREN)
                self.state = 236
                self.match(VagaxParser.STRING)
                self.state = 237
                self.match(VagaxParser.RPAREN)
                self.state = 238
                self.match(VagaxParser.SEMI)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.match(VagaxParser.SHOWVAG)
                self.state = 240
                self.match(VagaxParser.LPAREN)
                self.state = 241
                self.match(VagaxParser.RPAREN)
                self.state = 242
                self.match(VagaxParser.SEMI)
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


    class AllocStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALLOCVAG(self):
            return self.getToken(VagaxParser.ALLOCVAG, 0)

        def ID(self):
            return self.getToken(VagaxParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(VagaxParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(VagaxParser.ExprContext,0)


        def getRuleIndex(self):
            return VagaxParser.RULE_allocStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllocStmt" ):
                listener.enterAllocStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllocStmt" ):
                listener.exitAllocStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllocStmt" ):
                return visitor.visitAllocStmt(self)
            else:
                return visitor.visitChildren(self)




    def allocStmt(self):

        localctx = VagaxParser.AllocStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_allocStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(VagaxParser.ALLOCVAG)
            self.state = 246
            self.match(VagaxParser.ID)
            self.state = 247
            self.match(VagaxParser.ASSIGN)
            self.state = 248
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FreeStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FREEVAG(self):
            return self.getToken(VagaxParser.FREEVAG, 0)

        def LPAREN(self):
            return self.getToken(VagaxParser.LPAREN, 0)

        def ID(self):
            return self.getToken(VagaxParser.ID, 0)

        def RPAREN(self):
            return self.getToken(VagaxParser.RPAREN, 0)

        def getRuleIndex(self):
            return VagaxParser.RULE_freeStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFreeStmt" ):
                listener.enterFreeStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFreeStmt" ):
                listener.exitFreeStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFreeStmt" ):
                return visitor.visitFreeStmt(self)
            else:
                return visitor.visitChildren(self)




    def freeStmt(self):

        localctx = VagaxParser.FreeStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_freeStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(VagaxParser.FREEVAG)
            self.state = 251
            self.match(VagaxParser.LPAREN)
            self.state = 252
            self.match(VagaxParser.ID)
            self.state = 253
            self.match(VagaxParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MEMVAG(self):
            return self.getToken(VagaxParser.MEMVAG, 0)

        def LPAREN(self):
            return self.getToken(VagaxParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(VagaxParser.RPAREN, 0)

        def getRuleIndex(self):
            return VagaxParser.RULE_memStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemStmt" ):
                listener.enterMemStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemStmt" ):
                listener.exitMemStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemStmt" ):
                return visitor.visitMemStmt(self)
            else:
                return visitor.visitChildren(self)




    def memStmt(self):

        localctx = VagaxParser.MemStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_memStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(VagaxParser.MEMVAG)
            self.state = 256
            self.match(VagaxParser.LPAREN)
            self.state = 257
            self.match(VagaxParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 6)
         




