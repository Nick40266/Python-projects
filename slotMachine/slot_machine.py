import random

# ---------------------------------
# CONSTANTS
# ---------------------------------
ROWS = 3
COLS = 3
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 1000

symbol_counts = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# higher value = rarer symbol
symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# ---------------------------------
# MAIN PROGRAM
# ---------------------------------
def main():
    balance = deposit_money()

    lines = get_number_of_lines()

    bet = get_bet(lines, balance)

    reels = spin_slot_machine()

    print_slot_machine(reels)

    winnings = check_winnings(reels, lines, bet)

    balance = balance - (bet * lines) + winnings

    print(f"\nYou won: ${winnings}")
    print(f"Final balance: ${balance}")


# ---------------------------------
# FUNCTIONS
# ---------------------------------
def deposit_money():
    while True:
        try:
            deposit = int(input("What would you like to deposit? $"))
        except ValueError:
            print("Please enter a number")
            continue

        if deposit > 0:
            return deposit
        else:
            print("Amount must be greater than zero")


def get_number_of_lines():
    while True:
        try:
            lines = int(input(f"Enter the number of lines to bet on (1 - {MAX_LINES}): "))
        except ValueError:
            print("Please enter a number")
            continue

        if 1 <= lines <= MAX_LINES:
            return lines
        else:
            print("Number of lines out of range")


def get_bet(lines, balance):
    while True:
        try:
            bet = int(input(f"What would you like to bet on each line? (${MIN_BET} - ${MAX_BET}): $"))
        except ValueError:
            print("Please enter a number")
            continue

        total_bet = bet * lines

        if MIN_BET <= bet <= MAX_BET:
            if total_bet <= balance:
                print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")
                return bet
            else:
                print(f"Not enough balance. Current balance: ${balance}")
        else:
            print("Bet amount out of range")


def spin_slot_machine():
    symbols = []

    for symbol, count in symbol_counts.items():
        for _ in range(count):
            symbols.append(symbol)

    reels = []
    for _ in range(COLS):
        # ALLOW duplicates inside a column (realistic)
        column = random.choices(symbols, k=ROWS)
        reels.append(column)

    return reels


def print_slot_machine(reels):
    print("\nSPIN RESULT:")
    for row in range(ROWS):
        for col in range(COLS):
            print(reels[col][row], end=" | ")
        print()


def check_winnings(reels, lines, bet):
    winnings = 0

    for row in range(lines):
        first_symbol = reels[0][row]

        for col in range(1, COLS):
            if reels[col][row] != first_symbol:
                break
        else:
            winnings += bet * symbol_values[first_symbol]

    return winnings


# ---------------------------------
# PROGRAM ENTRY POINT
# ---------------------------------
if __name__ == "__main__":
    main()
