class Account:
    def __init__(self,name,acc_no,):
        self.name = name
        self.acc_no = acc_no
        self.balance = 0

    def deposit(self):
        self.balance += float(input("Enter the amount you want to deposit : "))
        self.show_balance()
    
    def withdrawal(self):
        self.balance -= float(input("Enter the amount you want to widthraw : "))
        self.show_balance()

    def show_balance(self):
        print(f"Your current balance is : {self.balance}")


hasib = Account("Hasib",9874563210)
hasib.deposit()
hasib.withdrawal()
hasib.deposit()
hasib.withdrawal()
        