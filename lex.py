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
# PLUSPLUS symbol ++
# PRETURN keyword @return
# PRIVATE keyword private
# PUBLIC keyword public
# RB symbol }
# RETURN keyword return
# RP symbol )
# RS symbol ]
# SEPICOL symbol ;
# SHARED keyword shared
# SIZEOF keyword sizeof
# Appendix B 387
# SLASH symbol /
# STAR symbol *
# STRING keyword string
# STRING LIT string literal
# TERMINATE keyword terminate
# THROW keyword throw
# TRUE keyword true
# TRY keyword try
# TYPEOF keyword typeof
# VOID keyword void
# WHILE LP keyword while followed by (

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_STAR    = r'\*'
t_SLASH   = r'/'


# A regular expression rule with some action code
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
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
3 + 4 * 10
  + -20 *2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
