num = int(input('Input a number to find the factors of: '))

for n in range(1, num + 1):
    if num % n == 0:
        print(n)