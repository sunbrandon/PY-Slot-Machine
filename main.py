import random                                                           # import a random module, similar to #include in c++

MAX_LINES = 3                                                           # global const variable
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {                                                        # dictionary?
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {                                                        # dictionary?
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:                                                          # for-else loop, if for loop breaks else doesn't execute
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():                        # loop through dictionary item, ex. for "A", 2
        for _ in range(symbol_count):                                   # for (random variable) in 2
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]                                # colon in all_symbols means to copy into current_symbols
        for _ in range(rows):
            value = random.choice(current_symbols)                      # chooses random value from all_symbols list
            current_symbols.remove(value)                               # iterates in current_symbols and removes first instance of value parameter
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):                                  # len = length
        for i, column in enumerate(columns):
            if i != len(columns) - 1:                                   # checks if i reached the end of columns
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

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

def spin(balance):
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

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():                                                             # main function where program is called
    balance = deposit()                                                 # runs the deposit function and puts the value into variable "balance"
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()