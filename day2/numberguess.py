import random

random_number = random.randint(10, 20)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Try to guess the number between 10 and 20 (inclusive).\n")

while True:
    try:
        guess = int(input("Your guess: "))
        attempts += 1
        
        if guess == random_number:
            print(f"\n🎉 Excellent! You guessed it in {attempts} {'try' if attempts == 1 else 'tries'}!")
            break
        elif guess < 10 or guess > 20:
            print("Please enter a number between 10 and 20")
        elif guess < random_number:
            print("Try a higher number")
        else:
            print("Try a lower number")
            
    except ValueError:
        print("⚠️ Please enter a valid number!")
        continue

print("\nThanks for playing!")