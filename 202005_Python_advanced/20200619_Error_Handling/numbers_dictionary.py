numbers_dictionary = {}

line = input()

try:
    while line != "Search":
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
        line = input()

    line = input()

    while line != "Remove":
        searched = line
        print(numbers_dictionary[searched])
        line = input()

    line = input()

    while line != "End":
        searched = line
        del numbers_dictionary[searched]
        line = input()

except ValueError:
    print("The variable number must be an integer")

except KeyError:
    print("Number does not exist in dictionary")

print(numbers_dictionary)