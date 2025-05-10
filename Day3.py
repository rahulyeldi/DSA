#For loop
for i in range(5):
    print(i)

for char in "\nPython":
    print(char)

print("\n")

#while loop
count=5
while count>0:
    print(count)
    count-=1

#break
for i in range(5):
    if i==3:
        break
    print(i)
    
print("\n")

#continue
for i in range(5):
    if i==3:
        continue
    print(i)
 
"""
🔹 4. range() Function
	•	range(n) → 0 to n-1
	•	range(start, stop) → start to stop-1
	•	range(start, stop, step) → with steps
"""

for i in range(1, 10, 2):
    print(i)

print("\n")

#Multiplication table
Number=int(input("Enter any number: "))
for i in range(1,11):
    print(Number * i)
    
#Guess the number
import random
predefined_number=random.randint(1,100)
while True:
    user_number=int(input("Guess the number: "))
    if user_number<predefined_number:
        print("Too low!")
    elif user_number>predefined_number:
        print("Too high!")
    else:
        print("You guessed it!")
        break
            