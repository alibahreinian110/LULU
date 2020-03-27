grammar LULU2;
program : ft_def+;
ft_def : type_def | fun_def;
type_def : 'type' ID (':' ID)? '{' component+ '}';
component : (access_modifier)?(var_def | fun_def);
access_modifier : Private | Public | Protected;
var_def : 'const'? type var_val (',' var_val ',')*';';
type : Int | Bool | Float | String | Id | Type ;
var_val : ref ('=' expr);
ref : Id ('['expr']')*;
expr : expr binary_op expr | '(' expr ')' | unary_op expr| const_val| 'allocate' handle_call | func_call | var | list | list | 'nil' ;
binary_op : arithmatic | relational | bitwise | logical;
arithmatic : Addition | Subtraction | Multipliction | Division | Modulus;
relational : Equal | Not_Equal | Less_Than_or_Equal | Bigger_than_or_equal | Less_than | Bigger_than ;
fun_def :('('args_var')''=')? 'function' ID '(' (args_var)? ')' block;




fragment DIGIT : [0-9];
fragment DIGITS : DIGIT*;
fragment LETTER : [a-zA-Z];
Int : 'int';
Bool : 'bool';
Float : 'float';
String : 'string';
ID :  ('@' | '_' | LETTER)('@' | '_' | LETER | DIGITS)*;
Type :  Int | Bool | Float | String | ID  | 'type';
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
CONST : 'const'

Arithmatic : '+' | '-' | '*' | '/' |'%';
Relational : '==' | '!==' | '<=' | '>=' | '<' | '>';
Bitwise : '|' | '&';
Logical : '?';
// TODO: logical operators lexer should be added
Binary_op : Arithmatic | Relational | Bitwise | Logical;
