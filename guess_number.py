number = 10
count = 5
print("I'm thinking of a number...")
guess = int(input(f"What number am I thinking of? You get {count} guesses! "))
while guess != 'q' and count != 1:
    if guess == number:
        print("Congratulations! You guessed the right number.")
        guess = 'q'
    else:
        count -= 1
        guess = int(input(f"{count} guess(es) left, Try again! (or q to quit) "))
        