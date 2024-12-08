# list is a collection data type
# ordered, mutable, allow duplicate
# use square bracket same as arrya
# allows diffrerent data types
# Access list by index
print("Welcome to Python Lists")

# Create an empty list

my_list_one = []
my_list_two = list()

print(my_list_one)
print(my_list_two)

# we can append items to the list
# it allows different data types

fruits = ["apple","banana", "orange"]
cross_list  = [1,True,"Apple"] # Cross List
dup_list = [True, True, "apple","apple"]
print(fruits[0])
print("Cross Data type list : ", cross_list)
print("Duplicate list : ", dup_list)

# Negative index
print("Last element of cross list", cross_list[-1])

# Iterate in the list
for item in cross_list:
    print("The items of cross lists :", item)
    
# to check wheter an item in list

if "banana" in fruits:
    print("Banana is there in fruits")
else:
    print("No banans found")
    
# Number of elemets in list
print("The length of the fruits list :", len(fruits))

# append its tyo the lists
fruits.append("lemon")
print("Apppended fruit list", fruits)

# insert item at a specific index
fruits.insert(2, "mango")
print("Insert item in index 2 of fuits : ", fruits)

# pop last item
pop_item = fruits.pop()
print("The pop list : ", fruits)
print("poppped item :", pop_item)

# remove a speci item baed on name
fruits.remove("mango")
print("The fuits list final", fruits)

# to clear all th elemenrts in a list

fruits.clear()
print(fruits)

# Reverse a list

my_list_three = ["alice", "bob", "demy"]
print("The list in order : ", my_list_three)
my_list_three.reverse()
print("The reversed list : ", my_list_three)

sort_list = [22,12,1,44]
sort_list.sort() # this sort method will overwrite your original list
print("The sorted list : ", sort_list)

# if you dont want to overwrite ur original list use sorter() function
new_list = ['w','f', 'a','d','b']
new_list_sorted = sorted(new_list)

print("Original list : ", new_list)
print("Soretd List: ", new_list_sorted)

# need a list will same element multiple times
multi_list = [100] * 5
print("Multi List : ", multi_list)

# concat two list with plus oerator

list_one = [1,2,3,4]
list_two = [10,20]
new_list = list_one + list_two
print("Concat list : ", new_list)


# slicing a list
my_list = [1,2,3,4,5,6,7]
sliced_list = my_list[0:3]
print("The sliced list : ", sliced_list)
