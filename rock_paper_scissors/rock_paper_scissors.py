import random

print("Enter your name:")
name = input()
print(f"Hello, {name}")

score = 0

try:
    file = open("rating.txt", "r", encoding="utf-8")
    for line in file:
        data = line.split()
        if data[0] == name:
            score = int(data[1])
            break
    file.close()
except FileNotFoundError:
    score = 0

options_input = input()

if options_input == "":
    options = ["rock", "paper", "scissors"]
else:
    options = options_input.split(",")

print("Okay, let's start")

while True:
    user_choice = input()

    if user_choice == "!exit":
        print("Bye!")
        break

    elif user_choice == "!rating":
        print(f"Your rating: {score}")

    elif user_choice not in options:
        print("Invalid input")

    else:
        computer_choice = random.choice(options)

        if user_choice == computer_choice:
            print(f"There is a draw ({computer_choice})")
            score += 50
        else:
            index = options.index(user_choice)
            new_options = options[index + 1:] + options[:index]
            half = len(new_options) // 2

            options_that_beat_user = new_options[:half]

            if computer_choice in options_that_beat_user:
                print(f"Sorry, but the computer chose {computer_choice}")
            else:
                print(f"Well done. The computer chose {computer_choice} and failed")
                score += 100