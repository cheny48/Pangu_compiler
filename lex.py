import ply.lex as lex
from ply.lex import TOKEN
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
# as a name of a class
t_CLASSNAME= r'[A-Z][a-zA-Z_0-9]*'
# CLASSNAME DOT CLASSANAME followed by .
t_CLASSNAME_DOT = r'[A-Z][a-zA-Z_0-9]*\.'
# CLASSNAME LP CLASSANAME followed by (
t_CLASSNAME_LP  = r'[A-Z][a-zA-Z_0-9]*\('
# COLON symbol :
t_COLON   = r':'
# COMMA symbol ,
t_COMMA   = r','
# DOT symbol .
t_DOT     = r'\.'
# EQ symbol ==
t_EQ      = r'=='
# GE symbol >=
t_GE      = r'>='
# GTGT symbol >>
t_GTGT    = r'>>'
# IF LP keyword if followed by (
t_IF_LP   = r'if\('
# INT keyword int
t_INT     = r'int'
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
t_MAIN_LP = r'main'+ r'[ ]*' +r'\('
# FOR LP keyword for followed by (
t_FOR_LP = r'for\('
# MINUS symbol -
t_MINUS   = r'-'
# MINUSMINUS symbol --
t_MINUSMINUS = r'--'
# MOD symbol %
t_MOD     = r'\%'
# NEQ symbol !=
t_NEQ     = r'!='
# NOT symbol !
t_NOT   = r'\!'
# OR symbol |
t_OR    = r'\|'
# PARENT DOT PARENT followed by .
t_PARENT_DOT = r'parent.'
# PARENT LP PARENT followed by (
t_PARENT_LP = r'parent\('
# PASSIG symbol @=
t_PASSIG = r'@='
# PLUS symbol +
t_PLUS    = r'\+'
# PLUSPLUS symbol ++
t_PLUSPLUS = r'\+\+'
# PRETURN keyword @return
t_PRETURN = r'@return'
# RB symbol }
t_RB   = r'}'
# RP symbol )
t_RP   = r'\)'
# SEPICOL symbol ;
t_SEPICOL = r';'
# SLASH symbol /
t_SLASH   = r'/'
# STAR symbol *
t_STAR    = r'\*'
# STRING LIT string literal
t_STRING_LIT = r'"(\.|[^"])*"'
# WHILE LP keyword while followed by (
t_WHILE_LP = r'while\('

digit            = r'([0-9])'
nondigit         = r'([_A-Za-z])'
identifier       = r'((?!(while|if|parent | main |for|([a-zA-Z][0-9a-zA-Z]*[:\()]))\b)' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'
identifier_lp    = r'(' + identifier + r'\()'
identifier_colon = r'(' + identifier + r':)'
# CHAR LIT char literal
def t_CHAR_LIT(t):
    r'\"[a-zA-Z]{1}\"'
    t.value = t.value[1]
    return t
# FLOAT LIT float literal
# Numbers with a decimal point. No leading zeros or embedded spaces allowed.
# May miss the integer or fractional part, but not both
def t_FLOAT_LIT(t):
    r'[-\+]?(\.[0-9]+)|(0\.[0-9]*)|([1-9][0-9]*\.[0-9]*)'
    t.value = float(t.value)
    return t
# ID LP ID followed by (
@TOKEN(identifier_lp)
def t_ID_LP(t):
    return t
# # ID COLON ID followed by :
@TOKEN(identifier_colon)
def t_ID_COLON(t):
    return t
# ID
@TOKEN(identifier)
def t_ID(t):
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t
def t_INT_LIT(t):
    r'\d+'
    t.value = int(t.value)
    return t
# PEEKNOTELSE the lookahead token indicating that the next token is not ELSE
def t_PEEKNOTELSE(t):
    r'\b(?!(else)\b)\.+\b'
    return t

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
    'noref' : 'NOREF',
    'permanent' : 'PERM',
    'private' : 'PRIVATE',
    'public' : 'PUBLIC',
    'return' : 'RETURN',
    'else'      : 'ELSE',
    'extends'   : 'EXTENDS',
    'false'     : 'FALSE',
    'float'     : 'FLOAT',
    'goto'      : 'GOTO',
    'ideof'     : 'IDOF',
}


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
t_ignore_COMMENT = r'(/\*(.|\n)*?\*/)|(//.*)'

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
  f25f8d75e6771f8efcb64aa9dd7822cff102883a

    !+|+@= +
    ++ + } + permanent + ) + @return parent. @= parent( return
  . else == extends false float 3.2
  ==  for() >= goto >> x y x( y : ideof for3  er : 0. .0
  x: for(
'''

def tokenizer():
    file = open("source.pc","r")
    alldata = file.read()
    lexer.input(alldata)
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)
    file.close()

tokenizer()
