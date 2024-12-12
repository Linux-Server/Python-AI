class Bank:
    # class attributes
    name:str="State Bank Of India"
    balance:int=0
    
    def __init__(self,name:str,balance:int=0) -> None:
        self.name = name
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        Bank.balance += 10
        
    def withdraw(self,amount):
        self.balance -= amount
        Bank.balance += 10
        
        

acc_one = Bank(name="sam")
acc_one.deposit(100)
print("Acc one: ", acc_one.balance)
print("Bank bala: ", Bank.balance)
acc_one.withdraw(99)
print("Acc one: ", acc_one.balance)
print("Bank bala: ", Bank.balance)

        
        
    
    