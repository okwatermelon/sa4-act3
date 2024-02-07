number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))
while guess != 'q':
    if guess == number:
        print("Congratulations! You guessed the right number.")
        guess = 'q'
    elif guess < number:
        guess = int(input("Too low, try again! (or q to quit) "))
    else:
        guess = int(input("Too high, try again! (or q to quit) "))
        