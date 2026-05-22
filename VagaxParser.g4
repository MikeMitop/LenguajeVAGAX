parser grammar VagaxParser;

options { tokenVocab=VagaxLexer; }

// -------- PROGRAMA --------

program
    : statement* EOF
    ;

// -------- SENTENCIAS --------

statement
    : varDecl SEMI
    | assignment SEMI
    | allocStmt SEMI
    | freeStmt SEMI
    | memStmt SEMI
    | ifStatement
    | whileStatement
    | forStatement
    | functionDecl
    | returnStmt SEMI
    | expr SEMI
    ;

// -------- DECLARACIÓN DE VARIABLES --------

varDecl
    : type ID ASSIGN expr
    | type ID
    ;

type
    : INT
    | FLOAT
    | BOOL_T
    | STRING_T
    | LIST
    | MATRIX
    | DICC
    | DATAFRAME
    ;

// -------- ASIGNACIÓN --------

assignment
    : ID ASSIGN expr
    ;

// -------- IF --------

ifStatement
    : IF LPAREN expr RPAREN block
      (ELSE block)?
      END
    ;

// -------- WHILE --------

whileStatement
    : WHILE LPAREN expr RPAREN block END
    ;

// -------- FOR --------

forStatement
    : FOR LPAREN assignment SEMI expr SEMI assignment RPAREN block END
    ;

// -------- BLOQUES --------

block
    : LBRACE statement* RBRACE
    ;

// -------- FUNCIONES --------

functionDecl
    : FUNCTION ID LPAREN paramList? RPAREN block END
    ;

paramList
    : ID (COMMA ID)*
    ;

// -------- RETURN --------

returnStmt
    : RETURN expr
    ;

// -------- EXPRESIONES --------

expr
    : expr POW expr
    | expr MUL expr
    | expr DIV expr
    | expr MOD expr
    | expr PLUS expr
    | expr MINUS expr
    | expr EQ expr
    | expr NEQ expr
    | expr LT expr
    | expr GT expr
    | expr LE expr
    | expr GE expr
    | expr AND expr
    | expr OR expr
    | NOT expr
    | LPAREN expr RPAREN
    | functionCall
    | literal
    | ID
    ;

// -------- LLAMADA A FUNCIÓN --------

functionCall
    : ID LPAREN argList? RPAREN
    ;

argList
    : expr (COMMA expr)*
    ;

// -------- LITERALES --------

literal
    : NUMBER
    | STRING
    | BOOL_LIT
    ;

//------ REGLAS GRAFICAS ------

instruccionGrafica
    : PLOTVAG '(' expr ',' expr ')' ';' // plotvag(x,y);
    | TITLEVAG '('  STRING ')' ';' // titlevag("titulo");
    | SHOWVAG '('  ')' ';' // showvag();
    ;

//------ REGLAS MEMORIA ------    
    
    allocStmt
    : ALLOCVAG ID ASSIGN expr
    ;

freeStmt
    : FREEVAG LPAREN ID RPAREN
    ;

memStmt
    : MEMVAG LPAREN RPAREN
    ;
