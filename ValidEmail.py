class ValidEmail:
    def __init__(self,name):
        self.name = name
    
    def __get__(self,instance):
        if isinstance is None:
            return self
        return instance.__dict__[self.name]
    
    def __set__(self,new_val,instance):

        if instance is None:
            return self
        
        if isinstance(new_val,str):
            if new_val.endswith("@gmail.com") or new_val.endswith("@mail.ru") or new_val.endswith("@icloud.com"):
                if new_val.count('.') == 1 and new_val.count('@') == 1 and new_val[0] != '.' and new_val[-1] != '.':
                    instance.__dict__[self.name] = new_val
                else:
                    raise ValueError("Email must contain only 1 @, '.' and must not start with .")
            else:
                raise ValueError("You have got a wrong domain")
        else:
            raise TypeError("Email must be str")
        
    def __delete__(self,instance):
        del instance.__dict__[self.name]