# Generated from grammar/VagaxParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .VagaxParser import VagaxParser
else:
    from VagaxParser import VagaxParser

# This class defines a complete generic visitor for a parse tree produced by VagaxParser.

class VagaxParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VagaxParser#program.
    def visitProgram(self, ctx:VagaxParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#statement.
    def visitStatement(self, ctx:VagaxParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#varDecl.
    def visitVarDecl(self, ctx:VagaxParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#type.
    def visitType(self, ctx:VagaxParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#assignment.
    def visitAssignment(self, ctx:VagaxParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#ifStatement.
    def visitIfStatement(self, ctx:VagaxParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#whileStatement.
    def visitWhileStatement(self, ctx:VagaxParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#forStatement.
    def visitForStatement(self, ctx:VagaxParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#block.
    def visitBlock(self, ctx:VagaxParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#functionDecl.
    def visitFunctionDecl(self, ctx:VagaxParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#paramList.
    def visitParamList(self, ctx:VagaxParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#returnStmt.
    def visitReturnStmt(self, ctx:VagaxParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#expr.
    def visitExpr(self, ctx:VagaxParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#functionCall.
    def visitFunctionCall(self, ctx:VagaxParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#argList.
    def visitArgList(self, ctx:VagaxParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#literal.
    def visitLiteral(self, ctx:VagaxParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#instruccionGrafica.
    def visitInstruccionGrafica(self, ctx:VagaxParser.InstruccionGraficaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#allocStmt.
    def visitAllocStmt(self, ctx:VagaxParser.AllocStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#freeStmt.
    def visitFreeStmt(self, ctx:VagaxParser.FreeStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VagaxParser#memStmt.
    def visitMemStmt(self, ctx:VagaxParser.MemStmtContext):
        return self.visitChildren(ctx)



del VagaxParser