MAX_LINES = 3                                                           # global const variable
MAX_BET = 100
MIN_BET = 1

def deposit():                                                          # def = function
    while True:                                                         # while loop checks if user input is valid, if not ask again
        amount = input("What would you like to deposit? $")             # amount = string variable asking for an input with prompt inside parenthesis
        if amount.isdigit():                                            # checks if amount is a valid number and not random chars
            amount = int(amount)                                        # converts amount into an integer from string if amount is a proper number
            if amount > 0:
                break                                                   # if input is greater than 0 break out of loop
            else:
                print("Amount must be greater than 0.")                 # if input not greater than 0 prompt user to input again
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:                                                     
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")  # prompt user to enter max num of lines and convert MAX_LINES into a string to be used in output msg
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:                                                    # checks if lines is between max and min number
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:                       
        amount = input("What would you like to bet on each line? $") 
        if amount.isdigit():    
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")                  # min and max bet are converted to strings by f string in py to be used in output
        else:
            print("Please enter a number.")

    return amount

def main():                                                             # main function where program is called
    balance = deposit()                                                 # runs the deposit function and puts the value into variable "balance"
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")


main()