from random import randint
 
n = int(input())
a = [randint(0,1) for i in range(n)]
print(a)
count0 = 0
count1 = 0
for i in range (0, n):
    if a[i] == 0:
        count0 += 1
    else:
        count1 += 1
if count1 <= count0:
    print(count1)
else:
    print(count0)

