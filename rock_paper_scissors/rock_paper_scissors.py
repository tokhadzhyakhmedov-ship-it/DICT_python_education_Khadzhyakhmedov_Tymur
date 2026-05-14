import random


def get_score(name):
    score = 0

    try:
        file = open("rating.txt", "r")
        for line in file:
            data = line.split()
            if data[0] == name:
                score = int(data[1])
                break
        file.close()
    except FileNotFoundError:
        score = 0

    return score


def get_options():
    print("Enter all your game symbols (full set of options):")
    options_input = input("> ")

    if options_input == "":
        return ["rock", "paper", "scissors"]
    else:
        return options_input.split(",")


def check_result(user_choice, computer_choice, options):
    if user_choice == computer_choice:
        return "draw"

    index = options.index(user_choice)
    new_options = options[index + 1:] + options[:index]
    half = len(new_options) // 2

    options_that_beat_user = new_options[:half]

    if computer_choice in options_that_beat_user:
        return "lose"
    else:
        return "win"


print("Enter your name:")
name = input("> ")
print(f"Hello, {name}")

score = get_score(name)

options = get_options()

print("Okay, let's start")

while True:
    print("Enter your current game symbol (move) or !exit for quit the program or !rating for your score displaying:")
    user_choice = input("> ")

    if user_choice == "!exit":
        print("Bye!")
        break

    elif user_choice == "!rating":
        print(f"Your rating: {score}")

    elif user_choice not in options:
        print("Invalid input")

    else:
        computer_choice = random.choice(options)
        result = check_result(user_choice, computer_choice, options)

        if result == "draw":
            print(f"There is a draw ({computer_choice})")
            score += 50

        elif result == "lose":
            print(f"Sorry, but the computer chose {computer_choice}")

        elif result == "win":
            print(f"Well done. The computer chose {computer_choice} and failed")
            score += 100