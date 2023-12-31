MAX_LINES = 3                                                           # global const variable


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

def main():                                                             # main function where program is called
    balance = deposit()                                                 # runs the deposit function and puts the value into variable "balance"
    lines = get_number_of_lines()
    print(balance, lines)

main()