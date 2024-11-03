import random

NUM_ROUNDS = 5

def get_user_choice():
    """Prompt user to guess if their number is higher or lower than the computer's."""
    while True:
        user_choice = input("Do you think your number is higher or lower than the computer's? (Enter 'higher' or 'lower'): ").strip().lower()
        if user_choice in ["higher", "lower"]:
            return user_choice
        print("Invalid choice! Please enter 'higher' or 'lower'.")

def play_round():
    """Play a single round of the High-Low game and return whether the guess was correct."""
    player_num = random.randint(1, 100)
    computer_num = random.randint(1, 100)
    
    print(f"Your number is {player_num}")
    user_choice = get_user_choice()
    
    if (user_choice == "higher" and player_num > computer_num) or (user_choice == "lower" and player_num < computer_num):
        print(f"You were right! The computer's number was {computer_num}")
        return True
    elif player_num == computer_num:
        print(f"It's a tie! The computer's number was also {computer_num}. Computer wins this round.")
        return False
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_num}")
        return False

def play_game():
    """Run the High-Low game for multiple rounds, tracking score and providing feedback."""
    score = 0
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        if play_round():
            score += 1
        print(f"Your score is now {score}\n")
    
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Amazing! You got a perfect score!")
    elif score > NUM_ROUNDS / 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

play_game()
