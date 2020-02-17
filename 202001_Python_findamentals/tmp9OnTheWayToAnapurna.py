
# Solution without dublicates, but dublicates should be added

# result = dict()
# while True:
#     entry = input().split("->")
#     command = entry[0]
#     if command == 'END':
#         pass # print sorted dictionary items
#         break
#     if command == 'Add':
#         if entry[1] not in  result.keys():
#             result[entry[1]] = set()
#         # include = set(entry[2].split(','))
#         result[entry[1]].update(set(entry[2].split(',')))
#     if command == 'Remove':
#         result.pop(entry[1], None)
#
# print(result)

result = dict()
while True:
    entry = input().split("->")
    command = entry[0]
    if command == 'END':
        pass # print sorted dictionary items
        break
    if command == 'Add':
        if entry[1] not in  result.keys():
            result[entry[1]] = list()
        result[entry[1]]= result[entry[1]] + (list(entry[2].split(',')))
    if command == 'Remove':
        result.pop(entry[1], None)

print("Stores list:")
for i in sorted(result, key = lambda x: (len(result[x]), x), reverse = True):
    print(i)
    for k in result[i]:
        print("<<"+k+">>")
