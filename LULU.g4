grammar LULU;
ft_def : type_def | fun_def ;
type_def : 'type' ID (':' ID)? '{' (component)+ '}';
component : ACCESS_MODIFIER? ( var_def | fun_def );
var_def : 'const'? TYPE var_val (',' var_val)* ';';
var_val : ref ('=' expr)? ;
fun_def : ('(' args_var ')' '=' )? 'function'ID '(' args_var?  ')' block ;
args_var : TYPE ('[' ']')* ID | args_var ',' TYPE ('[' ']')* ID;
block : '{' (var_def | stmt )* '}';
stmt : assign ';' | func_call ';' | cond_stmt | loop_stmt | break ';'| 'continue' ';' | 'destruct' ('[' ']')* ID ';' ;
assign : ( var | '(' var (',' var )* ')') '=' expr ;
var : (('this' | 'super')'.')? ref ('.' ref )* ;
ref : ID ('[' expr ']')* ;
expr : expr BINARY_OP expr  | '(' expr ')' | UNARY_OP  expr | CONST_VAL | 'allocate' handle_call | func_call | var | list | 'nil' ;












DIGITS :[0-9];
LOWERCASE : [a-z];
UPERCASE  : [A-Z];
TYPE :  'int' | 'bool' | 'float' | 'string' | ID  | 'type';
ACCESS_MODIFIER : 'public' | 'private' | 'protected';
ID : (LOWERCASE* UPERCASE* | '@' | '_')+ DIGITS* (LOWERCASE* UPERCASE* | '@' | '_' | DIGITS*)*;
RALATION_OP : '==' | '!=' | '<=' | '>=' | '>' | '<';
BITWISE_OP: '~' | '|' | '&';
LOGIC_OP : '!' | '||' | '&&';


ARITHMATIC_OP : '+' | '-' | '*' | '/' | '%';

WHITESPACE : ' '+ | '\t'+;

NEWLINE : '\r'+ | '\n'+ | '\n\r'+;

HEX_DIGITS :   ('a' | 'A' | 'b' | 'B' | 'C' |'c' | 'd' | 'D' | 'e' | 'E' | 'f' | 'F');
HEX_NUMBERS : ('0h' | '0H')(HEX_DIGITS* DIGITS*)*;
INT_CONST : DIGITS+ | HEX_NUMBERS+;
REAL_CONST : (DIGITS*'.'DIGITS*)+ | (HEX_NUMBERS'.'HEX_NUMBERS)+ | DIGITS+'^'('+' | '-')?DIGITS+;
BOOL_CONST : 'true' | 'false';


CONST_VAL : INT_CONST | REAL_CONST | BOOL_CONST;
