# Список доступних форматтерів
formatters = ["plain", "bold", "italic", "header", "link",
              "inline-code", "ordered-list", "unordered-list", "new-line"]


# Безпечне введення числа
def safe_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Incorrect format")


# Обробка заголовка
def make_header():
    while True:
        level = safe_int_input("Level: ")
        if level < 1 or level > 6:
            print("The level should be within the range of 1 to 6")
        else:
            break

    user_text = input("Text: ")
    return "#" * level + " " + user_text + "\n"


# Обробка списків
def make_list(ordered, text):
    while True:
        rows = safe_int_input("Number of rows: ")
        if rows <= 0:
            print("The number of rows should be greater than zero")
        else:
            break

    if text != "" and not text.endswith("\n"):
        text += "\n"

    for i in range(1, rows + 1):
        row_text = input(f"Row #{i}: ")
        if ordered:
            text += f"{i}. {row_text}\n"
        else:
            text += f"* {row_text}\n"

    return text


text = ""

while True:
    command = input("Choose a formatter: ")

    if command == "!help":
        print("Available formatters:", " ".join(formatters))
        print("Special commands: !help !done")

    elif command == "!done":
        file = open("output.md", "w", encoding="utf-8")
        file.write(text)
        file.close()
        break

    elif command not in formatters:
        print("Unknown formatting type or command")

    elif command == "plain":
        user_text = input("Text: ")
        text += user_text
        print(text)

    elif command == "bold":
        user_text = input("Text: ")
        text += f"**{user_text}**"
        print(text)

    elif command == "italic":
        user_text = input("Text: ")
        text += f"*{user_text}*"
        print(text)

    elif command == "inline-code":
        user_text = input("Text: ")
        text += f"`{user_text}`"
        print(text)

    elif command == "new-line":
        text += "\n\n"
        print(text)

    elif command == "link":
        label = input("Label: ")
        url = input("URL: ")
        text += f"[{label}]({url})"
        print(text)

    elif command == "header":
        text += make_header()
        print(text)

    elif command == "ordered-list":
        text = make_list(True, text)
        print(text)

    elif command == "unordered-list":
        text = make_list(False, text)
        print(text)
