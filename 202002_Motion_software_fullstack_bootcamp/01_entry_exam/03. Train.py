result = dict()

while True:
    command = input()
    if command == 'Slide rule':
        break
    cmd_list = command.split(':')
    cmd_list2 = cmd_list[1].split('->')
    town = cmd_list[0]
    time_ambush = cmd_list2[0]
    passengers_count = int(cmd_list2[1])
    # print(town, time_ambush, int(passengers_count))
    if time_ambush == 'ambush':
        if town not in result.keys():
            continue
        else:
            # result.pop(town, None)
            result[town][0] = 0
            result[town][1] -= passengers_count
    else:
        time = int(time_ambush)
        if town not in result.keys():
            result[town] = [time, passengers_count]
        else:
            if result[town][0] == 0 or result[town][0] > time:
                result[town][0] = time
            result[town][1] += passengers_count

for_removal = []
for i in result:
    if result[i][0] <= 0 or result[i][1] <= 0:
        for_removal.append(i)
for i in for_removal:
    result.pop(i, None)

for i in sorted(sorted(result), key=lambda x: result[x][0]):
    print(f"{i} -> Time: {result[i][0]} -> Passengers: {result[i][1]}")
