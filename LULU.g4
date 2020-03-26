grammar LULU;















DIGITS :[0-9];
ID : ([a-z][A-z] | '@' | '_')+ DIGITS* ([a-z][A-z] | '@' | '_' | [0-9])*;
RALATION_OP : '==' | '!=' | '<=' | '>=' | '>' | '<';
BITWISE_OP: '~' | '|' | '&';
LOGIC_OP : '!' | '||' | '&&';
KEYWORD : 'allocate' | 'bool' | 'break' | 'caseof' | 'const' | 'continue' | 'default' | 'destruct' | 'else' | 'false' | 'function' | 'float' | 'for' | 'if' | 'int' | 'nill' | 'true' | 'type' | 'while' | 'write'
      'private' | 'protected' | 'public' | 'read' | 'string' | 'super' | 'switch' | 'this';


ARITHMATIC_OP : '+' | '-' | '*' | '/' | '%';

WHITESPACE : ' '* | '\t'*;

NEWLINE : '\r' | '\n' | '\n\r';

HEX :   ('a' | 'A' | 'b' | 'B' | 'C' |'c' | 'd' | 'D' | 'e' | 'E' | 'f' | 'F');

INT_CONST : [0-9]+ | ('0h' | '0H')(HEX* DIGITS*)*;
