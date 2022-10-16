# this returns the result of the given function to apply for the item from the iterables

numbers = [1, 2, 3, 4, 4, 4]
squers = list(map(lambda a: a * a, numbers))
print(squers)
