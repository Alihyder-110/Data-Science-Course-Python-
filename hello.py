print("Hello GitHub")
print(len("hello word"))
#Operators
print(5 + 3)
print(10 - 2)
print(4 * 3)
print(15 / 3)
print(10 % 3)


# Conditional statements
# age = int(input("Enter your age: "))
# print("You entered:", age)
# if(age >= 18):
#     print("You are an adult.")
# elif(age >= 13):
#     print("You are a teenager.")
# else:
#     print("You are a child.")

first_name = "AliHyder"
print( first_name)
print(len(first_name))
print(first_name[2:])
print(first_name[:-3])
print(first_name[-3::])
print(first_name[::2])

print(first_name.upper())
print(first_name.lower())

# LOOPS
seq = [1, 2, 3, 4, 5]
print(seq)
for item in seq:
    print(item) #this shows the items in the list

print(item) #this shows the number of items

for item in seq:
    print(item + item) #here it will double the items

#now if i want to print the message or anything at that number
for item in seq:
    print("Welcome to the world of python")

alp = ['a', 'b', 'c', 'd', 'e']
print(seq+alp) #this will combine the two lists
