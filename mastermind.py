import random

def generate_number(length):
    """Generates a random number with the given length."""
    return ''.join(random.choices('0123456789', k=length))

def get_feedback(secret, guess):
    """Provides feedback on the guessed number."""
    correct_positions = sum(1 for s, g in zip(secret, guess) if s == g)
    correct_digits = sum(min(secret.count(digit), guess.count(digit)) for digit in set(guess))
    return correct_positions, correct_digits - correct_positions

def play_game():
    length = 2 # Length of the number to guess
    secret_number = generate_number(length)
    attempts = 0

    print("Player 1 has set a secret number.")
    print("Player 2, start guessing!")

    while True:
        guess = input("Enter your guess: ")
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break
        else:
            correct_positions, correct_digits = get_feedback(secret_number, guess)
            print(f"Correct positions: {correct_positions}, Correct digits (wrong positions): {correct_digits}")

    return attempts

def main():
    print("Welcome to the Mastermind Game!")
    print("Player 1 will set a secret number, and Player 2 will try to guess it.")
    print("After Player 2 guesses correctly, the roles will switch.")

    print("\nRound 1: Player 2 guessing Player 1's number")
    player2_attempts = play_game()

    print("\nRound 2: Player 1 guessing Player 2's number")
    player1_attempts = play_game()

    if player1_attempts < player2_attempts:
        print("\nPlayer 1 wins and is crowned Mastermind!")
    elif player1_attempts > player2_attempts:
        print("\nPlayer 2 wins and is crowned Mastermind!")
    else:
        print("\nIt's a tie! Both players are equally good!")

if __name__ == "__main__":
    main()
