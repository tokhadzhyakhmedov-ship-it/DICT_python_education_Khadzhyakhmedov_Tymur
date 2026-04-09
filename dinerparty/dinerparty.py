import random

print("Enter the number of friends (except you):")
number_of_friends = int(input())
if number_of_friends <= 0:
    print("you're lonely :(")
else:
    print("Enter the number of friends (except you) on a new line:")
    friends = {}
    for i in range(number_of_friends):
        name = input()
        friends[name] = 0
    print("Enter the total amount:")
    total_amount = float(input())
    share = round(total_amount / number_of_friends, 2)
    for name in friends:
        friends[name] = share
    print("Do you want to use the Who is lucky? feature? Write Yes/No:")
    lucky_answer = input()
    if lucky_answer == "Yes":
        lucky_friend = random.choice(list(friends.keys()))
        print(f"{lucky_friend} is lucky one!")
        new_share = round(total_amount / (number_of_friends -1), 2)
        for name in friends:
            if name == lucky_friend:
                friends[name] = 0
            else:
                friends[name] = new_share
    else:
        print("No one is lucky")
    print(friends)


