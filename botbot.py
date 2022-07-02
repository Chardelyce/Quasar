
from sly import Lexer 
from sly import Parser
from termcolor import colored

""" 
 .::::::.    ...    :::  :::.     .::::::.   :::.    :::::::..   
,;;'```';;,  ;;     ;;;  ;;`;;   ;;;`    `   ;;`;;   ;;;;``;;;;  
[[[     [[[\[['     [[[ ,[[ '[[, '[==/[[[[, ,[[ '[[,  [[[,/[[['  
"$$c  cc$$$"$$      $$$c$$$cc$$$c  '''    $c$$$cc$$$c $$$$$$c    
 "*8bo,Y88b,88    .d888 888   888,88b    dP 888   888,888b "88bo,
   "*YP" "M" "YmmMMMM"" YMM   ""`  "YMmMY"  YMM   ""` MMMM   "W" 
            
            "the most basic programming language 
            if you have a very limited keyboard"
                            
                created by: Chardleyce Edwards  
 """

class Protons(Lexer):
    tokens = { NAME, NUMBER, STRING, FLOAT, INT}
    ignore = '\t '
    literals = { '=', '+', '-', '/', 
                '*', '(', ')', ',', ';'}
  
    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return tokens(INT, int(num_str))
        else:
            return tokens(FLOAT, float(num_str))
    
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
  
    
    @_(r'\d+')
    def NUMBER(self, t):
        
        
        t.value = int(t.value) 
        return t
  
    
    @_(r'//.*')
    def COMMENT(self, t):
        pass
  
  
    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')

#parser class 
class Neutron(Parser):

    tokens = Protons.tokens
  
    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
    )
  
    def __init__(self):
        self.env = { }
  
    @_('')
    def statement(self, p):
        pass
  
    @_('var_assign')
    def statement(self, p):
        return p.var_assign
  
    @_('NAME "=" expr')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.expr)
  
    @_('NAME "=" STRING')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.STRING)
  
    @_('expr')
    def statement(self, p):
        return (p.expr)
  
    @_('expr "+" expr')
    def expr(self, p):
        return ('add', p.expr0, p.expr1)
  
    @_('expr "-" expr')
    def expr(self, p):
        return ('sub', p.expr0, p.expr1)
  
    @_('expr "*" expr')
    def expr(self, p):
        return ('mul', p.expr0, p.expr1)
  
    @_('expr "/" expr')
    def expr(self, p):
        return ('div', p.expr0, p.expr1)
  
    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return p.expr
  
    @_('NAME')
    def expr(self, p):
        return ('var', p.NAME)
  
    @_('NUMBER')
    def expr(self, p):
        return ('num', p.NUMBER)

#executing code 
class electron:
    def __init__(self, tree, env):
        self.env = env
        result = self.walkTree(tree)
        if result is not None and isinstance(result, int):
            print(result)
        if isinstance(result, str) and result[0] == '"':
            print(result)
  
    def walkTree(self, node):
  
        if isinstance(node, int):
            return node
        if isinstance(node, str):
            return node
  
        if node is None:
            return None
  
        if node[0] == 'program':
            if node[1] == None:
                self.walkTree(node[2])
            else:
                self.walkTree(node[1])
                self.walkTree(node[2])
  
        if node[0] == 'num':
            return node[1]
  
        if node[0] == 'str':
            return node[1]
  
        if node[0] == 'add':
            return self.walkTree(node[1]) + self.walkTree(node[2])
        elif node[0] == 'sub':
            return self.walkTree(node[1]) - self.walkTree(node[2])
        elif node[0] == 'mul':
            return self.walkTree(node[1]) * self.walkTree(node[2])
        elif node[0] == 'div':
            return self.walkTree(node[1]) / self.walkTree(node[2])
  
        if node[0] == 'var_assign':
            self.env[node[1]] = self.walkTree(node[2])
            return node[1]
  
        if node[0] == 'var':
            try:
                return self.env[node[1]]
            except LookupError:
                print( colored ("Undefined variable '"+node[1]+"' found!",'green'))
                return 0


#displaying to term


if __name__ == '__main__':
    lexer = Protons()
    parser = Neutron()
print (colored('      • Quasar                       ', 'red'))
print('                           ')
print (colored('"The most basic programming language' , 'yellow'))
print (colored('if you have a very limited keyboard"', 'yellow'))
print('                           ')
print (colored('chardelyce edwards 2022', 'blue'))
print (colored('https://github.com/chardelyce/Quasar', 'blue'))
print('--------------------------------')


env = {}
      
while True:
          
        try:
            text = input(colored('Quasar ⚛ ', 'red'))
          
        except EOFError:
            break
          
        if text:
            tree = parser.parse(lexer.tokenize(text))
            electron(tree, env)





