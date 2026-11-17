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

student_name = "AliHyder"
marks = int(input("Enter your marks: "))
if(marks>=90):
    print(student_name + " has A grade")
elif(marks>=80):
    print(student_name + " has B grade")
else:
    print(student_name + " has C grade")

first_name = "AliHyder"
print( first_name)
print(len(first_name))
print(first_name[2:])
print(first_name[:-3])
print(first_name[-3::])
print(first_name[::2])

print(first_name.upper())
print(first_name.lower())

# tuples
#Tuples are immutable (cannot be changed)
t1 = ('one',4,3,5)
print(len(t1))
t1[-1]
t1.index('one')
t1.count('one')

#sets
x= set()
x.add(1)
x.add(2)
print(x)

# LOOPS
seq = [1, 2, 3, 4, 5]
print(seq)
for item in seq:
     print(item) #this shows the items in the list

# print(item) #this shows the number of items
for item in seq:
    print(item + item) #here it will double the items

#now if i want to print the message or anything at that number
for item in seq:
     print("Welcome to the world of python")

alp = ['a', 'b', 'c', 'd', 'e']
print(seq+alp) #this will combine the two lists

com = seq + alp
print(com)#this will print the combined list
print(seq)
print(alp)
alp.append('f') #this will add the item to the list
print(alp)
alp.pop(5) #this will remove the item from the list
print(alp)

#you can call it the loops in dictionary
ages = {"Sam":3,"Frank":4,"Dan":29}

for key in ages:
    print("This is the key")
    print(key)
    print("This is the value")
    print(ages[key])
    print("\n")

mypairs = [(1,10),(3,30),(5,50)]

# Normal
for tup in mypairs:
    print(tup)

# Tuple un-packing
for item1,item2 in mypairs:
    print(item1)
    print(item2)

i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1

# RANGE FUNCTION
# range() can quickly generate integers for you, based on a starting and ending point

# Note that its a generator:
range(8)

list(range(8))

for i in range(8):
    print(i)

# Start and ending
range(1,10)

# Third argument for step-size
range(0,10,2)

#Functions
# A simple print 'hello' function

def hello():
    print("hello")

hello()

def giveMeHello():
    return "hello"

result = giveMeHello()
print(result)

def evenCheck(num):
    print("I'm checking to see if {} is even!".format(num))
    print(num % 2 == 0)
evenCheck(41)

def helloYou(name="Default Name"):
    return("Hello, "+name)

# Try this with and without a name
result = helloYou()
print(result)


def addEvenOnly():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))

    if (num1 % 2 != 0) or (num2 % 2 != 0):
        return False
    else:
        return num1 + num2

x = addEvenOnly()
print(x)

