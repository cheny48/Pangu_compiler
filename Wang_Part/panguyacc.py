import ply.yacc as yacc
import pangulex
import sys

tokens = pangulex.tokens

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/', 'MOD','AND', 'OR'),
    ('right', 'UMINUS', 'UNOT'),
)

def p_expression(p):
    '''expression : simple_expression
                  | expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | expression MOD expression
                  | expression AND expression
                  | expression OR expression '''
    if (len(p) == 2):
        print("*** expression : simple_expression")
    else:
        if p[2] == 'and':
            print("*** expression : expression AND expression")
        elif p[2] == 'or':
            print("*** expression : expression OR expression")
        elif p[2] == 'mod':
            print("*** expression : expression MOD expression")
        else:
            print("*** expression : expression",p[2],"expression")

def p_expression_uminus(p):
    "expression : '-' simple_expression %prec UMINUS"
    print("*** expression : '-' simple_expression")

def p_expression_not(p):
    "expression : NOT simple_expression %prec UNOT"
    print("*** expression : NOT simple_expression")


def p_expression_group(p):
    "simple_expression : '(' expression ')'"
    print("*** simple_expression : ( expression )")

def p_expression_int_literal(p):
    "simple_expression : INT_LIT"
    print("*** simple_expression : INT_LIT")
    
def p_expression_float_literal(p):
    "simple_expression : FLOAT_LIT"
    print("*** simple_expression : FLOAT_LIT")

def p_expression_bool_literal(p):
    """simple_expression : FALSE
                         | TRUE """
    if p[1] == 'False':
        print("*** simple_expression : FALSE")
    else:
        print("*** simple_expression : TRUE")

def p_expression_char_literal(p):
    "simple_expression : CHAR_LIT"
    print("*** simple_expression : CHAR_LIT")
    
def p_expression_string_literal(p):
    "simple_expression : STRING_LIT "
    print("*** simple_expression : STRING_LIT")

def p_reference1(p):
    "reference : ID_DOT reference"
    print("*** reference : ID_DOT reference")

def p_referene2(p):
    "reference : ID"
    print("*** reference : ID")

def p_expression_reference(p):
    "simple_expression : reference"
    print("*** simple_expression : reference")
    
#page 390 start

#VarMultiDef1

def p_var_multi_def_1(p):
    '''var_multi_def_1 : ',' ID init var_multi_def_1
                    |  '''
    if (len(p) == 1):
        print("*** var_multi_def_1 : epsilon")
    else:
        print("*** var_multi_def_1 : , ID init var_multi_def_1")


#Init
def p_init1(p):
    '''init : '=' expression
            | '''
    if (len(p) == 1):
        print("*** init : empty")
    else:
        print("*** init : '=' expression")

def p_init2(p):
    '''init : PASSIG alloc '''
    print("*** init : @= alloc")

def p_init2(p):
    '''init : PASSIG expression '''
    print("*** init : @= expression")

#MethodBody
def p_method_body_1(p):
    '''method_body : stm method_body'''
    print("*** method_body : stm method_body")

def p_method_body_2(p):
    '''method_body : var_multi_def method_body
                   | RB'''
    if(len(p) == 2):
        print("*** method_body : }")
    else:
        print("*** method_body : var_multi_def method_body")

    
#Stm
def p_stm(p):
    '''stm : ID_COLON ustm
           | ustm '''
    if (len(p) == 2):
        print("*** stm : ustm")
    else:
        print("*** stm : ID_COLON ustm")


#Ustm

def p_ustm1(p):
    '''ustm : ';' '''
    print("*** ustm : ;")

def p_ustm2(p):
    '''ustm : expression ';' '''
    print("*** ustm : expression ;")

def p_ustm3(p):
    '''ustm : multi_assig ';' '''
    print("*** ustm : multi_assig ;")

def p_ustm4(p):
    '''ustm : if_stm '''
    print("*** ustm : if_stm")

def p_ustm5(p):
    '''ustm : if_else_stm '''
    print("*** ustm : if_else_stm")

def p_ustm6(p):
    '''ustm : for_stm'''
    print("*** ustm : for_stm")

def p_ustm7(p):
    '''ustm : while_stm ';' '''
    print("*** ustm : while_stm")

def p_ustm8(p):
    '''ustm : GOTO ID ';' '''
    print("*** ustm : GOTO ID ;")

def p_ustm9(p):
    '''ustm : CONTINUE ';' '''
    print("*** ustm : CONTINUE ;")

def p_ustm10(p):
    '''ustm : BREAK ';' '''
    print("*** ustm : BREAK ;")

def p_ustm11(p):
    '''ustm : TERMINATE ';' '''
    print("*** ustm : TERMINATE ;")

def p_ustm12(p):
    '''ustm : return_stm '''
    print("*** ustm : return_stm")

def p_ustm13(p):
    '''ustm : RETURN expression ';' '''
    print("*** ustm : RETURN expression ;")

def p_ustm14(p):
    '''ustm : THROW expression ';' '''
    print("*** ustm : THROW expression ;")

def p_ustm15(p):
    '''ustm : try_catch_stm '''
    print("*** ustm : try_catch_stm ")

 
#IfStm
def p_if_stm(p):
    '''if_stm : IF_LP cond ')' then_part PEEKNOTELESE''' #miss peeknotelse& IF_LP#
    print("*** if_stm : IF_LP cond ) then_part PEEKNOTELESE")


def p_then_part(p):
    '''then_part : ustm
                 | '{' then_part_1 '}' '''
    if(len(p) == 2):
        print("*** then_part : ustm")
    else:
        print("*** then_part : { then_part_1 }")

def p_then_part_1(p):
    '''then_part_1 : stm then_part_1
                   | '''
    if (len(p) != 1):
        print("*** then_part_1 : stm then_part_1")
    else:
        print("*** then_part_1 : empty")

#page 390 end
 
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
        print("line={},pos={}".format(p.lineno,p.lexpos-pangulex.last_newline))
        print("offending token =",p.type,p.value)
        sys.exit(0)
    else:
        print("Syntax error at EOF")
        sys.exit(0)

# test lexer
def TestLexer(file):
    pangulex.show_tokens = False
    f = open(file,"rt")
    if f.mode == "rt":
        data = f.read()
        f.close()
    else:
        print("can't open input file '"+file+"'")
        sys.exit(0)
    print(data)
    pangulex.lexer.input(data)
    while True:
        t = pangulex.lexer.token()
        if not t:
            break
        else:
            print("***",t)
    #end while
#end TestLexar

#TestLexer("xxx.asc")


# run parser
def Parser(file):
    f = open(file,"rt")
    if f.mode == "rt":
        data = f.read()
        f.close()
    else:
        print("can't open input file '"+file+"'")
        sys.exit(0)
    print(data)
    pangupar = yacc.yacc()
    pangulex.show_tokens = False
    pangupar.parse(data,pangulex.lexer,False,False,None)
    print("parsing done")
#end Parser
  
Parser('test.pan')

