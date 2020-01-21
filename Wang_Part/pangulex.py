import ply.lex as lex
import sys

show_tokens = True

reserved = {
   'bool' : 'BOOL',
   'break' : 'BREAK',
   'catch' : 'CATCH',
   'char' : 'CHAR',
   'class' : 'CLASS',
   'const' : 'CONST',
   'continue' : 'CONTINUE',
   'else' : 'ELSE',
   'extends' : 'EXTENDS',
   'false' : 'FALSE',
   'float' : 'FLOAT',
   'goto' : 'GOTO',
   'ideof' : 'IDOF',
   'new' : 'NEW',
   'noref' : 'NOREF',
   'not' : 'NOT',
   'or'  : 'OR',
   'and' : 'AND',
   'for' : 'FOR',
   'mod' : 'MOD',
   'int' : 'INT',
   'if' : 'IF',
   'permanent' : 'PERMANENT',
   'return' : 'RETURN',
   'private' : 'PRIVATE',
   'public' : 'PUBLIC',
   'shared' : 'SHARED',
   'sizeof' : 'SIZEOF',
   'string' : 'STRING',
   'terminate' : 'TERMINATE',
   'throw' : 'THROW',
   'true' : 'TRUE',
   'try' : 'TRY',
   'typeof' : 'TYPEOF',
   'void' : 'VOID',
   'while' : 'WHILE'
}

def digit(a):
   if len(a) == 1 and a <= '9' and a >= '0':
      return True
   else:
      return False

def is_reserved(id):
   global reserved
   for i in reserved:
      if i == id:
         return True
   return False

tokens = [
   'ID',
   'CHAR_LIT',
   'DOT',
   'EQ',
   'FLOAT_LIT',
   'INT_LIT',
   'CLASSNAME',
   'CLASSNAME_DOT',
   'CLASSNAME_LP',
   'ID_DOT',
   'ID_LP',
   'ID_COLON',
   'GE',
   'LE',
   "2GT",
   'LT',
   'GT',
   '2LT',
   '2MINUS',
   'NE',
   'PASSIG',
   '2PLUS',
   'PRETURN',
   'STRING_LIT',
   'ERROR',
   'LINE_COMMENT',
   'MULTILINE_COMMENT',
   'MULTILINE_COMMENT_END'
]+list(reserved.values())
t_PASSIG  = r'@='
t_EQ     = r'=='
t_GE     = r'>='
t_LE     = r'<='
t_2GT    = r'>>'
t_2LT    = r'<<'
t_2MINUS = r'--'
t_NE     = r'!='
t_2PLUS  = r'\+\+'

literals = "=:,{}()[];+&*/%-<>"
t_ignore = " \t"

last_newline = 0

# Tokens

def t_STRING_LIT(t):
   r'\"([^\\\"]|\\\\|\\\"|\\n|\\/|\\\d+)*\"'
   global last_newline
   lexem = t.value
   t.value = t.value[1:-1]
   i = 0
   a = len(t.value)
   while i < a:
      if t.value[i] == '\\':
         if i+1 < a:
            if t.value[i+1] == '\\':                  # case \\
               i += 2
               continue
            elif t.value[i+1] == '"':                 # case \"
               i += 2
               continue
            elif t.value[i+1] == '#':                 # case \#
               i += 2
               continue
            elif t.value[i+1] == 'n':                 # case \n
               i += 2
               continue
            elif t.value[i+1] == '/':                 # case \/
               i += 2
               continue
            if digit(t.value[i+1]):                   # case \d
               if i+2 < a:
                  if digit(t.value[i+2]):             # case \dd
                     if i+3 < a:
                        if digit(t.value[i+3]):       # case \ddd
                           i += 4
                           continue
                        elif t.value[i+3] == '/':     # case \dd/
                           i += 4
                           continue
                        elif t.value[i+3] == '\\':    # case \dd\
                           i += 3
                           continue
                        else:                         # case \ddA
                           i += 4
                           continue
                     else:                            # case \dd$
                        i += 3
                        continue
                  elif t.value[i+2] == '/':           # case \d/
                     i += 3
                     continue
                  elif t.value[i+2] == '\\':          # case \d\
                     i += 2
                     continue
                  else:                               # case \dA
                     i += 3
                     continue
               else:                                  # case \d$
                  i += 2
                  continue
            else:                                     # case \A
               c1 = "incorrect escaped sequence in string"
               c2 = " (lineno={},pos={})".format(t.lineno,t.lexpos-last_newline)
               print(lexem,c1+c2)
               t.value = 'ERROR'
               return t
         else:                                        # case \$
            c1 = "incorrect escaped sequence in string"
            c2 = " (lineno={},pos={})".format(t.lineno,t.lexpos-last_newline)
            print(lexem,c1+c2)
            t.value = 'ERROR'
            return t
      else:                                           # case A
         i += 1
         continue
   #end while
   return t
#end t_STRING_LIT

def t_MULTILINE_COMMENT(t):
   r'\(\#(.|\n)*?\#\)'
   global last_newline
   ln = len(t.value)
   beg = lexer.lexpos-ln  # begenning of the comment
   for i in range(ln):
      if t.value[i] == '\n':
         t.lexer.lineno += 1
         last_newline = i

def t_LINE_COMMENT(t):
   r'\#(.)*\n'
   global last_newline
   t.lexer.lineno += 1
   last_newline = lexer.lexpos-1

def t_CHAR_LIT(t):
   r"'[^.]'|'\\n'|'\\\\'|'\\\d+'"
   global last_newline
   lexem = t.value
   t.value = t.value[1:-1]
   if t.value[0] == '\\' and t.value[1] == '0':
      if len(t.value) == 2:       #it is \0
         return t
      else:
         c1 = "character literal does not allow leading zeros"
         c2 = " (line={},pos={})".format(t.lineno,t.lexpos-last_newline)
         print(lexem,c1+c2)
         t.type = 'ERROR'
         return t
   elif t.value[0] == '\\' and t.value[1] >= '0' and t.value[1] <= '9':
      b = int(t.value[1:])
      if b > 255:
         c1 = "character literal must have values 0..255"
         c2 = " (line={},pos={})".format(t.lineno,t.lexpos-last_newline)
         print(lexem,c1+c2)
         t.type = 'ERROR'
         return t
      else:
         return t                 # it is \255
   else:
      return t                    # it is a or \n or \\


def t_ID_DOT(t):
   r'[a-zA-Z_][a-zA-Z-0-9]*\.'
   if is_reserved(t.value[:-1]):
      tok = lex.LexToken()
      tok.type = 'ERROR'
      tok.value = 'reserved word cannot be dotted'
      tok.lineno = t.lineno
      tok.lexpos = t.lexpos
      if show_tokens:
         print(tok)
      return tok
   else:
      if show_tokens:
         print(t)
      return t


def t_ID_LP(t):
   r'[a-zA-Z_][a-zA-Z-0-9]*[ ]*\('
   for i in range(len(t.value)):
      if t.value[i] == ' ' or t.value[i] == '(':
         x = i
         break
   id = t.value[:x]
   if is_reserved(id):
      lexer.lexpos = t.lexpos + len(id)
      t.type = reserved.get(id)
      t.value = id
   return t

def t_ID_COLON(t):
   r'[a-zA-Z_][a-zA-Z-0-9]*[ ]*\:'
   for i in range(len(t.value)):
      if t.value[i] == ' ' or t.value[i] == ':':
         x = i
         break
   id = t.value[:x]
   if is_reserved(id):
      lexer.lexpos = t.lexpos + len(id)
      t.type = reserved.get(id)
      t.value = id
      return t
   a = symtab_lookup(id,1)
   if a == 'CLASSNAME':
      c1 = id+" is a name of a class"
      c2 = " (lineno={},pos={})".format(t.lineno,t.lexpos)
      print(t.value,c1+c2)
      t.type = 'ERROR'
      return t
   return t

def t_ID(t):
   r'[a-zA-Z_][a-zA-Z-0-9]*'
   t.type = reserved.get(t.value,'ID')
   if show_tokens:
      print(t)
   return t

def strcmp(s1,s2,a):
   for i in range(a):
      if s1[i] == s2[i]:
         continue
      return int(s1[i])-int(s2[i])
   return 0

# range Â±2.23e+10^-308 to Â±1.79e+10^308
def t_FLOAT_LIT(t):
   r'\d*\.\d*'
   global last_newline
   lexem = t.value
   a = len(t.value)
   if a == 1:
      c1 = "float literal cannot have leading zeros"
      c2 = " (line={},pos={})".format(t.lineno,t.lexpos-last_newline)
      print(lexem,c1+c2)
      t.type = 'ERROR'
      if show_tokens:
         print(t)
      return t
   #find decimal point
   for i in range(len(t.value)):
      if t.value[i] == '.':
         dot = i
   if dot == 0:
      left = '0'
   else:
      left = t.value[:dot]
   if dot == a-1:
      right = '0'
   else:
      right = t.value[dot+1:]
   if left[0] == '0' and len(left) > 1:
      c1 = "float literal cannot have leading zeros"
      c2 = " (line={},pos={})".format(t.lineno,t.lexpos-last_newline)
      print(lexem,c1+c2)
      t.type = 'ERROR'
      if show_tokens:
         print(t)
      return t
   x = float(left+'.'+right)
   if x < 2.23e-308:
      c1 = 'float literal too small'
      c2 = ' (lineno={},pos={})'.format(t.lineno,t.lexpos-last_newline)
      print(lexem,c1+c2)
      t.type = 'ERROR'
      if show_tokens:
         print(t)
      return t
   if x > 1.79e+308:
      c1 = 'float literal too big'
      c2 = ' (lineno={},pos={})'.format(t.lineno,t.lexpos-last_newline)
      print(lexem,c1+c2)
      t.type = 'ERROR'
      if show_tokens:
         print(t)
      return t
   t.value = float(left+'.'+right)
   if show_tokens:
      print(t)
   return t

def t_INT_LIT(t):
   r'\d+'
   global last_newline
   lexem = t.value
   b = len(t.value)
   if b > 1:
      if t.value[0] == '0' and t.value[1] == '0':
         c1 = "int literal cannot have leading zeros"
         c2 = " (line={},pos={})".format(t.lineno,t.lexpos-last_newline)
         print(lexem,c1+c2)
         t.type = 'ERROR'
         if show_tokens:
            print(t)
         return t
   if b > 19:
      c1 = "int literal too long"
      c2 = " (line={},pos={})".format(t.lineno,t.lexpos-last_newline)
      print(lexem,c1+c2)
      t.type = 'ERROR'
      if show_tokens:
         print(t)
      return t
   if b == 19:
      if strcmp(t.value,'9223372036854775807',b) > 0:
         c1 = "int literal too big"
         c2 = " (line={},pos={})".format(t.lineno,t.lexpos-last_newline)
         print(lexem,c1+c2)
         t.type = 'ERROR'
         if show_tokens:
            print(t)
         return t
   t.value = int(t.value)
   if show_tokens:
      print(t)
   return t


def t_newline(t):
    r'\n+'
    global last_newline
    t.lexer.lineno += t.value.count("\n")
    last_newline = lexer.lexpos-1
    if show_tokens:
       print("newline")

def t_PRETURN(t):
   r'@return'
   return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
