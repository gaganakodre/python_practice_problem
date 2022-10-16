weeks_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
num_list = [1, 2, 3, 4, 5, 6, 7]
print(list(zip(weeks_list, num_list)))
# zip will take the index of 1list and antoher and it will print
my_dict = {}
for weeks, num in zip(weeks_list, num_list):
    my_dict[weeks] = num
print(my_dict)
# using dict comprehension
my_dict = {weeks: num for weeks, num in zip(weeks_list, num_list)}
print(my_dict)

# we can give the condition
my_dict = {weeks: num for weeks, num in zip(weeks_list, num_list) if weeks != 'monday'}
print(my_dict)

# using  dict comprehension
num = [1, 2, 3]
new_dict = {num: num * num for num in num}
print(new_dict)
