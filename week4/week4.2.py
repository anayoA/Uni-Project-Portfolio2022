
def letcheck(a):
    upper = 0
    lower = 0
    for letter in a:
        if letter.islower():
            lower += 1
        else:
            upper += 1
    print('The number of lowercase letters is', lower)
    print('The number of uppercase letters is', upper)
    return

letcheck('My name is Anayo')