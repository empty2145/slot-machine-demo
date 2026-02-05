def deposit():
    while True:
        amount = input("What amount would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero. Please try again.")
        else:
            print("Amount must be a number. Please try again.")
    return amount
def main():
    balance = deposit()

main()