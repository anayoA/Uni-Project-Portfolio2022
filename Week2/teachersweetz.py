"""A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
first count the sweets and then divide them according to how many pupils attend
that day. Write a program that will tell the teacher how many sweets to give to each
pupil, and how many she will have left over."""
import time

print('/////////////////////////////////////////////////\nLoading minion charity program. Please wait..\n////////////////////////////////////////////////')

time.sleep(3)
sweets = input('Beep boop. Hello Miss. How many sweets will you give to the minions today? ')
minions = input('A wise choice. How many minions do you have in your possession today? ')

validsweets = int(sweets)
validminions = int(minions)

minionprize = validsweets // validminions
minionfight = validsweets % validminions
print('Perfect. You will ration approximately',minionprize,'sweets to each minion, with',minionfight,'sweets left over, which they can fight to the death over.')
time.sleep(5)
print('Thank you, Miss. Enjoy your remaining time with the class.')