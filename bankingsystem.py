class Bank:
    minimum_balance = 1000
    
    def __init__(self,name,age,phone,balance):

      self.name = name
      self.age = age
      self.phone = phone
      self.balance = balance

#object methods
    def withdrawmoney(self,amount):
      if self.balance - amount >= Bank.minimum_balance:
        self.balance-=amount
        print(f"withdrawn {amount}.remaining balance {self.balance}")
      else:
        print("withdrawal failed\n minimum balance required")
    def depositmoney(self,amount):
     self.balance+=amount
     print(f"deposited money {amount}.new balance {self.balance}")
    def displaymoney(self):
     print(self.name,self.phone,self.balance)
#class method
    @classmethod
    def updateminbalance(cls,new_minimumbalance):
     cls.minimum_balance = new_minimumbalance
     print("minimum balance is updated to: ",cls.minimum_balance)
#creating objects
obj1 = Bank("srihita",'21','6281634676',50000)
obj2 = Bank("jahnavi",'18','6000346861',50500)
obj3 = Bank("jyothsna",'28','9581333374',60000)
obj4 = Bank("yashwitha",'25','904578674',50000)
obj5 = Bank("lalith",'20','9000868683',50000)
# calling functions
obj3.withdrawmoney(1000)
obj2.depositmoney(1000)
obj1.displaymoney()
Bank.updateminbalance(2000)
