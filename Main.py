class ATM:
    def __init__(self):
        self.data = []
        with open("numbers.csv", "r") as f:
            for line in f:
                values = line.strip().split(",")
                if values and values[0]: 
                    self.data.extend(map(int, values))
        self.login = False

    def password(self):
        self.num = int(input("\nenter your number: "))      
        found = False
        for i in range(0, len(self.data), 3):
            if self.data[i] == self.num:
                self.index = i
                found = True
                break
        if not found:
            print("invalid number")
            return 
        attempt = 0
        while attempt < 3:
            self.pin = int(input("\nenter your pin: "))
            if self.pin == self.data[self.index + 1]:
                print("logged in successfully")
                print("\n---------Welcome To The ATM----------------")
                self.login = True
                break
            else:
                attempt += 1
                print(f"wrong password, attempts left: {3 - attempt}")
                self.login = False
        if attempt == 3:
            print("account blocked!")

    def display(self):
        print("\n-----MENU-----")
        print("1. check balance")
        print("2. deposit money")
        print("3. withdraw money")
        print("4. change pin")
        print("5. Exit")

    def check_balance(self):
        print(f"\nYour current balance is: {self.data[self.index + 2]}")

    def deposit(self):
        self.amount = int(input("enter your amount: "))
        if self.amount < 0 :
            print("error: amount must be positive: ")
        else:
            self.data[self.index + 2] += self.amount
            print(f"deposit successful: updated balance is {self.data[self.index + 2]} ")
            self.save_balance()

    def withdraw(self):
        self.amount = int(input("enter your amount: "))
        if self.amount < 0 :
            print("error: amount must be positive: ")
        else:
            self.data[self.index + 2] -= self.amount
            print(f"withdrawal successful , available balance is {self.data[self.index + 2]}")
            self.save_balance()
        
    def change_password(self):
        old_pin = int(input("enter old pin: "))

        if old_pin == self.data[self.index + 1]:
            new_pin = int(input("enter new pin: "))
            self.data[self.index + 1] = new_pin
            self.save_balance()
            print("password change successful")
        else:
            print("invalid pin. please try again")

    def exit(self):
        print("thank you for using Atm.")

    def save_balance(self):
        with open("numbers.csv", "w") as f:
            for i in range(0, len(self.data), 3):
                chunk = self.data[i:i+3]
                f.write(",".join(map(str, chunk)) + "\n")

    def run(self):
        self.password()

        if not self.login:
            return
        
        while self.login:
            self.display()

            choice = input("enter your choice(1-5): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.change_password()
            elif choice == "5":
                self.exit()
                break
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
atm = ATM()
atm.run()    