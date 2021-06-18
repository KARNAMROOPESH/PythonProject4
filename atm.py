class Atm:
    def __init__(self,acc,pin,money , total , balance):
        self.acc = card
        self.pin = pincode
        self.money = amount  
        self.total = 10,000    
    def information(self):
        self.balance = balanceam
        balanceam1 = str(self.balance)
        print("Thanks for using RoopBank . As per now your Bank balance is " + balanceam1 )
        
print(" WELCOME TO ROOP BANK ")
card = input("Enter your Card number :")
pincode = input("Enter your Pin :")
print(" Current Balance : 10,000")
amount = int(input("Enter amount needed : "))
if(amount > 10000):
    print(" The amount u entered is not there in our account . Please eneter a value which can be withdrawn ")
    balanceam = 10000
else:
    balanceam = 10000-amount

AnyTimeMoney = Atm(card , pincode , amount , 10000 , balanceam)
AnyTimeMoney.information()