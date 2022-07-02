
from sly import Lexer 

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
    tokens = { NAME, NUMBER, STRING }
    ignore = '\t '
    literals = { '=', '+', '-', '/', 
                '*', '(', ')', ',', ';'}
  
  
    
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



print('      • Quasar                       ')
print('                           ')
print('"the most basic programming language')
print('if you have a very limited keyboard"')
print('                           ')
print('chardelyce edwards 2022')
print('https://github.com/chardelyce/Quasar')
print('--------------------------------')

