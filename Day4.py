# #Functions
# #Defining and Calling a Function
# def greet():
#     print("Welcome")
# greet()

# #Function with Parameters
# def greet_user(name):
#     print("Hello",name)
# greet_user("Rahul")

# #Function with Return Value
# def add(a, b):
#     return a + b
# result = add(5, 7)
# print("Sum is:", result)

# #Default Parameters
# def greet(name="Guest"):
#     print("Hello,", name)
# greet()           # Hello, Guest
# greet("Ravi")     # Hello, Ravi

# #Keyword Arguments
# def student_info(name,age):
#     print("Name:", name)
#     print("Age:", age)
# student_info(age=21,name="Rahul")

# #Variable-Length Arguments
# # *args: any number of positional arguments
# def total_sum(*num):
#     return sum(num)
# print("Sum:", total_sum(1, 2, 3, 4, 5))

# # **kwargs: any number of keyword arguments
# def printinfo(**info):
#     for key,value in info.items():
#         print(key, ":",value)
# printinfo(name="Rahul",age=21)


#Practice problems
#1.	Write a function that takes two numbers and returns their GCD.
# a=int(input("Enter 1st number: "))
# b=int(input("Enter 2nd number: "))
# # def gcd(a,b):
# #     result=1
# #     for i in range(1,min(a,b)+1):
# #         if a%i==0 and b%i==0:
# #             result=i
# #     return result
# # print("GCD is:",gcd(a,b))

# #another approach-euclidean
# def gcd(a,b):
#     while b:
#         a,b=b,a%b
#     return a
# print(gcd(a,b))

#2.Write a function that takes a list of numbers and returns the average.
def average(*lst):
    return sum(lst)/len(lst)
print("Average is:",average(1,2,3,4,5))

#3.Prime number or not
n=int(input("Enter number: "))
def is_prime(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
    return cnt==2
print(is_prime(n))
            
#another approach
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True