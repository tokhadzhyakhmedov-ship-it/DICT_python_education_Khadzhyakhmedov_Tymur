import random

print("Enter the number of friends joining (except you):")

try:
    number_of_friends = int(input())
except ValueError:
    print("Incorrect format")
else:
    if number_of_friends <= 0:
        print("No one is joining for the party")
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        friends = {}

        for _ in range(number_of_friends):
            name = input()
            friends[name] = 0

        print("Enter the total amount:")

        try:
            total_amount = float(input())
        except ValueError:
            print("Incorrect format")
        else:
            share = round(total_amount / number_of_friends, 2)

            for name in friends:
                friends[name] = share

            print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
            lucky_answer = input()

            if lucky_answer == "Yes":
                lucky_friend = random.choice(list(friends.keys()))
                print(f"{lucky_friend} is the lucky one!")

                if number_of_friends == 1:
                    friends[lucky_friend] = 0
                else:
                    new_share = round(total_amount / (number_of_friends - 1), 2)

                    for name in friends:
                        if name == lucky_friend:
                            friends[name] = 0
                        else:
                            friends[name] = new_share
            else:
                print("No one is going to be lucky")

            print(friends)