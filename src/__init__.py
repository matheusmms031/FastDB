from typing import Literal
from app import App


class FastDB(App):
    
    def __init__(self,name,dbtype:Literal['sql','nosql']):
        self.funcs = []
        self.name  = name
        self.dbtype = dbtype
        

teste = FastDB('Matheus','sql')
@teste.app
def soma(x,y):
    return x + y

print(soma(10,24))
print(teste.funcs)