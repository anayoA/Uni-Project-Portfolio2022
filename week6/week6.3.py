
num = int(input('Input a number to determine if it is a prime number: '))
if num > 1:
    for x in range(2, num):
        if (num % x) == 0:
            print(num, "is not a prime number.")
            print(x, "times", num // x, "is equal to", str(num) + '.')
            break
    else:
        print(num, "is a prime number.")

else:
    print(num, "is not a prime number.")