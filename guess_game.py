import random

print("⚔️ Welcome to the Viking Guessing Game ⚔️")
print("I am thinking of a number between 1 and 20.")

secret_number = random.randint(1, 20)
attempts = 0

while True:
    guess = input("Take a guess (or type 'q' to quit): ")

    if guess.lower() == "q":
        print("You fled the battlefield. The number was:", secret_number)
        break

    if not guess.isdigit():
        print("❌ Please enter a number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("⬆️ Too low!")
    elif guess > secret_number:
        print("⬇️ Too high!")
    else:
        print(f"🔥 Victory! You guessed it in {attempts} tries.")
        break
