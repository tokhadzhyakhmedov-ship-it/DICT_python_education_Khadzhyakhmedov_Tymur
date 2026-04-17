import random

def generate_task(level):
    if level == 1:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        op = random.choice(["+", "-", "*"])
        print(f"{a} {op} {b}")

        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        else:
            return a * b

    elif level == 2:
        a = random.randint(11, 29)
        print(a)
        return a * a


def get_level():
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")

        level = input()

        if level not in ["1", "2"]:
            print("Incorrect format.")
        else:
            return int(level)


def get_answer():
    while True:
        try:
            return int(input())
        except:
            print("Incorrect format.")


def save_result(score, level):
    answer = input("Would you like to save your result to the file? Enter yes or no.\n")

    if answer.lower() in ["yes", "y"]:
        name = input("What is your name?\n")

        if level == 1:
            level_text = "simple operations with numbers 2-9"
        else:
            level_text = "integral squares of 11-29"

        file = open("results.txt", "a")
        file.write(f"{name}: {score}/5 in level {level} ({level_text})\n")
        file.close()

        print('The results are saved in "results.txt".')


def main():
    level = get_level()
    score = 0

    for i in range(5):
        correct = generate_task(level)
        answer = get_answer()

        if answer == correct:
            print("Right!")
            score += 1
        else:
            print("Wrong!")

    print(f"Your mark is {score}/5.")
    save_result(score, level)

main()