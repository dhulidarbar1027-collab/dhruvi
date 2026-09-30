import random

print("Welcome to Number Guessing Game!")

# Computer chooses a random number
number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < number:
        print("Hint: Try a higher number!")

    elif guess > number:
        print("Hint: Try a lower number!")

    else:
        print("Congratulations! You guessed the correct number.")
        print("Number of attempts:", attempts)
        break
