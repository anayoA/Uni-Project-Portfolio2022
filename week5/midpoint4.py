def password_checker(password):
    from string import ascii_letters as letters, digits, punctuation
    has_letter = has_digit = has_punc = False
    for character in password:
        if character in letters:
            has_letter = True
        elif character in digits:
            has_digit = True
        elif character in punctuation:
            has_punc = True
    return has_letter and has_digit and has_punc


while True:
    pswrd = input('Please enter a password containing at LEAST one of each: digit, punctuation character and letter: ')
    if password_checker(pswrd) == True:
        print('This password is acceptable.')
        break
    else:
        print('This pass is not acceptable. Please read the instructions and try again.')
        continue
