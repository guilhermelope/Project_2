from itertools import count

c1 = count(step=2)

print('Count')
for i in c1:
    if i >= 1000:
        break

    print(i)