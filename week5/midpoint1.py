name = input('Greetings! How shall we call you? ')
namecheck = name.startswith(('Lord ', 'Lady '))
if namecheck == False:
    print('You may not be known by that name!')
else:
    print('It shall be so,', name)