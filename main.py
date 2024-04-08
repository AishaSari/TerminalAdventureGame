import random

name = input('Your name is:  ')

print("You're an average student trying to get through the day. Choose how you want to behave and see how your day turns out!")

#Q1
print("You wake up late for school and rush to get ready. You could either shower and possibly be late, or show up to school a little stinky. What do you do?")
print("     1) Shower")
print("     2) Show up stinky")
q1 = int(input())

popularity = 20
attitude = 20
appearance = 20

if q1 == 1:
    popularity += 2
    tardy = random.randint(0, 1)
    if tardy > 0.5:
        print("You barely made it to class!")
    else:
        print("You were twenty minutes late and tripped when running into class.")
        popularity -= 4
elif q1 == 2:
    popularity -= 2
    appearance -= 4
    print("The air had a certain stench, and everyone realized it was coming from you with your greasy hair.")
else:
    q1 = int(input("Enter a valid number:"))

#Q2
print("The teacher starts the class and you realize that you didn't bring a pen! Who will you ask to borrow one from?")
print("     1) Shower")
print("     2) Show up stinky")
q1 = int(input())

popularity = 20
attitude = 20
appearance = 20

if q1 == 1:
    popularity += 2
    tardy = random.randint(0, 1)
    if tardy > 0.5:
        print("You barely made it to class!")
    else:
        print("You were twenty minutes late and tripped when running into class.")
        popularity -= 4
elif q1 == 2:
    popularity -= 2
    appearance -= 4
    print("The air had a certain stench, and everyone realized it was coming from you with your greasy hair.")
else:
    q1 = int(input("Enter a valid number:"))
