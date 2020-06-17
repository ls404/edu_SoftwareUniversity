import os

while True:
    command = input().split('-')
    if command[0] == "End":
        break

    elif command[0] == "Create":
        filename = command[1]
        with open(filename, 'w') as file:
            file.write("")

    elif command[0] == "Add":
        filename = command[1]
        file_content = command[2]
        with open(filename, 'a') as file:
            file.write(file_content)
            file.write("\n")

    elif command[0] == "Replace":
        filename = command[1]
        old_string = command[2]
        new_string = command[3]
        if os.path.exists(filename):
            text = ""
            with open(filename, 'r') as file:
                text = file.read()
            text = text.replace(old_string,new_string)
            with open(filename, 'w') as file:
                file.write(text)
        else:
            print("An error occurred")

    elif command[0] == "Delete":
        filename = command[1]
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print("An error occurred")


