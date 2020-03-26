grammer LULU;

ID  : ([a-z] | [A-Z] | '@' | '_')+ [0-9]* ([a-z] | [A-Z] | '@' | '_' | [0-9])*;

















keyword : 'allocate' | 'bool' | 'break' | 'caseof' | 'const' | 'continue' | 'default' | 'destruct' | 'else' | 'false' | 'function' | 'float' | 'for' | 'if' | 'int' | 'nill' | 'true' | 'type' | 'while' | 'write'
      'private' | 'protected' | 'public' | 'read' | 'string' | 'super' | 'switch' | 'this';

fragment addition :   '+';
fragment subtractions :   '-';
fragment multiplication :   '*';
fragment division :   '/';
fragment modulus :   '%';

arithmetic_op : addition | subtractions | multiplication | division | modulus;
