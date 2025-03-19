class NullBalance:
    def init(self, email, balance=0):
        self.email = email  
        self._balance = max(0, balance) 
    
    def balance(self):
        return self._balance  
    
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Bu hisobda hech qanday muammo")
        self._balance = amount 
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Bu hisobda hechqanday muammo yoq")
        self._balance += amount  
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Bu hisobda hech qanday muammo")
        if amount > self._balance:
            raise ValueError("Bu hisobda NullBalance muammosi ma")
        self._balance -= amount 

    @staticmethod
    def check_null_balance(description):
        if description is None:
            return False
        return "NullBalance" in description

sample_description1 = "Bu hisobda NullBalance muammosi ma"
sample_description2 = "Bu hisobda hech qanday muammo "

print(NullBalance.check_null_balance(sample_description1))  
print(NullBalance.check_null_balance(sample_description2))  
print(NullBalance.check_null_balance(None))
