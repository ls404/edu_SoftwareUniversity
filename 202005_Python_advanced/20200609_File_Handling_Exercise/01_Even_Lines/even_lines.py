'''
Maketrans python method generates dictionary to be used by translate method
'''

translation = ''
translation = translation.maketrans('-,.!?', '@@@@@')

with open('text.txt', 'r') as file:
    for idx, line in enumerate(file):
        if idx % 2 == 0:
            print(' '.join(line.translate(translation).split()[::-1]))
