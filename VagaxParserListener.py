# Generated from grammar/VagaxParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .VagaxParser import VagaxParser
else:
    from VagaxParser import VagaxParser

# This class defines a complete listener for a parse tree produced by VagaxParser.
class VagaxParserListener(ParseTreeListener):

    # Enter a parse tree produced by VagaxParser#program.
    def enterProgram(self, ctx:VagaxParser.ProgramContext):
        pass

    # Exit a parse tree produced by VagaxParser#program.
    def exitProgram(self, ctx:VagaxParser.ProgramContext):
        pass


    # Enter a parse tree produced by VagaxParser#statement.
    def enterStatement(self, ctx:VagaxParser.StatementContext):
        pass

    # Exit a parse tree produced by VagaxParser#statement.
    def exitStatement(self, ctx:VagaxParser.StatementContext):
        pass


    # Enter a parse tree produced by VagaxParser#varDecl.
    def enterVarDecl(self, ctx:VagaxParser.VarDeclContext):
        pass

    # Exit a parse tree produced by VagaxParser#varDecl.
    def exitVarDecl(self, ctx:VagaxParser.VarDeclContext):
        pass


    # Enter a parse tree produced by VagaxParser#type.
    def enterType(self, ctx:VagaxParser.TypeContext):
        pass

    # Exit a parse tree produced by VagaxParser#type.
    def exitType(self, ctx:VagaxParser.TypeContext):
        pass


    # Enter a parse tree produced by VagaxParser#assignment.
    def enterAssignment(self, ctx:VagaxParser.AssignmentContext):
        pass

    # Exit a parse tree produced by VagaxParser#assignment.
    def exitAssignment(self, ctx:VagaxParser.AssignmentContext):
        pass


    # Enter a parse tree produced by VagaxParser#ifStatement.
    def enterIfStatement(self, ctx:VagaxParser.IfStatementContext):
        pass

    # Exit a parse tree produced by VagaxParser#ifStatement.
    def exitIfStatement(self, ctx:VagaxParser.IfStatementContext):
        pass


    # Enter a parse tree produced by VagaxParser#whileStatement.
    def enterWhileStatement(self, ctx:VagaxParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by VagaxParser#whileStatement.
    def exitWhileStatement(self, ctx:VagaxParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by VagaxParser#forStatement.
    def enterForStatement(self, ctx:VagaxParser.ForStatementContext):
        pass

    # Exit a parse tree produced by VagaxParser#forStatement.
    def exitForStatement(self, ctx:VagaxParser.ForStatementContext):
        pass


    # Enter a parse tree produced by VagaxParser#block.
    def enterBlock(self, ctx:VagaxParser.BlockContext):
        pass

    # Exit a parse tree produced by VagaxParser#block.
    def exitBlock(self, ctx:VagaxParser.BlockContext):
        pass


    # Enter a parse tree produced by VagaxParser#functionDecl.
    def enterFunctionDecl(self, ctx:VagaxParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by VagaxParser#functionDecl.
    def exitFunctionDecl(self, ctx:VagaxParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by VagaxParser#paramList.
    def enterParamList(self, ctx:VagaxParser.ParamListContext):
        pass

    # Exit a parse tree produced by VagaxParser#paramList.
    def exitParamList(self, ctx:VagaxParser.ParamListContext):
        pass


    # Enter a parse tree produced by VagaxParser#returnStmt.
    def enterReturnStmt(self, ctx:VagaxParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by VagaxParser#returnStmt.
    def exitReturnStmt(self, ctx:VagaxParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by VagaxParser#expr.
    def enterExpr(self, ctx:VagaxParser.ExprContext):
        pass

    # Exit a parse tree produced by VagaxParser#expr.
    def exitExpr(self, ctx:VagaxParser.ExprContext):
        pass


    # Enter a parse tree produced by VagaxParser#functionCall.
    def enterFunctionCall(self, ctx:VagaxParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by VagaxParser#functionCall.
    def exitFunctionCall(self, ctx:VagaxParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by VagaxParser#argList.
    def enterArgList(self, ctx:VagaxParser.ArgListContext):
        pass

    # Exit a parse tree produced by VagaxParser#argList.
    def exitArgList(self, ctx:VagaxParser.ArgListContext):
        pass


    # Enter a parse tree produced by VagaxParser#literal.
    def enterLiteral(self, ctx:VagaxParser.LiteralContext):
        pass

    # Exit a parse tree produced by VagaxParser#literal.
    def exitLiteral(self, ctx:VagaxParser.LiteralContext):
        pass


    # Enter a parse tree produced by VagaxParser#instruccionGrafica.
    def enterInstruccionGrafica(self, ctx:VagaxParser.InstruccionGraficaContext):
        pass

    # Exit a parse tree produced by VagaxParser#instruccionGrafica.
    def exitInstruccionGrafica(self, ctx:VagaxParser.InstruccionGraficaContext):
        pass


    # Enter a parse tree produced by VagaxParser#allocStmt.
    def enterAllocStmt(self, ctx:VagaxParser.AllocStmtContext):
        pass

    # Exit a parse tree produced by VagaxParser#allocStmt.
    def exitAllocStmt(self, ctx:VagaxParser.AllocStmtContext):
        pass


    # Enter a parse tree produced by VagaxParser#freeStmt.
    def enterFreeStmt(self, ctx:VagaxParser.FreeStmtContext):
        pass

    # Exit a parse tree produced by VagaxParser#freeStmt.
    def exitFreeStmt(self, ctx:VagaxParser.FreeStmtContext):
        pass


    # Enter a parse tree produced by VagaxParser#memStmt.
    def enterMemStmt(self, ctx:VagaxParser.MemStmtContext):
        pass

    # Exit a parse tree produced by VagaxParser#memStmt.
    def exitMemStmt(self, ctx:VagaxParser.MemStmtContext):
        pass



del VagaxParser