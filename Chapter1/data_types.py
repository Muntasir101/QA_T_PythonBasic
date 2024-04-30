myAge = input('Enter age: ')
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

print(10 > 20 and 10 < 30)  # False
print(10 > 20 or 10 < 30)  # True
print(not (10 > 20 and 10 < 30))  # False

"""
2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
True and not 2 + 2 == 5 and 2 * 2 == 2 + 2
True and not False and 2 * 2 == 2 + 2
True and True and 2 * 2 == 2 + 2
True and True and True
True and True
True
"""
name = 'Alice'

if name == 'Alice':
    print('Hi, Alice.')