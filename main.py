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

# Main Program
print("=" * 40)
print("Welcome to Tennis Odds Tracker!")
print("=" * 40)

display_matches()

# Get User Input
while True:
    try:
        match_id = int(input("Enter match number (1-3) or 0 to exit: "))

        if match_id == 0:
            print("Thanks for using Tennis Odds Tracker!")
            break

        if match_id < 1 or match_id > 3:
            print("Invalid match number. Please try again.\n")
            continue

        player_choice = int(input("Choose player (1 or 2): "))

        if player_choice not in [1, 2]:
            print("Invalid player choice. Please try again.\n")
            continue

        bet_amount = float(input("Enter bet amount ($):"))

        if bet_amount <= 0:
            print("Bet amount must be greater than 0. Please try again.\n")
            continue

        calculate_winnings(match_id, bet_amount, player_choice)

    except ValueError:
        print("Invalid input. Please enter a number.\n")
