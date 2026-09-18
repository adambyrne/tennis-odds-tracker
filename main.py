# Tennis Odds Tracker

# Sample Tennis Matches (mock data)
matches = [
    {
        "id": 1,
        "player1": "Novak Djokovic",
        "player2": "Carlos Alcaraz",
        "odds_player1": 1.80,
        "odds_player2": 2.05
    },
    {
        "id": 2,
        "player1": "Jannik Sinner",
        "player2": "Daniil Medveddev",
        "odds_player1": 1.65,
        "odds_player2": 2.30
    },
    {
        "id": 3,
        "player1": "Taylor Fritz",
        "player2": "Alexander Zverev",
        "odds_player1": 2.10,
        "odds_player2": 1.72
    }
]

# List to store all bets placed
betting_history = []

# Function to display all matches
def display_matches():
    print("\n=== Tennis Matches ===\n")
    for match in matches:
        print(f"Match {match['id']}: {match['player1']} vs {match['player2']}")
        print(f" Odds - {match['player1']}: {match['odds_player1']} | {match['player2']}: {match['odds_player2']}")
        print()

# Function to calculate potential winnings
def calculate_winnings(match_id, bet_amount, player_choice):
    match = matches[match_id -1]

    if player_choice == 1:
        odds = match['odds_player1']
        player_name = match['player1']
    else:
        odds = match['odds_player2']
        player_name = match['player2']

    potential_winnings = bet_amount * odds
    profit = potential_winnings - bet_amount

    print(f"\n=== Bet Summary ===")
    print(f"Match {match_id}: {match['player1']} vs {match['player2']}")
    print(f"Betting on: {player_name}")
    print(f" Bet Amount: ${bet_amount}")
    print(f" Odds: {odds}")
    print(f" Potential Winnings: ${potential_winnings:.2f}")
    print(f" Profit: ${profit:.2f}\n")

# Function to track betting history
# This function should store bets in a list and display them
# Include: match, player bet on, bet amount, odds, status (pending/win/loss)

def add_to_history(match_id, player_choice, bet_amount):
    match = matches[match_id - 1]
    player_name = match['player1'] if player_choice == 1 else match['player2']
    odds = match['odds_player1'] if player_choice == 1 else match['odds_player2']

    bet_record = {
        "match": f"{match['player1']} vs {match['player2']}",
        "player_bet_on": player_name,
        "bet_amount": bet_amount,
        "odds": odds,
        "status": "pending"
    }

    betting_history.append(bet_record)

# Function to display all bets in history
def display_history():
    if not betting_history:
        print("\nNo bets placed yet.\n")
        return

    print("\n=== Betting History ===\n")
    for idx, bet in enumerate(betting_history, start=1):
        print(f"Bet {idx}:")
        print(f" Match: {bet['match']}")
        print(f" Player Bet On: {bet['player_bet_on']}")
        print(f" Bet Amount: ${bet['bet_amount']}")
        print(f" Odds: {bet['odds']}")
        print(f" Status: {bet['status']}\n")

# Main Program
print("=" * 40)
print("Welcome to Tennis Odds Tracker!")
print("=" * 40)

display_matches()

print("\noptions:")
print("1. Place a bet")
print("2. View betting history")
print("0. Exit\n")

# Get User Input
while True:
    try:
        user_choice = input("Enter your choice: ")

        if user_choice == "0":
            print("Thanks for using Tennis Odds tracker!")
            break

        if user_choice == "2":
            display_history()
            continue

        if user_choice == "1":
            match_id = int(input("Enter match number (1-3): "))

            if match_id < 1 or match_id > 3:
                print("Invalid match number. Please try again.\n")
                continue

            player_choice = int(input("Choose player to bet on (1 or 2): "))

            if player_choice not in [1, 2]:
                print("Invalid choice. Please enter 1 or 2.\n")
                continue

            bet_amount = float(input("Enter bet amount ($): "))

            if bet_amount <= 0:
                print("Bet amount must be greater than 0. Please try again.\n")
                continue

            calculate_winnings(match_id, bet_amount, player_choice)
            add_to_history(match_id, player_choice, bet_amount)
        else:
            print("Invalid choice. Please try again.\n")

    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
