grammar LULU;
args_var : TYPE ('[' ']')* ID | args_var ',' TYPE ('[' ']')* ID;











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
