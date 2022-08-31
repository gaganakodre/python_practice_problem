nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def gen_num(nums):
    for n in nums:
        # used to return from a function without destroying the states of its local variable
        yield n * n


my_gens = gen_num(nums)

for i in my_gens:
    print(i)

my_tuple = (n * n for n in nums)
print(tuple(my_tuple))
