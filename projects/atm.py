balance=10000
def check_balance():
    print("your balance is:",balance)

def deposit():
    global balance

    amount=int(input("enter the deposit amount:"))
    if amount>0:
        balance=balance+amount
        print("successfully deposit amount")
        print("total_amount is:",balance)
    else:
        print("enter invalid amount")

def withdraw():
    global balance

    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Enter a valid amount")

    elif amount <= balance:
        balance = balance - amount
        print("Please collect your cash")
        print("Remaining balance:", balance)

    else:
        print("Insufficient balance")


def atm_menu():

    while True:

        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()

        elif choice == 2:
            deposit()

        elif choice == 3:
            withdraw()

        elif choice == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")


atm_menu()


