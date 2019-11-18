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

# AND symbol &
t_AND     = r'&'
# ASSIG symbol =
t_ASSIGN  = r'='
# BOOL keyword bool
t_BOOL    = r'bool'
# BREAK keyword break
t_BREAK   = r'break'
# CATCH keyword catch
t_CATCH   = r'catch'
# CHAR keyword char
t_CHAR    = r'char'
#t_CHAR_LIT=  r'\"[a-zA-Z]{1}\"' Made with action code
# CHAR LIT char literal
def t_CHAR_LIT(t):
    r'\"[a-zA-Z]{1}\"'
    t.value = t.value[1]
    return t
# CLASS keyword class
t_CLASS   = r'class'
# CLASSNAME identier that has been previously dened or declared
# as a name of a class
t_CLASSNAME= r'[A-Z][a-zA-Z_0-9]*'
# CLASSNAME DOT CLASSANAME followed by .
t_CLASSNAME_DOT = r'\.'
# CLASSNAME LP CLASSANAME followed by (
t_CLASSNAME_LP  = r'\('
# COLON symbol :
t_COLON   = r':'
# COMMA symbol ,
t_COMMA   = r','
# CONST keyword const
t_CONST   = r'const'
# CONTINUE keyword continue
t_CONTINUE= r'continue'
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
t_IF_LP   = r'if\('
# INT keyword int
t_INT     = r'int'
# INT LIT int literal
def t_INT_LIT(t):
    r'\d+'
    t.value = int(t.value)
    return t
# LB symbol {
t_LB      = r'\{'
# LE symbol <=
t_LE      = r'<='
# LP symbol (
t_LP      = r'\('
# LS symbol [
t_LS      = r'\['
# LT symbol <
t_LT      = r'\<'
# LTLT symbol <<
t_LTLT    = r'\<\<'
# MAIN LP keyword main followed by (
t_MAIN_LP = r'main\('
# MINUS symbol -
t_MINUS   = r'-'
# MINUSMINUS symbol --
t_MINUSMINUS = r'--'
# MOD symbol %
t_MOD     = r'\%'
# NEQ symbol !=
t_NEQ     = r'!='
# NEW keyword new
t_NEW     = r'new'
# NOREF keyword noref
t_NOREF   = r'noref'
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
t_RP = r'\)'
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

# >>>>>>> f25f8d75e6771f8efcb64aa9dd7822cff102883a

reserved = {
    'bool'   : 'BOOL',
    'break'  : 'BREAK',
    'catch'  : 'CATCH',
    'char'   : 'CHAR',
    'class'  : 'CLASS',
    'const'  : 'CONST',
    'continue':'CONTINUE',
    'shared' : 'SHARED',
    'sizeof' : 'SIZEOF',
    'string' : 'STRING',
    'terminate' : 'TERMINATE',
    'throw' : 'THROW',
    'true' : 'TRUE',
    'try' : 'TRY',
    'typeof' : 'TYPEOF',
    'void' : 'VOID',
    'int' : 'INT',
    'new' : 'NEW',
    'noref' : 'NOREF'
}


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
  + -20 *2 5%2
  <=  if( 8+* ( mainly aif newly lynew ifa
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
