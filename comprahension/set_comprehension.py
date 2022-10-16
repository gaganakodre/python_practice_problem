nums = [1, 2, 4, 1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 7, 8]
my_sets=set()
for n in nums:
    my_sets.add(n)
print(my_sets)
# using set comprehension
my_sets={num for num in nums}
print(my_sets)
#
my_set = {num for num in nums if num % 2 == 0}
print(my_set)

