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
expr : expr Binary_op expr | '(' expr ')' | Unary_op expr| const_val| 'allocate' handle_call | func_call | var | list | list | 'nil' ;
const_val : Int_const | Real_const | Bool_const | String_const;
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
And : '&';
Or : '|';
Not : '!';
L_or : '||';
L_and : '&&';
Negation : '~';
CONST : 'const';
True : 'true';
False : 'false';
HEX_DIGITS :   ('a' | 'A' | 'b' | 'B' | 'C' |'c' | 'd' | 'D' | 'e' | 'E' | 'f' | 'F');
Arithmatic : Addition | Subtraction | Multipliction | Division | Modulus;;
Relational : Equal | Not_Equal | Less_Than_or_Equal | Bigger_than_or_equal | Less_than | Bigger_than ;
Bitwise : Or | And | Negation ;
Logical : L_or | L_and | Not;
Unary_op: Subtraction | Not | Negation ;
Binary_op : Arithmatic | Relational | Bitwise | Logical;
HEX_NUMBERS : ('0h' | '0H')(HEX_DIGITS* DIGITS)*;
Int_const : DIGITS | HEX_NUMBERS+;
Real_const : (DIGITS'.'DIGITS)+ | (HEX_NUMBERS'.'HEX_NUMBERS)+ | DIGITS+'^'('+' | '-')?DIGITS+;
Bool_const : True | False ;
