import random
random_number = random.randint(0,20)
no_of_guess = 0
print("Welcome to the number guessing game.")
game_start=0
game_limit=3
while game_start<game_limit:
    print(3-game_start)
    game_start+=1
print("Game Started.")
while no_of_guess<game_limit:
    guess = int(input("Guess a number from 0 to 20 :\n"))
    if guess == random_number:
        print(f"Congratulations! Your guess {guess} is right.")
        break
    elif no_of_guess == game_limit-1:
        print(f"you didn't guess it right.")
        print("Try again!")
    elif guess > random_number:
        print(f"your guess {guess} is greater, try guessing smaller one.")
    elif guess < random_number:
        print(f"your guess {guess} is smaller, try guessing greater one.")
    no_of_guess+=1
