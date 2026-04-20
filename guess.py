import random

def get_attempts(level):
    if level == 1:
        return 10   # Easy
    elif level == 2:
        return 7    # Medium
    elif level == 3:
        return 5    # Hard
    else:
        return None


def play_game():
    print("\n Welcome to Number Guessing Game!")

    while True:
        print("\nSelect Difficulty:")
        print("1. Easy (1–50, 10 attempts)")
        print("2. Medium (1–100, 7 attempts)")
        print("3. Hard (1–200, 5 attempts)")

        try:
            level = int(input("Enter choice (1/2/3): "))
        except ValueError:
            print("⚠ Invalid input!")
            continue

        attempts = get_attempts(level)

        if attempts is None:
            print("Invalid choice!")
            continue

        # Range based on difficulty
        if level == 1:
            number = random.randint(1, 50)
        elif level == 2:
            number = random.randint(1, 100)
        else:
            number = random.randint(1, 200)

        print("\nGame Started!")

        for i in range(attempts):
            try:
                guess = int(input(f"Attempt {i+1}/{attempts}: Enter your guess: "))
            except ValueError:
                print("Enter a valid number!")
                continue

            if guess == number:
                print(f"Correct! You guessed it in {i+1} attempts.")
                break
            elif guess < number:
                print("Too low!")
            else:
                print("Too high!")
        else:
            print(f"Game Over! The number was {number}")

        # Replay option
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()