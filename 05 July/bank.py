class Account:
    def __init__(self,name,age,password,acc_no):
        self.name = name
        self.__balance = 0
        self.age = age 
        self.__password = password
        self.__acc_no = acc_no

    def show_balance(self,password):
        if self.__password == password:
            print(f"Your acc balance is {self.__balance}")
    
    def update_password(self,acc_no,new_pass):
        if acc_no == self.__acc_no:
            self.__password = new_pass

        
    
hasib = Account("Hasib Sir",55,12345)
