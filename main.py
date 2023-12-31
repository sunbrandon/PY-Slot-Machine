
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