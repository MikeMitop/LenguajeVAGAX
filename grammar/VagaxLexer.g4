lexer grammar VagaxLexer;

// --- PALABRAS RESERVADAS ---
IF       : 'ifvag';
ELSE     : 'elsevag';
WHILE    : 'whilevag';
FOR      : 'forvag';
IN       : 'invag';
FUNCTION : 'functionvag';
RETURN   : 'returnvag';
END      : 'endvag';
IMPORT   : 'importvag';
AS       : 'asvag';

// --- TIPOS ---
INT       : 'intvag';
FLOAT     : 'floatvag';
BOOL_T    : 'boolvag';
STRING_T  : 'stringvag';
LIST      : 'listvag';
DICC      : 'diccvag';
MATRIX    : 'matrixvag';
DATAFRAME : 'dataframevag';

// --- LITERALES ---
BOOL_LIT : 'sisas' | 'nokas'; // True | False
NUMBER   : [0-9]+ ('.' [0-9]+)?;
STRING   : '"' (~["\r\n])* '"' ;

// --- IDENTIFICADORES ---
ID : [a-zA-Z_][a-zA-Z0-9_]* ;

// --- OPERADORES ARITMÉTICOS ---
PLUS   : '+' ;
MINUS  : '-' ;
MUL    : '*' ;
DIV    : '/' ;
MOD    : '%' ;
POW    : '^' ;
ASSIGN : '=' ;

// --- SIGNOS DE PUNTUACIÓN ---
COLON  : ':' ;
COMMA  : ',' ;
SEMI   : ';' ;
DOT    : '.' ;

// --- AGRUPADORES ---
LPAREN : '(' ;
RPAREN : ')' ;
LBRACK : '[' ;
RBRACK : ']' ;
LBRACE : '{' ;
RBRACE : '}' ;

// --- OPERADORES LÓGICOS Y COMPARACIÓN ---
EQ  : '==' ;
NEQ : '!=' ;
LE  : '<=' ;
GE  : '>=' ;
LT  : '<' ;
GT  : '>' ;

OR  : '||' ;
AND : '&&' ;
NOT : '!' ;

// --- COMENTARIOS Y ESPACIOS ---
COMMENT : '//' ~[\r\n]* -> skip ;
WS      : [ \t\r\n]+ -> skip ;