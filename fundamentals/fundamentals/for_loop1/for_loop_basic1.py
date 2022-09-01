for int in range(0, 151):
    print(int)

for x in range(5, 1001):
    x = x * 5
    print(x)

for y in range(1, 101):
    if y % 5 ==  0:
        print("Coding")
    if y % 10 == 0:
        print("Coding Dojo")
    else:
        print(y)

sum = 0
for o in range(0, 500000):
    if o % 2 != 0:
        sum += o
        print(sum)

for p in range(2018, 0, -4):
    print(p)

lowNUm = 2
highNum = 9
mult = 3

for s in range(lowNUm, highNum + 1):
    if s % mult == 0:
        print(s)