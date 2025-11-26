import random
def play():
    words = ['python','java','c++','ruby']
    word = random.choice(words)
    hidden = list("-"*len(word))
    attempts = 8
    guessed_L = set()

    print("\n"+"HANGMAN\n")

    while attempts > 0:
        print("".join(hidden))
        letter = input("Input your letter: > ").strip()
        if len(letter) != 1:
            print("You must enter a single letter.")
            continue
        if not letter.isalpha() or not letter.islower():
            print("You must enter a lowercase letter.")
            continue
        guessed_L.add(letter)
        if letter not in word:
            print(" Thet latter isn't in the word.")
            attempts -= 1
        else:
            improved = False
            for i in range(len(word)):
                if word[i] == letter and hidden[i] == "-":
                    hidden[i] = letter
                    improved = True
            if not improved:
                print(" No improvements.")
                attempts -= 1
        if "".join(hidden) == word:
            print("You guessed the word {word}")
            print("You survived")
            return
    print("Sorry, you lose :(")
def main():
    print("HANGMAN GAME")
    while True:
        comand = input('Tipe "P" to play the game, "Q" to quit: > ').strip()
        if comand == "P":
            play()
        elif comand == "Q":
            break
if __name__ == "__main__":
    main()
