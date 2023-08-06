#1
class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        print((self.x**2)+(self.y**2)+(self.z**2))
    
obj=Point(1,3,5)
obj.sqSum()


#2
class Calculator:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print(self.num1+self.num2)
    def subtract(self):
        if self.num1>self.num2:
            print(self.num1-self.num2)
        else:
            print(self.num2-self.num1)
    def multiply(self):
        print(self.num1*self.num2)
    def divide(self):
        if self.num1>self.num2:
            print(self.num1/self.num2)
        else:
            print(self.num2/self.num1)

obj=Calculator(10,94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()


#3
class Student:
    def setName(self,x):
        self.__name=x
    def getName(self):
        print(self.__name)
    def setRollnumber(self,y):
        self.__rollNumber=y
    def getRollnumber(self):
        print(self.__rollNumber)

obj=Student()
obj.setName("Hemil")
obj.getName()
obj.setRollnumber(12)
obj.getRollnumber()


#4
class Account:
    def __init__(self,title,balance):
        self.title=title
        self.balance=balance

class SavingsAccount(Account):
    
    def __init__(self,title,balance,interestRate):
        super().__init__(title,balance)
        self.interestRate=interestRate

obj=Account("Hemil Shah",2000)
obj1=SavingsAccount("Hemil",5000,7)
print(obj.title)
print(obj.balance)
print(obj1.title)
print(obj1.balance)
print(obj1.interestRate)

#5
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance=self.balance-amount
        return self.balance

    def deposit(self, amount):
        self.balance=self.balance+amount
        return self.balance

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        a=self.balance*self.interestRate//100
        return a


obj=SavingsAccount("Hemil",2000,5)
print(obj.interestAmount())
obj.deposit(500)
print(obj.getBalance())
obj.withdrawal(200)
print(obj.getBalance())
