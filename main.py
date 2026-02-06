MAX_LINES = 3


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

def get_number_of_lines():
        while True:
            lines = input("Enter the number of lines to bet on (1-A")
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