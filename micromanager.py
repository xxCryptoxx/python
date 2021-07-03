import os

#input
sentence = input('Type the big problem: ')
then = ' then '
counter = 0

#process
output = sentence.split(then)
listtostr = '\n'.join([str(elem) for elem in output])
with open('micromanage.md', 'w') as f:
    f.write(listtostr)
    f.close()

os.system('clear')

#output
print('\033[1mProblem Broken Down\033[0m')
print(f'\n{listtostr}')

"""
Example

INPUT:
>> Get the format of a string then display the output to the screen then clear the screen then close the program

OUTPUT:
<< Get the format of a string
<< Display the output to the screen
<< Clear the screen
<< Close the program
"""