# Not tested on Windows!
import os

path = input()
result_dict = {}
count_sep = path.count(os.path.sep)

for root, dirs, files in os.walk(path):
    print(files)
    if root.count(os.path.sep) - count_sep > 1:
        continue
    for file in files:
        extension = file.split('.')[-1]
        if extension not in result_dict:
            result_dict[extension] = []
        result_dict[extension].append(file)

print(result_dict)
print("------------------")
result_str = ""
for key, value in sorted(result_dict.items()):
    result_str += f".{key}\n"
    for file in sorted(value):
        result_str += f"- - - {file}\n"

desktop = os.path.expanduser("~/Desktop")  # works on linux and windows
final_location = desktop + os.path.sep + "report.txt"
print(result_dict)
print(final_location)

with open(final_location, 'w') as file:
    file.write(result_str)

