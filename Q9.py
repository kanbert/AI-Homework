a = []
for n in range(0, 100):
    a.append(n)
def c(x):
    return x ** 3
b = list(map(c, a))
for k, i in enumerate(b):
    number = 0
    count = 0
    for j in range(0, len(str(i))):
        number = str(i)[j]
        count += int(number)
    if (count == a[k]):
        print(a[k])
