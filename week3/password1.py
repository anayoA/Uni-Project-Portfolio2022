pswrd = input('Please choose a password: ')
pswrd2 = input('Please retype your new password for confirmation: ')
if pswrd2 == pswrd:
        print('Thank you. Your password has been set.')
else:
    print('Error: Your two passwords do not match. Self destructing in 5..')
