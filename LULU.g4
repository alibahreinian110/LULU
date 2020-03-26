grammar LULU;















ID  : ([a-z] | [A-Z] | '@' | '_')+ [0-9]* ([a-z] | [A-Z] | '@' | '_' | [0-9])*;
ralation_op : '==' | '!=' | '<=' | '>=' | '>' | '<';
bitwise_op: '~' | '|' | '&';
logic_op : '!' | '||' | '&&';
keyword : 'allocate' | 'bool' | 'break' | 'caseof' | 'const' | 'continue' | 'default' | 'destruct' | 'else' | 'false' | 'function' | 'float' | 'for' | 'if' | 'int' | 'nill' | 'true' | 'type' | 'while' | 'write'
      'private' | 'protected' | 'public' | 'read' | 'string' | 'super' | 'switch' | 'this';


arithmetic_op : '+' | '-' | '*' | '/' | '%';

whitespace : ' '* | '\t'*

newline : '\r' | '\n' | '\n\r'
