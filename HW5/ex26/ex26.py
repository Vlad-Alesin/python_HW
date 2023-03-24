"""
Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8

"""
def degree (x, y, d):
    if y == 0 :
        return 1
    elif y == 1:
        return x
    elif y >= 2:
        return degree(x*d, y-1, d)
    return x

A = int(input('A='))
B = int(input('B='))
d = A

print(degree(A, B, d))