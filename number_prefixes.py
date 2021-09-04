numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
"""
for x in numbers:
    index = numbers.indexOf(x)
    if index == 0:
        print(x + "st")
    if index == 1:
        print(x + "nd")
    if index == 2:
        print(x + "rd")

"""
for x in numbers:
    index = numbers.index(x)
    x = str(x)
    if index == 0:
        print(x + "st")
    elif index == 1:
        print(x + "nd")
    elif index == 2:
        print(x + "rd")
    else:
        print(x + "th")