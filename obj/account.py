class Account():
    def __init__(self, name, money):
        self.name = name 
        self.money = money
        self.changes = 0
    
    def getName(self):
        return self.name
    
    #* POST request
    def setName(self, name):
        self.name = name
    
    def getMoney(self):
        return self.money  

    #* POST request
    def changeMoney(self, money):
        self.money += money
        self.changes += money
        return self.money  
    
    def setMoney(self, money):
        self.money = money
        return self.money
