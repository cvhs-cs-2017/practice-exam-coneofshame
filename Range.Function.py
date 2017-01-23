"""Use the range function to print the numbers from 1-20"""
def count():
    for i in range(1, 21):
        print(i)

print(count())
"""Repeat the exercise above counting by 2's"""
def count2():
    for i in range (2, 21, 2):
        print(i)
print(count2())


"""Print all the multiples of 5 between 10 and 200 in DECENDING order"""
def multiple5():
    for i in range (200, 9, -5):
        print(i)
multiple5()
