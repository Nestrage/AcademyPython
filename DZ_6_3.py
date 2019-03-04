import random
a = []
for i in range(1,11):
    i = random.randint(-100, 100)
    a.append(i)
print(a)
print(a[::-1])