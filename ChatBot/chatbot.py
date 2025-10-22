def pupu():
    """""
    Introduces the chatbot by name and creation year.
    """""
    bot_name = "Butters"
    vicidish = '2025'
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {vicidish}.")


def rapugo():
    """""
    Asks  the user for their name and greets them.
    """""
    print("Please remind me your name.")
    name = input(" > ")
    print(f" What a great name you have,  {name}!")


def tutu():
    """""
    Guess user age.
    """""
    print("Let my guess your age.")
    print("Enter reminders of dividing your age by 3,5 and 7 .")
    remainder3= int (input(" > "))
    remainder5 = int (input(" > "))
    remainder7 = int (input(" > "))
    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print  (f"Your age is {age}; thets a good time to start programming!")


def count():
    """""
    Batters prove to user thet he can count to any number.
    """""
    print("Now i will prove to you thet l can count to any number you want. ")
    num =    int(input(" > "))
    for i in range (num + 1):
        print(f"{i}")


def test():
    """""
    Testing user knowledge of Southspark.
    """""
    print ("Let's test your knowledge of Southspark.")
    print ("What was the name of Kyle Broflovski's brother?")
    print ("1. Cartman")
    print ("2. Kenny")
    print ("3. Tolkien")
    print ("4. Ike")
    correct_answer = 4
    while True:
        answer = int(input(" > "))
        if answer == correct_answer:
            break
        else:
            print("Please, try again.")
    print ("Congratulations, have a nice day!")
pupu()
rapugo()
tutu()
count()
test()

