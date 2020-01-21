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
    print(len(p))
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

def p_var_multi_def1(p):
    """varmultidef1 : ',' ID init varmultidef1
                    |  empty"""
    if (len(p) == 1):
        print("*** VarMultiDef1 : empty")
    else:
        print("*** VarMultiDef1 : ',' ID init varmultidef1")
        
def p_init(p):
    """init : '=' expression
            | '@=' expression
            | '@=' alloc """
    if (p[1] == '='):
        print("*** init : '='", p[2])
    else:
        print("*** init : '@='", p[2])

def p_stm(p):
    '''stm : ID_COLON ustm
                 | ustm '''
                 
def p_ustm(p):
    '''ustm : ';'
            | expression ';'
            | multiassig ';'
            | ifstm
            | ifelsestm
            | forstm
            | whilestm
            | GOTO ID ';'
            | CONTINUE ';'
            | BREAK ';'
            | TERMINATE ';'
            | returnstm
            | PRETURN expression ';'
            | THROW expression ';'
            | trycatchstm '''
            
def p_ifstm(p):
    "ifstm : IF ( cond ) thenpart" #miss peeknotelse& IF_LP#
    
def p_thenpart(p):
    '''thenpart : ustm
                | { thenpart1 } '''
                
def p_thenpart1(p):
    '''thenpart1 : stm thenpart1
                 | empty '''
    
    
    

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

