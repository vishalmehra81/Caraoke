class Guest:
    def __init__(self,name,age,wallet):
        self.name = name
        self.age = age
        self.wallet = wallet


    def entry_fee(self,amount):
        self.wallet -= amount
