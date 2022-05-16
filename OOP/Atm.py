class Atm:

    def __init__(self):

        self.balance = 0
        self.pin = ""
        self.menu()
    
    def menu(self):
        choice = 0
        while (choice!=5):
            choice  = int(input("""
            1 - Create PIN
            2 - Deposit
            3 - Withdraw
            4 - Balance
            5 - Exit
            
            Enter a choice: """))

            if choice == 1:
                self.create_pin()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.withdraw()
            elif choice == 4:
                self.check_balance()
            elif choice == 5:
                break
            else:
                print("Enter a valid choice")

    def check_balance(self):
        temp = input("Enter a PIN: ")
        if temp == self.pin:
            print(f"Balance: {self.balance}")
        else:
            print("Invalid PIN")

    def deposit(self):
        temp = input("Enter a PIN: ")
        if temp == self.pin:
            amt = int(input("Enter the amt to be deposited: "))
            self.balance += amt 
            print(f"Balance after depositing: {self.balance}")
        else:
            print("Invalid PIN")

    def withdraw(self):
        temp = input("Enter a PIN: ")
        if temp == self.pin:
            amt = int(input("Enter the amt to be withdrawn: "))
            if amt <= self.balance:
                self.balance -= amt 
                print(f"Balance after withdrawing: {self.balance}")
            else:
                print("Insufficient Funds")
        else:
            print("Invalid PIN")

    def create_pin(self):
        self.pin = input("Enter a new PIN: ")