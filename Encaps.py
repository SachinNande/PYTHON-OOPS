#Encapsulation

class Account:
    actno = 123456789
    bal  = 0.0
    print("Old Bal    : ",bal)
    def getBal(self):
        return self.bal
    
    def setBal(self,bal):
        self.bal=bal

class Transaction:
    def Deposit(self,amt,object):
        if(amt>0):
            b1 = object.getBal()
            b1=b1+amt
            object.setBal(b1)
            print("Curren Bal : ",b1)
            
        else:
            print("invalid amount..")

class Encapsulation:
     a1= Account()
     ts = Transaction()
     ts.Deposit(500,a1)
     ts.Deposit(-22,a1)

