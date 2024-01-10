from typing import Literal



class FastDB():
    
    def __init__(self,name,dbtype:Literal['sql','nosql']):
        self.name  = name
        self.dbtype = dbtype