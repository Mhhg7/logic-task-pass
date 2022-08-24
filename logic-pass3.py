
x = [1,2,3,4,5,6,7,8]

y = []

for i in x:
    e = True
    for s in range(2,max(x)):
        if i % s == 0 or i == 1:
            e = False
            break
        if e:
            y.append(i)
print(list(set(y)))
