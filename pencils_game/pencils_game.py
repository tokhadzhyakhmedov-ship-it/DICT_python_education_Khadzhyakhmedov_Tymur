import random


# Функція для ходу бота
def bot_move(pencils_left):
    if pencils_left % 4 == 0:
        return 3
    elif pencils_left % 4 == 3:
        return 2
    elif pencils_left % 4 == 2:
        return 1
    else:
        return random.randint(1, min(3, pencils_left))


# Функція для введення кількості олівців з перевіркою коректності
def get_pencils():
    while True:
        print("How many pencils would you like to use:")
        pencils_input = input()

        if not pencils_input.isdigit():
            print("The number of pencils should be numeric")
        elif int(pencils_input) == 0:
            print("The number of pencils should be positive")
        else:
            return int(pencils_input)


# Функція вибору першого гравця
def choose_first_player(players):
    while True:
        print("Who will be the first (Tony, Poli):")
        current_player = input()

        if current_player not in players:
            print("Choose between 'Tony' and 'Poli'")
        else:
            return current_player


# Функція для ходу користувача з перевіркою введення
def player_move(pencils):
    while True:
        move = input()

        if move not in ["1", "2", "3"]:
            print("Possible values: '1', '2' or '3'")
        elif int(move) > pencils:
            print("Too many pencils were taken")
        else:
            return int(move)


# Основна функція, яка реалізує логіку гри
def play_game():
    players = ["Tony", "Poli"]

    pencils = get_pencils()
    current_player = choose_first_player(players)

    while pencils > 0:
        print("|" * pencils)
        print(f"{current_player}'s turn:")

        if current_player == "Poli":
            taken = bot_move(pencils)
            print(taken)
        else:
            taken = player_move(pencils)

        pencils -= taken

        # Перевірка завершення гри
        if pencils == 0:
            if current_player == "Tony":
                print("Poli won!")
            else:
                print("Tony won!")
            break

        # Зміна гравця
        current_player = "Poli" if current_player == "Tony" else "Tony"

play_game()
