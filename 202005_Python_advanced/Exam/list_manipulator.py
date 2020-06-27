def list_manipulator(*args):
    lst = args[0]
    param1 = args[1]
    param2 = args[2]
    if args[2:]:
        nums = list(args[3:])
    if param1 == 'add':
        if param2 == 'beginning':
            return nums + lst
        elif param2 == 'end':
            return lst + nums
    if param1 == 'remove':
        if param2 == 'beginning':
            if nums:
                del lst[0:nums[0]]
            else:
                del lst[0]
            return lst
        if param2 == 'end':
            if nums:
                return lst[:-nums[0]]
            else:
                del lst[-1]
                return lst








# print(list_manipulator([1,2,3], "remove", "end"))
# print(list_manipulator([1,2,3], "remove", "beginning"))
# print(list_manipulator([1,2,3], "add", "beginning", 20))
# print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
# print(list_manipulator([1,2,3], "remove", "beginning", 2))
# print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))