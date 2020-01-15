import ply.yacc as yacc
import pangulex
import sys

tokens = pangulex.tokens

#precedence = (
#    ('left', '+', '-'),
#    ('left', '*', '/', 'MOD','AND', 'OR'),
#    ('right', 'UMINUS', 'UNOT'),
#)

precedence = (
    ('left', '+', '-', 'MOD', 'AND', 'OR', 'LE', 'GE','2GT','2LT','>','<','NE','EQ'),
    ('left', '*', '/'),
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
                  | expression OR expression
                  | simple_expression '<' simple_expression
                  | simple_expression LE simple_expression
                  | simple_expression ">" simple_expression
                  | simple_expression GE simple_expression
                  | simple_expression 2GT simple_expression
                  | simple_expression 2LT simple_expression
                  | simple_expression NE simple_expression
                  | simple_expression EQ simple_expression'''
    if (len(p) == 2):
        print("*** expression : simple_expression")
    else:
        if p[2] == 'and':
            print("*** expression : expression AND expression")
        elif p[2] == 'or':
            print("*** expression : expression OR expression")
        elif p[2] == 'mod':
            print("*** expression : expression MOD expression")
        elif p[2] == '<=':
            print("*** expression : simple_expression LE simple_expression")
        elif p[2] == '>=':
            print("*** expression : simple_expression GE simple_expression")
        elif p[2] == '>>':
            print("*** expression : simple_expression 2GT simple_expression")
        elif p[2] == '<<':
            print("*** expression : simple_expression 2LT simple_expression")
        elif p[2] == '!=':
            print("*** expression : simple_expression NE simple_expression")
        elif p[2] == '==':
            print("*** expression : simple_expression EQ simple_expression")
        elif p[2] == '<':
            print("*** expression : simple_expression < simple_expression")
        elif p[2] == '>':
            print("*** expression : simple_expression > simple_expression")
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

def p_expression_reference(p):
    "simple_expression : reference"
    print("*** simple_expression : reference")

def p_expression_2plus(p):
    '''simple_expression : 2PLUS reference
                         | reference 2PLUS'''
    if(p[1] == "++"):
        print("*** simple_expression : 2PLUS reference")
    else:
        print("*** simple_expression : reference 2PLUS")

def p_expression_2minus(p):
    '''simple_expression : 2MINUS reference
                         | reference 2MINUS'''
    if(p[1] == "--"):
        print("*** simple_expression : 2MINUS reference")
    else:
        print("*** simple_expression : reference 2MINUS")

#def p_expression_multi_assig(p):
#    "simple_expression : '(' multi_assig ')'"
#    print("*** simple_expression : ( multi_assig )")

def p_expression_cast(p):
    "simple_expression : cast simple_expression"
    print("*** simple_expression : cast simple_expression")

#Cast
def p_cast_bool(p):
    "cast : '(' BOOL ')'"
    print("*** cast : ( BOOL )")

def p_cast_char(p):
    "cast : '(' CHAR ')'"
    print("*** cast : ( CHAR )")

def p_cast_float(p):
    "cast : '(' FLOAT ')'"
    print("*** cast : ( FLOAT )")

def p_cast_int(p):
    "cast : '(' INT ')'"
    print("*** cast : ( INT )")

def p_cast_string(p):
    "cast : '(' STRING ')'"
    print("*** cast : ( STRING )")

def p_cast_classname(p):
    "cast : '(' CLASSNAME ')'"
    print("*** cast : ( CLASSNAME )")

#reference
def p_reference1(p):
    "reference : ID_DOT reference"
    print("*** reference : ID_DOT reference")

def p_reference2(p):
    "reference : ID"
    print("*** reference : ID")


##page 388
#ConstrDecl
#def p_constr_decl(p):
#    '''constr_decl : CLASSNAME_DOT CLASSNAME_LP args ';' '''
#    print("*** constr_decl : CLASSNAME_DOT CLASSNAME_LP args SEMICOL")

#ClassDecl
def p_class_decl(p):
    '''class_decl : CLASS ID inherit ';' '''
    print("*** class_decl : CLASS ID inherit ;",)

#ClassDef
#def p_class_def(p):
#    '''class_def : CLASS ID inherit '{' class_body
#                 | CLASS CLASSNAME inherit '{' class_body'''
#    if(len(p) == 6):
#        print("*** class_def : CLASS ID inherit { class_body")
#    else:
#        print("*** class_def : CLASS CLASSNAME inherit { class_body")

#Inherit
def p_inherit(p):
    '''inherit : EXTENDS CLASSNAME
              | '' '''
    if(len(p) == 3):
        print("*** inherit : EXTENDS CLASSNAME")
    else:
        print("*** inherit : '' ")

#ClassBody
#def p_class_body(p):
#    '''class_body : class_member class_body
#                  | '}' '''
#    if(len(p)==2):
#        print("*** class_body : }")
#    else:
#        print("*** class_body : class_member class_body")

#ClassMember
#def p_class_member1(p):
#    "class_member : method_def"
#    print("*** class_member : method_def")

#def p_class_member2(p):
#    "class_member : constr_def"
#    print("*** class_member : constr_def")

#def p_class_member3(p):
#    "class_member : attr_multi_def"
#    print("*** class_member : attr_multi_def")

#DataType
def p_data_type1(p):
    "data_type : BOOL array_dim"
    print("*** data_type : BOOL array_dim")

def p_data_type2(p):
    "data_type : CHAR array_dim"
    print("*** data_type : CHAR array_dim")

def p_data_type3(p):
    "data_type : FLOAT array_dim"
    print("*** data_type : FLOAT array_dim")

def p_data_type4(p):
    "data_type : INT array_dim"
    print("*** data_type : INT array_dim")

def p_data_type5(p):
    "data_type : STRING array_dim"
    print("*** data_type : STRING array_dim")

def p_data_type6(p):
    "data_type : CLASSNAME array_dim"
    print("*** data_type : CLASSNAME array_dim")

#ArrayDim
def p_array_dim(p):
    '''array_dim : '[' ']' array_dim
                 | '' '''
    if(len(p) == 1):
        print("*** array_dim : '' ")
    else:
        print("*** array_dim : [ ] array_dim")

#AccessSpecifier
def p_access_specifier(p):
    '''access_specifier : PUBLIC
                        | PRIVATE'''
    if(p[1] == "public"):
        print("*** access_specifier : PUBLIC")
    else:
        print("*** access_specifier : PRIVATE")

#Prefix
def p_prefix(p):
    '''prefix : access_specifier SHARED CONST
              | access_specifier CONST SHARED
              | SHARED access_specifier CONST
              | SHARED CONST access_specifier
              | CONST access_specifier SHARED
              | CONST SHARED access_specifier
              | access_specifier SHARED
              | SHARED access_specifier
              | access_specifier CONST
              | CONST access_specifier
              | access_specifier
              | SHARED
              | CONST
              | '' '''
    if(len(p) == 2):
        if(p[1] == "const"):
            print("*** prefix : CONST")
        elif(p[1] == "shared"):
            print("*** prefix : SHARED")
        elif(p[1] == ''):
            print("*** prefix : '' ")
        else:
            print("*** prefix : access_specifier")
    elif(len(p) == 3):
        if(p[1] == "const"):
            print("*** prefix : CONST access_specifier")
        elif(p[1] == "shared"):
            print("*** prefix : SHARED access_specifier")
        else:
            print("*** prefix : access_specifier CONST")
    else:
        if(p[2] == "shared" and p[3] == "const"):
            print("*** prefix : access_specifier SHARED CONST")
        elif(p[2] == "const" and p[3] == "shared"):
            print("*** prefix : access_specifier CONST SHARED")
        elif(p[1] == "shared" and p[3] == "const"):
            print("*** prefix : SHARED access_specifier CONST")
        elif(p[1] == "shared" and p[2] == "const"):
            print("*** prefix : SHARED CONST access_specifier")
        elif(p[1] == "const" and p[3] == "shared"):
            print("*** prefix : CONST access_specifier SHARED")
        elif(p[1] == "const" and p[2] == "shared"):
            print("*** prefix : CONST SHARED access_specifier")

#page 389

    
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
  
Parser('prog.pan')

