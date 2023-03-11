n = int(input())
m = int(input())
piece = int(input())

if piece == 1 and (n != 1 or m!=1):
    print('no')     
elif (piece % n == 0) or (piece % m == 0):
    if n * m > piece:
        print('yes')
else:
    print('no') 