import random

the_number = random.randint(1, 10)
guess_list = []


while len(guess_list) < 5:
    guess = int(input("Try to guess the secret number in 5 tries. It's between 1 and 100. "))
    if guess == the_number:
        print("Brilliance! You guessed it! Game Over!")
        guess_list.append(guess)
        print("It only took you {} tries." .format(len(guess_list)))
        break
    elif guess > the_number:
        print("Your guess is too high.")
        if (abs(guess - the_number <= 5)):
            print("But you were really close.")
    else:
        print("Your guess is too low.")
        if (abs(guess - the_number <= 5)):
            print("But you were really close.")
    guess_list.append(guess)

else:
    print("Too many tries. You lose.")