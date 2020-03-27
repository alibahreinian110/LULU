grammar LULU;
program : ft_def;
ft_def : type_def | fun_def ;
type_def : 'type' ID (':' ID)? '{' (component)+ '}';
component : ACCESS_MODIFIER? ( var_def | fun_def );
var_def : 'const'? TYPE var_val (',' var_val)* ';';
var_val : ref ('=' expr)? ;
fun_def : ('(' args_var ')' '=' )? 'function'ID '(' args_var?  ')' block ;
args_var : TYPE ('[' ']')* ID | args_var ',' TYPE ('[' ']')* ID;
block : '{' (var_def | stmt )* '}';
stmt : assign ';' | func_call ';' | cond_stmt | loop_stmt | 'break' ';'| 'continue' ';' | 'destruct' ('[' ']')* ID ';' ;
assign : ( var | '(' var (',' var )* ')') '=' expr ;
var : ((THIS | SUPER)'.')? ref ('.' ref )* ;
ref : ID ('[' expr ']')* ;
expr : expr BINARY_OP expr  | '(' expr ')' | UNARY_OP  expr | CONST_VAL | ALLOCATE handle_call | func_call | var | list_ | NIL ;
func_call : (var '.')? handle_call | READ '('')' | WRITE '(' expr ')' ;
list_ : '[' (expr | list_ ) (','(expr | list_ ))* ']' ;
handle_call : ID '(' params? ')' ;
params : expr | expr ',' params ;
cond_stmt : IF expr ( block | stmt ) (ELSE ( block | stmt ))? | SWITCH var '{' switch_body '}' ;
switch_body : (CASEOF INT_CONST ':' block )+ (DEFAULT ':' block)?;
loop_stmt : FOR (TYPE? assign )? ';' expr ';' assign? block | WHILE expr ( block | stmt) ;



fragment DIGITS :[0-9];
fragment LOWERCASE : [a-z];
fragment UPERCASE  : [A-Z];

IF : 'if';
ELSE : 'else';
SWITCH : 'switch';
CASEOF : 'caseof';
DEFAULT : 'default';

FOR : 'for';
WHILE : 'while';

ALLOCATE : 'allocate';

NIL : 'nil';

READ : 'read';
WRITE : 'write';

THIS : 'this';
SUPER : 'super';

INT : 'int';
BOOL : 'bool';
FLOAT : 'float';
STRING : 'string';
TYPE :  INT | BOOL | FLOAT | STRING | ID  | 'type';

PUBLIC :  'public';
PRIVATE : 'private';
PROTECTED :  'protected';
ACCESS_MODIFIER : 'public' | 'private' | 'protected';

ID :  ('@' | '_' | UPERCASE LOWERCASE)('@' | '_' | UPERCASE LOWERCASE | DIGITS)*;

RELATION_OP : '==' | '!=' | '<=' | '>=' | '>' | '<';
BITWISE_OP: '~' | '|' | '&';
LOGIC_OP : '!' | '||' | '&&';
ARITHMATIC_OP : '+' | '-' | '*' | '/' | '%';

BINARY_OP : ARITHMATIC_OP | RELATION_OP | BITWISE_OP | LOGIC_OP;
UNARY_OP  : '-' | '!' | '~';

WHITESPACE : ' '+ | '\t'+;

NEWLINE : '\r'+ | '\n'+ | '\n\r'+;

fragment HEX_DIGITS :   [a-fA-F];
fragment HEX_NUMBERS : ('0h' | '0H')(HEX_DIGITS* DIGITS*)*;
INT_CONST : DIGITS+ | HEX_NUMBERS+;
REAL_CONST : (DIGITS*'.'DIGITS*)+ | (HEX_NUMBERS'.'HEX_NUMBERS)+ | DIGITS+'^'('+' | '-')?DIGITS+;

fragment True : 'true';
fragment False: 'false';
BOOL_CONST : 'true' | 'false';

fragment ESCAPE_CHARS :  WHITESPACE | '\\';
fragment TEXT :  ESCAPE_CHARS*LOWERCASE*UPERCASE*WHITESPACE*DIGITS;
STRING_CONST : '"'TEXT*'"';


CONST_VAL : INT_CONST | REAL_CONST | BOOL_CONST | STRING_CONST;

COMMENT : '$$'TEXT*'$$';
