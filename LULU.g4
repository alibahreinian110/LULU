grammar LULU;















Digits :[0-9];
Id : ([a-z][A-z] | '@' | '_')+ Digits* ([a-z][A-z] | '@' | '_' | [0-9])*;
ralation_op : '==' | '!=' | '<=' | '>=' | '>' | '<';
bitwise_op: '~' | '|' | '&';
logic_op : '!' | '||' | '&&';
keyword : 'allocate' | 'bool' | 'break' | 'caseof' | 'const' | 'continue' | 'default' | 'destruct' | 'else' | 'false' | 'function' | 'float' | 'for' | 'if' | 'int' | 'nill' | 'true' | 'type' | 'while' | 'write'
      'private' | 'protected' | 'public' | 'read' | 'string' | 'super' | 'switch' | 'this';


arithmetic_op : '+' | '-' | '*' | '/' | '%';

whitespace : ' '* | '\t'*;

newline : '\r' | '\n' | '\n\r';

Hex :   ('a' | 'A' | 'b' | 'B' | 'C' |'c' | 'd' | 'D' | 'e' | 'E' | 'f' | 'F');

Int_const : [0-9]+ | ('0h' | '0H')(Hex* Digits*)*;
