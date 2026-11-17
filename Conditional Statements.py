# Conditional statements
age = int(input("Enter your age: "))
print("You entered:", age)
if(age >= 18):
    print("You are an adult.")
elif(age >= 13):
    print("You are a teenager.")
else:
    print("You are a child.")

student_name = "AliHyder"
marks = int(input("Enter your marks: "))
if(marks>=90):
    print(student_name + " has A grade")
elif(marks>=80):
    print(student_name + " has B grade")
else:
    print(student_name + " has C grade")