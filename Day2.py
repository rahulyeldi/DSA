age=int(input("What is your age: "))
if age<18:
    print("You are a minor")
elif age<60:
    print("You are an adult")
else:
    print("You are a senior citizen")


#number is even or odd
num=int(input("Enter a number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")
    
#username and password
old_username="rahulsy"
old_password="1234"

username=input("Enter your username: ")
password=input("Enter your password: ")

if username==old_username and password==old_password:
    print("Login successful")
    