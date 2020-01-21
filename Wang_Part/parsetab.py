
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-left*/MODANDORrightUMINUSUNOTAND CHAR_LIT ERROR FALSE FLOAT_LIT ID ID_DOT ID_LP INT_LIT MOD NOT OR STRING_LIT TRUEexpression : simple_expression\n                  | expression '+' expression\n                  | expression '-' expression\n                  | expression '*' expression\n                  | expression '/' expression\n                  | expression MOD expression\n                  | expression AND expression\n                  | expression OR expression expression : '-' simple_expression %prec UMINUSexpression : NOT simple_expression %prec UNOTsimple_expression : '(' expression ')'simple_expression : INT_LITsimple_expression : FLOAT_LITsimple_expression : FALSE\n                         | TRUE simple_expression : CHAR_LITsimple_expression : STRING_LIT reference : ID_DOT referencereference : IDsimple_expression : referenceinit : '=' expression"
    
_lr_action_items = {'-':([0,1,2,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,],[3,16,-1,3,-12,-13,-14,-15,-16,-17,-20,-19,3,3,3,3,3,3,3,-9,-10,16,-18,-2,-3,-4,-5,-6,-7,-8,-11,]),'NOT':([0,5,15,16,17,18,19,20,21,],[4,4,4,4,4,4,4,4,4,]),'(':([0,3,4,5,15,16,17,18,19,20,21,],[5,5,5,5,5,5,5,5,5,5,5,]),'INT_LIT':([0,3,4,5,15,16,17,18,19,20,21,],[6,6,6,6,6,6,6,6,6,6,6,]),'FLOAT_LIT':([0,3,4,5,15,16,17,18,19,20,21,],[7,7,7,7,7,7,7,7,7,7,7,]),'FALSE':([0,3,4,5,15,16,17,18,19,20,21,],[8,8,8,8,8,8,8,8,8,8,8,]),'TRUE':([0,3,4,5,15,16,17,18,19,20,21,],[9,9,9,9,9,9,9,9,9,9,9,]),'CHAR_LIT':([0,3,4,5,15,16,17,18,19,20,21,],[10,10,10,10,10,10,10,10,10,10,10,]),'STRING_LIT':([0,3,4,5,15,16,17,18,19,20,21,],[11,11,11,11,11,11,11,11,11,11,11,]),'ID_DOT':([0,3,4,5,13,15,16,17,18,19,20,21,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'ID':([0,3,4,5,13,15,16,17,18,19,20,21,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'$end':([1,2,6,7,8,9,10,11,12,14,22,23,25,26,27,28,29,30,31,32,33,],[0,-1,-12,-13,-14,-15,-16,-17,-20,-19,-9,-10,-18,-2,-3,-4,-5,-6,-7,-8,-11,]),'+':([1,2,6,7,8,9,10,11,12,14,22,23,24,25,26,27,28,29,30,31,32,33,],[15,-1,-12,-13,-14,-15,-16,-17,-20,-19,-9,-10,15,-18,-2,-3,-4,-5,-6,-7,-8,-11,]),'*':([1,2,6,7,8,9,10,11,12,14,22,23,24,25,26,27,28,29,30,31,32,33,],[17,-1,-12,-13,-14,-15,-16,-17,-20,-19,-9,-10,17,-18,17,17,-4,-5,-6,-7,-8,-11,]),'/':([1,2,6,7,8,9,10,11,12,14,22,23,24,25,26,27,28,29,30,31,32,33,],[18,-1,-12,-13,-14,-15,-16,-17,-20,-19,-9,-10,18,-18,18,18,-4,-5,-6,-7,-8,-11,]),'MOD':([1,2,6,7,8,9,10,11,12,14,22,23,24,25,26,27,28,29,30,31,32,33,],[19,-1,-12,-13,-14,-15,-16,-17,-20,-19,-9,-10,19,-18,19,19,-4,-5,-6,-7,-8,-11,]),'AND':([1,2,6,7,8,9,10,11,12,14,22,23,24,25,26,27,28,29,30,31,32,33,],[20,-1,-12,-13,-14,-15,-16,-17,-20,-19,-9,-10,20,-18,20,20,-4,-5,-6,-7,-8,-11,]),'OR':([1,2,6,7,8,9,10,11,12,14,22,23,24,25,26,27,28,29,30,31,32,33,],[21,-1,-12,-13,-14,-15,-16,-17,-20,-19,-9,-10,21,-18,21,21,-4,-5,-6,-7,-8,-11,]),')':([2,6,7,8,9,10,11,12,14,22,23,24,25,26,27,28,29,30,31,32,33,],[-1,-12,-13,-14,-15,-16,-17,-20,-19,-9,-10,33,-18,-2,-3,-4,-5,-6,-7,-8,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,5,15,16,17,18,19,20,21,],[1,24,26,27,28,29,30,31,32,]),'simple_expression':([0,3,4,5,15,16,17,18,19,20,21,],[2,22,23,2,2,2,2,2,2,2,2,]),'reference':([0,3,4,5,13,15,16,17,18,19,20,21,],[12,12,12,12,25,12,12,12,12,12,12,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> simple_expression','expression',1,'p_expression','panguyacc.py',14),
  ('expression -> expression + expression','expression',3,'p_expression','panguyacc.py',15),
  ('expression -> expression - expression','expression',3,'p_expression','panguyacc.py',16),
  ('expression -> expression * expression','expression',3,'p_expression','panguyacc.py',17),
  ('expression -> expression / expression','expression',3,'p_expression','panguyacc.py',18),
  ('expression -> expression MOD expression','expression',3,'p_expression','panguyacc.py',19),
  ('expression -> expression AND expression','expression',3,'p_expression','panguyacc.py',20),
  ('expression -> expression OR expression','expression',3,'p_expression','panguyacc.py',21),
  ('expression -> - simple_expression','expression',2,'p_expression_uminus','panguyacc.py',35),
  ('expression -> NOT simple_expression','expression',2,'p_expression_not','panguyacc.py',39),
  ('simple_expression -> ( expression )','simple_expression',3,'p_expression_group','panguyacc.py',45),
  ('simple_expression -> INT_LIT','simple_expression',1,'p_expression_int_literal','panguyacc.py',49),
  ('simple_expression -> FLOAT_LIT','simple_expression',1,'p_expression_float_literal','panguyacc.py',53),
  ('simple_expression -> FALSE','simple_expression',1,'p_expression_bool_literal','panguyacc.py',57),
  ('simple_expression -> TRUE','simple_expression',1,'p_expression_bool_literal','panguyacc.py',58),
  ('simple_expression -> CHAR_LIT','simple_expression',1,'p_expression_char_literal','panguyacc.py',65),
  ('simple_expression -> STRING_LIT','simple_expression',1,'p_expression_string_literal','panguyacc.py',69),
  ('reference -> ID_DOT reference','reference',2,'p_reference1','panguyacc.py',73),
  ('reference -> ID','reference',1,'p_referene2','panguyacc.py',77),
  ('simple_expression -> reference','simple_expression',1,'p_expression_reference','panguyacc.py',81),
  ('init -> = expression','init',2,'p_init','panguyacc.py',92),
]