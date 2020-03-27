grammar LULU2;
program : ft_def+;
ft_def : type_def | fun_def;
type_def : 'type' ID (':' ID)? '{' component+ '}';
component : (access_modifier)?(var_def | fun_def);
access_modifier : 'private' | 'public' | 'protected';
var_def : 'const'? type var_val (',' var_val ',')*';';
type : 'int' | 'bool' | 'float' | 'string' | 'id' | 'type';
var_val : ref ('=' expr);
ref : 'id'('['expr']')*;
expr : expr binary_op expr | '(' expr ')' | unary_op expr| const_val| 'allocate' handle_call | func_call | var | list | list | 'nil' ;
binary_op : arithmatic | relational | bitwise | logical;
arithmatic : '+' | '-' | '*' | '/' |'%';
relational : '==' | '!==' | '<=' | '>=' | '<' | '>';
fun_def :('('args_var')''=')? 'function' ID '(' (args_var)? ')' block;




DIGIT : [0-9];
DIGITS : DIGIT*;
LETTER : [a-zA-Z];
Int : 'int';
Bool : 'bool';
Float : 'float';
String : 'string';
//Id : ?;
//Type : ?;
Private : 'private';
Public : 'public';
Protected : 'protected';
Addition : '+';
Subtraction : '-';
Multipliction : '*';
Division : '/';
Modulus : '%';
Equal : '==';
Not_Equal : '!=';
Less_Than_or_Equal : '<=';
Less_than : '<';
Bigger_than : '>';
Bigger_than_or_equal : '>=';