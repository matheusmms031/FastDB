class App():
    
    def app(self,func):
        
        def inner1(*args, **kwargs):
            self.funcs.append(func.__name__)
            print(func)
            return func(*args,**kwargs)
            
        return inner1 