grammar LULU;
args_var : TYPE ('[' ']')* ID | args_var ',' TYPE ('[' ']')* ID











DIGITS :[0-9];
LOWERCASE : [a-z];
UPERCASE  : [A-Z];
TYPE :  'int' | 'bool' | 'float' | 'string' | ID  | 'type';
ACCESS_MODIFIER : 'public' | 'private' | 'protected';
ID : (LOWERCASE* UPERCASE* | '@' | '_')+ DIGITS* ([a-z][A-z] | '@' | '_' | [0-9])*;
RALATION_OP : '==' | '!=' | '<=' | '>=' | '>' | '<';
BITWISE_OP: '~' | '|' | '&';
LOGIC_OP : '!' | '||' | '&&';


ARITHMATIC_OP : '+' | '-' | '*' | '/' | '%';

WHITESPACE : ' '* | '\t'*;

NEWLINE : '\r' | '\n' | '\n\r';

HEX :   ('a' | 'A' | 'b' | 'B' | 'C' |'c' | 'd' | 'D' | 'e' | 'E' | 'f' | 'F');

INT_CONST : [0-9]+ | ('0h' | '0H')(HEX* DIGITS*)*;
