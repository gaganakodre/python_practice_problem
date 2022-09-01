num = [1, 2, 3, 4, 5, 6, 7, 8]
my_list = []
for n in num:
    my_list.append(n)
print(my_list)
# using list comprehension
my_list = [n for n in num]
print(my_list)

my_list = []
for n in num:
    my_list.append(n * n)
print(my_list)

my_list = [n * n for n in num]
print(my_list)

# using lambda and map
my_list=list(map(lambda n:n*n,num))
print(my_list)

# even number list
my_list = []
for n in num:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)


my_list= [n for n in num if n%2==0]
print(my_list)

# using lambda and map
my_list=list(filter(lambda  n : n%2==0,num))
print(my_list)


# alphabet code with numbers like a,1...etc
my_list=[]
for letter in 'abcd':
    for n in range(4):
        my_list.append((letter,n))
print(my_list)

# using list comprehension
my_list=[(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)
my_list= [n for n in num if n%2==0]
print(my_list)


fruit_list=['apple','grapes','kiwi']
new_list=[fruits for fruits in fruit_list if 'a' in fruits]
print( list(new_list))




