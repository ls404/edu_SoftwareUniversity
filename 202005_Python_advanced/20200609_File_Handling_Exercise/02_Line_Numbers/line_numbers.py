import string           # option 2 for counting punctuation

with open('text.txt', 'r') as file:
    result = ''
    for idx, line in enumerate(file):
        # punct_len = len([x for x in line if x in ".,!?-'\";:"])       # option 1 without module import
        punct_len = len([x for x in line if x in string.punctuation])   # option 2 with module import
        alpha_len = len([x for x in line if x.isalpha()])
        result += f"Line {idx + 1}: {line.rstrip()} ({alpha_len})({punct_len})\n"

with open("output.txt", 'w') as file:
    file.write(result)
