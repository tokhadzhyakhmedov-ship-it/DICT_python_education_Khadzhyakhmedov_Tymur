import random
players = ["Tony", "Poli"]
def bot_move(pencils_left):
    if pencils_left % 4 == 0:
        return 3
    elif pencils_left % 4 == 3:
        return 2
    elif pencils_left % 4 == 2:
        return 1
    else:
        return random.randint(1, min(3, pencils_left))
while True:
    print("How many pencils would you like to use:")
    pencils_input = input()
    if not pencils_input.isdigit():
        print("The number of pencils should be numeric")
    elif int(pencils_input) == 0:
        print("The number of pencils should be positive")
    else:
        pencils = int(pencils_input)
        break
while True:
    print("Who will be the first (Tony, Poli):")
    current_player = input()
    if current_player not in players:
        print("Choose between 'Tony' and 'Poli'")
    else:
        break
while pencils > 0:
    print("|" * pencils)
    print(f"{current_player}'s turn:")
    if current_player == "Poli":
        taken = bot_move(pencils)
        print(taken)
    else:
        while True:
            move = input()
            if move not in ["1", "2", "3"]:
                print("Possible values: '1', '2' or '3'")
            elif int(move) > pencils:
                print("Too many pencils were taken")
            else:
                taken = int(move)
                break
    pencils -= taken
    if pencils == 0:
        if current_player == "Tony":
            print("Poli won!")
        else:
            print("Tony won!")
        break
    current_player = "Poli" if current_player == "Tony" else "Tony"