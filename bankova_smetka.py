class BankAccount:
    def __init__(self, accountNumber, owner, balance):
        self.accountNumber = accountNumber
        self.owner = owner
        self.balance = balance
    
    def Deposit(self, add):
        self.balance+= add
        print(f"New balance: {self.balance}")

    def Withdrawl(self, withdrawl):
        if withdrawl > self.balance:
            print("You are broke hahah")
        else:
            self.balance -= withdrawl
            print(f"New balance: {self.balance}")

    def BankFees(self):
        self.balance -= self.balance * 0.05
        print(f"Balance after bank fees: {self.balance}")

    def Display(self):
        print(f"Account NUmber: {self.accountNumber}")
        print(f"Account Name: {self.owner}")
        print(f"Account Balance: {self.balance}")

newAccount = BankAccount(2178514584, 'Mariq' , 2700)
newAccount.Withdrawl(300)
newAccount.Deposit(200)
newAccount.Display()    