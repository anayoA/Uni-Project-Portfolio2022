def stringdel(x):
    if len(x) > 1:
        return x[:-1]
    else:
        return x

val = input('Input your message: ')
print(stringdel(val))