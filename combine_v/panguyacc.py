import ply.yacc as yacc
import pangulex
import sys

tokens = pangulex.tokens

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/', '%','AND', 'OR'),
    ('right', 'UMINUS', 'UNOT'),
)


def p_expression(p):
    '''expression : simple_expression
                  | modifier
                  | expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | expression '%' expression
                  | expression AND expression
                  | expression OR expression
                  | '''
    if (len(p) == 1):
        print("*** expression : empty")
    elif (len(p) == 2):
        print("*** expression : simple_expression")
    else:
        if p[2] == 'and':
            print("*** expression : expression AND expression")
        elif p[2] == 'or':
            print("*** expression : expression OR expression")
        elif p[2] == '%':
            print("*** expression : expression % expression")
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
                         | TRUE"""
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


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
        print("line={},pos={}".format(p.lineno,p.lexpos-pangulex.last_newline))
        print("offending token =",p.type,p.value)
        sys.exit(0)
    else:
        print("Syntax error at EOF")
        sys.exit(0)

#p389
# def p_attri_multi_def(p):
#     '''attri_multi_def : prefix data_type ID init attri_multi_def_1 SEPICOL'''
#     print("*** attri_multi_def : attri_multi_def")
#
# def p_attri_multi_def_1(p):
#     '''attri_multi_def_1 : COMMA ID init attri_multi_def_1
#                          | '''
#     if (len(p) == 1):
#         print("*** attri_multi_def_1 : empty")
#     else:
#         print("*** attri_multi_def_1 : attri_multi_def_1")
#
# def p_constr_def(p):
#     '''constr_def : CLASSNAME_LP args LB parent_constr method_body'''
#     print("*** constr_def : constr_def")
#
# def p_parent_constr(p):
#     '''parent_constr : PARENT_LP params SEPICOL
#                      | '''
#     if (len(p) == 1):
#         print("*** parent_constr : empty")
#     else:
#         print("*** parent_constr : parent_constr")
#
# def p_methos_def(p):
#     '''methos_def : prefix data_type ID_LP args LB method_body
#                   | prefix VOID ID_LP args LB method_body'''
#     print("*** methos_def : methos_def")
#
# def p_arg(p):
#     '''arg : modifer date_type passing_specifier ID'''
#     print("*** arg : arg")
#
# def p_args(p):
#     '''args : RP
#             | arg args_1'''
#     print("*** args : args")
#
# def p_args_1(p):
#     '''args_1 : RP
#             | COMMA arg args_1'''
#     print("*** args_1 : args_1")
#
def p_modifier(p):
    '''modifier : CONST
                | '''
    if (len(p) == 1):
        print("*** modifier : empty")
    else:
        print("*** modifier : modifier")
#
# def p_passing_specifier(p):
#     '''passing_specifier : AND'''
#     if (len(p) == 1):
#         print("*** passing_specifier : empty")
#     else:
#         print("*** passing_specifier : passing_specifier")
#
# def p_var_multi_def(p):
#     '''var_multi_def : PERM CONST data_type ID init var_multi_def SEPICOL
#                      | CONST PERM data_type ID init var_multi_def SEPICOL
#                      | CONST data_type ID init var_multi_def SEPICOL
#                      | PERM data_type ID init var_multi_def SEPICOL
#                      | data_type ID init var_multi_def SEPICOL'''
#     print("*** var_multi_def : var_multi_def")

#p389 ends

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

TestLexer("test.pan")


# # run parser
# def Parser(file):
#     f = open(file,"rt")
#     if f.mode == "rt":
#         data = f.read()
#         f.close()
#     else:
#         print("can't open input file '"+file+"'")
#         sys.exit(0)
#     print(data)
#     pangupar = yacc.yacc()
#     pangulex.show_tokens = False
#     pangupar.parse(data,pangulex.lexer,False,False,None)
#     #parser = yacc.yacc(tabmodule='testparsetab')
#     print("parsing done")
# #end Parser
#
# Parser('test.pan')
