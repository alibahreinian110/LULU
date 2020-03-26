grammar LULU;















digits  : [0-9]*;
id  : ([a-z] | [A-Z] | '@' | '_')+ digits ([a-z] | [A-Z] | '@' | '_' | [0-9])*;
ralation_op : '==' | '!=' | '<=' | '>=' | '>' | '<';
bitwise_op: '~' | '|' | '&';
logic_op : '!' | '||' | '&&';
keyword : 'allocate' | 'bool' | 'break' | 'caseof' | 'const' | 'continue' | 'default' | 'destruct' | 'else' | 'false' | 'function' | 'float' | 'for' | 'if' | 'int' | 'nill' | 'true' | 'type' | 'while' | 'write'
      'private' | 'protected' | 'public' | 'read' | 'string' | 'super' | 'switch' | 'this';


arithmetic_op : '+' | '-' | '*' | '/' | '%';

whitespace : ' '* | '\t'*;

newline : '\r' | '\n' | '\n\r';

hex :   ('a' | 'A' | 'b' | 'B' | 'C' |'c' | 'd' | 'D' | 'e' | 'E' | 'f' | 'F')*;

int_const : [0-9]+ | 0('h' | 'H')(hex digits)*;
