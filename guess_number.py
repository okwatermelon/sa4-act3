number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))
while guess != 'q':
    if guess == number:
        print("Congratulations! You guessed the right number.")
        guess = 'q'
    else:
        guess = int(input("Try again! (or q to quit) "))
        