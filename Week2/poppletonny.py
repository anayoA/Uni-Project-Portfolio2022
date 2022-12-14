"""The Head of Computing at the University of Poppleton is tasked with dividing a
group of students into lab groups. A lab group is usually 24 students, but this is
sometimes varied to create groups of similar size. Write a program that prompts for
the number of students and group size, and then displays how many groups will be
needed and how many will be left over in a smaller group.
How many students? 113
Required group size? 22
There will be 5 groups with 3 students left over.
For bonus credit, see if you can fix the grammar in the output. So if there were 101
students in groups of 20 the output would be:"""

stunum = input('How many students? ')
group = input('Required group size? ')
val1 = int(stunum) // int(group)
val2 = int(stunum) % int(group)

if val2 == 1:
    print('There are',val1,'groups.')
    print('There is one student left over')
else:
    print('The number of full groups is: ' + str(val1))
    print('The number of students left over in the small group is: ' + str(val2))



