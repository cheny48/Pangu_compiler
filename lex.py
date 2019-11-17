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

<<<<<<< HEAD

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
=======
reserved = {
    'shared' : 'SHARED',
    'sizeof' : 'SIZEOF',
    'string' : 'STRING',
    'terminate' : 'TERMINATE',
    'throw' : 'THROW',
    'true' : 'TRUE',
    'try' : 'TRY',
    'typeof' : 'TYPEOF',
    'void' : 'VOID'
}

# AND symbol &
# ASSIG symbol =
# BOOL keyword bool
# BREAK keyword break
# CATCH keyword catch
# CHAR keyword char
# CHAR LIT char literal
# CLASS keyword class
# CLASSNAME identier that has been previously dened or declared
# as a name of a class
# CLASSNAME DOT CLASSANAME followed by .
# CLASSNAME LP CLASSANAME followed by (
# COLON symbol :
# COMMA symbol ,
# CONST keyword const
# CONTINUE keyword continue
# DOT symbol .
# ELSE keyword else
# EQ symbol ==
# EXTENDS keyword extends
# FALSE keyword false
# FLOAT keyword float
# FLOAT LIT float literal
# FOR LP keyword for followed by (
# GE symbol >=
# GOTO keyword goto
# GTGT symbol >>
# ID identier
def t_ID(t):
    r'\b(?!(while|if)\b)[a-zA-Z_][0-9a-zA-Z_]*\b'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t
# ID LP ID followed by (
# ID COLON ID followed by :
# IDOF keyword ideof
# IF LP keyword if followed by (
# INT keyword int
# INT LIT int literal
# LB symbol {
# LE symbol <=
# LP symbol (
# LS symbol [
# LT symbol <
# LTLT symbol <<
# MAIN LP keyword main followed by (
# MINUS symbol -
t_MINUS   = r'-'
# MINUSMINUS symbol --
# MOD symbol %
# NEQ symbol !=
# NEW keyword new
# NOREF keyword noref
# NOT symbol !
# OR symbol |
# PARENT DOT PARENT followed by .
# PARENT LP PARENT followed by (
# PASSIG symbol @=
# PEEKNOTELSE the lookahead token indicating that the next token is not ELSE
# PERM keyword permanent
# PLUS symbol +
t_PLUS    = r'\+'
# PLUSPLUS symbol ++
# PRETURN keyword @return
# PRIVATE keyword private
# PUBLIC keyword public
# RB symbol }
# RETURN keyword return
# RP symbol )
# RS symbol ]
t_RS = r'\]'
# SEPICOL symbol ;
t_SEPICOL = r';'
# SHARED keyword shared
t_SHARED = r'shared'
# SIZEOF keyword sizeof
t_SIZEOF = r'sizeof'
# SLASH symbol /
t_SLASH   = r'/'
# STAR symbol *
t_STAR    = r'\*'
# STRING keyword string
t_STRING = r'string'
# STRING LIT string literal
t_STRING_LIT = r'"(\.|[^"])*"'
# TERMINATE keyword terminate
t_TERMINATE = r'terminate'
# THROW keyword throw
t_THROW = r'throw'
# TRUE keyword true
t_TRUE = r'true'
# TRY keyword try
t_TRY = r'try'
# TYPEOF keyword typeof
t_TYPEOF = r'typeof'
# VOID keyword void
t_VOID = r'void'
# WHILE LP keyword while followed by (
t_WHILE_LP = r'while\('

>>>>>>> f25f8d75e6771f8efcb64aa9dd7822cff102883a


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
<<<<<<< HEAD
bool &
char p = "x"

class Boxes()
=======
  3 + 4 * 10 + -20 *2 
  try
  shared
  sizeof
  terminate
  throw
  true
  typeof
  void
  while(
  string adasd "while3+ !%@dalkjda*(&&)(><:?{4``10 <=> $^#&+()_=+"
>>>>>>> f25f8d75e6771f8efcb64aa9dd7822cff102883a
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
