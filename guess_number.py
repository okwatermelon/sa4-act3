number = 10
count = 5
print("I'm thinking of a number...")
guess2 = input(f"What number am I thinking of? You get {count} guesses! ")
guess = int(guess2)
while count != 1 and guess2 != 'q':
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        count -= 1
        guess2 = input(f"Too low, {count} guess(es) left, Try again! (or q to quit) ")
        if guess2.isnumeric():
            guess = int(guess2)
    elif guess > number:
        count -= 1
        guess2 = input(f"Too high, {count} guess(es) left, Try again! (or q to quit) ")
        if guess2.isnumeric():
            guess = int(guess2)
if count == 1 or guess2 == 'q':
    print(f"The number was {number}, good luck next time!")