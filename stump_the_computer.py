import random

guess_list = []
number = int(input("Pick a number between 1 and 100, and we'll see if the computer can guess it. "))

while len(guess_list) < 5:
    computer_guess = random.randint(1, 100)
    print("The computer guessed {}.".format(computer_guess))
    if computer_guess == number:
        computer_guess = random.randint(1, 100)
        print("Computers are insane! It guessed the number. Game Over!")
        guess_list.append(computer_guess)
        print("It only took the darned thing {} tries." .format(len(guess_list)))
        break
    elif computer_guess > number:
        print("The computer's guess is too high.")
    else:
        print("The computer's guess is too low.")

    if abs(computer_guess - number) <= 5:
        print("But it was really close.")
    guess_list.append(computer_guess)

else:
    print("Too many tries. The computer loses. Yeah!")