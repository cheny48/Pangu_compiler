import ply.lex as lex
# List of token names.   This is always required
tokens = (
    'AND',
    'ASSIGN',
    'BOOL',
    'BREAK',
    'CATCH',
    'CHAR',
    'CHAR_LIT',
    'CLASS',
    'CLASSNAME',
    'CLASSNAME_DOT',
    'CLASSNAME_LP',
    'COLON',
    'COMMA',
    'CONST',
    'CONTINUE',
    'DOT',
    'ELSE',
    'EQ',
    'EXTENDS',
    'FALSE',
    'FLOAT',
    'FLOAT_LIT',
    'FOR_LP',
    'GE',
    'GOTO',
    'GTGT',
    'ID',
    'ID_LP',
    'ID_COLON',
    'IDOF',
    'IF_LP',
    'INT',
    'INT_LIT',
    'LB',
    'LE',
    'LP',
    'LS',
    'LT',
    'LTLT',
    'MAIN_LP',
    'MINUS',
    'MINUSMINUS',
    'MOD',
    'NEQ',
    'NEW',
    'NOREF',
    'NOT',
    'OR',
    'PARENT_DOT',
    'PARENT_LP',
    'PASSIG',
    'PEEKNOTELSE',
    'PERM',
    'PLUS',
    'PLUSPLUS',
    'PRETURN',
    'PRIVATE',
    'PUBLIC',
    'RB',
    'RETURN',
    'RP',
    'RS',
    'SEPICOL',
    'SHARED',
    'SIZEOF',
    'SLASH',
    'STAR',
    'STRING',
    'STRING_LIT',
    'TERMINATE',
    'THROW',
    'TRUE',
    'TRY',
    'TYPEOF',
    'VOID',
    'WHILE_LP'
)


# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_STAR    = r'\*'
t_SLASH   = r'/'
t_AND     = r'&'
t_ASSIGN  = r'='
t_BOOL    = r'bool'
t_BREAK   = r'break'
t_CATCH   = r'catch'
t_CHAR    = r'char'
#t_CHAR_LIT=  r'\"[a-zA-Z]{1}\"' Made with action code 
t_CLASS   = r'class'
t_CLASSNAME= r'[A-Z][a-zA-Z_0-9]*' 
t_CLASSNAME_DOT = r'\.'
t_CLASSNAME_LP  = r'\('
t_COLON   = r':'
t_COMMA   = r','
t_CONST   = r'const'
t_CONTINUE= r'continue'


# A regular expression rule with some action code
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_CHAR_LIT(t):
    r'\"[a-zA-Z]{1}\"'
    t.value = t.value[1]
    return t 

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
bool &
char p = "x"

class Boxes()
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
