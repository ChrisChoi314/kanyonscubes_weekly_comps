import random

wca = ['2x2', '3x3', '4x4', '5x5', '6x6', '7x7', 'OH', 'sq1', 'clock', 'mega', 'skewb', 'pyra']
non_wca = ['ch2', 'mirror', '2x2x3', 'redi', 'dino', 'ivy', 'rex', 'kilo', 'mirrorbld', '2x2OH']

print('The WCA events will be: ')

for i in range(2):
    random_num = random.randint(0,len(wca)-1)
    print(wca[random_num])
    wca.pop(random_num)

print('The non-WCA events will be: ')

for i in range(2):
    random_num = random.randint(0,len(non_wca)-1)
    print(non_wca[random_num])
    non_wca.pop(random_num)