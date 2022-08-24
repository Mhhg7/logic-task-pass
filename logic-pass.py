characters = 'qwertyuioasdfghjk'

inp = input('enter: ')

for i in characters:
    if inp == i:
        continue
    print(i,end='')
