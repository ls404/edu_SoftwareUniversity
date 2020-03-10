N = int(input())
K = int(input())
result = ''

for num1 in range(1, N+1):
    for num2 in range(1, N+1):
        for letter1 in range(97, 97+K):
            for letter2 in range(97, 97 + K):
                for num3 in range(max(num1, num2)+1, N+1):
                    result += str(num1) + str(num2) + chr(letter1) + chr(letter2) + str(num3) + ' '

print(result)