a = 56
d = 0
type(a)
b = float(a)
c = complex(a, b)
print(a, b, c)
print(bool(a > d))
lst = [45, 67, 89, 47]
print(lst[0]) # single value from the list using index number
st = {34, 67, 89}
t = (65, 87, 8)

print(lst, st, t)
print(list(range(0, 10)))
print(list(range(0, 11, 2)))  # range(start,end(excluded),difference)
dictionary = {'gaga': 'iphone', 'shankar': 'samsung', 'sharan': 'mi'}
print(dictionary)
print(dictionary.keys())  # fetching keys
print(dictionary.values())  # fetching values
print(dictionary['gaga'])  # fetching single value using key
print(dictionary.get('sharan'))

set1 = set("GeeksForGeeks") # it will print on;y once no any repeated values
print("\nSet with the use of String: ")
print(set1)
