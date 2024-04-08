import random

print("You're a normal student trying to get through the day. Choose your actions, test your luck, and see how your day turns out!")

#Q1
print("You wake up late for school and rush to get ready. ")
print("You could either shower and possibly be late, or show up to school a little stinky. What do you do?")
print("     1) Shower")
print("     2) Show up stinky")
q1 = int(input())

emma = 10
mia = 5
valentina = 15

if q1 == 1:
    tardy = random.randint(0, 1)
    if tardy > 0.5:
        print("You barely made it to class!")
    else:
        print("You were twenty minutes late and tripped when running into class.")
        emma -= 1
elif q1 == 2:
    print("The air had a certain stench, and everyone realized it was coming from you with your greasy hair.")
    emma -= 1
    mia -= 1
    valentina -= 1
else:
    q1 = int(input("Enter a valid number:"))

#Q2
print("The teacher starts the class and you realize that you didn't bring a pen!")
print("Who will you ask to borrow one from?")
print("     1) The popular girl, Emma")
print("     2) The emo kid, Mia")
print("     3) The try-hard, Valentina")
q2 = int(input())

if q2 == 1:
    if q1 == 2:
        emma -= 2
        print("She hands it to you but makes a face once she smells your stench.")
    else:
        emma += 3
        print("She hands it to you and gives you a smile.")
elif q2 == 2:
    print("She sees that you are wearing a Radiohead shirt. She asks you name your favorite song.")
    song = random.randint(0, 1)
    if song > 0.5:
        mia -= 3
        print("You tell her it was 'Creep' and she reluctantly hands you the pen, looking disappointed")
    else:
        mia += 4
        print("You told her it was 'How to disappear' and she smiled and said it was also her favorite.")
elif q2 == 2:
    print("She shows you her pen collection and ask you to pick a color.")
    print("     1) Black")
    print("     2) Pink")
    q2b = int(input())
    if q2b == 1:
        valentina += 5
        print("she tells you that you chose well and that it's her most expensive pen")
    elif q2b == 2 :
        print("She's baffled and asks you how you're going to read your notes with that color. What do you tell her?")
        print("     1) Why do you even care?")
        print("     2) I just like pink.")
        q2b_a = int(input())
        if q2b_a == 1:
            valentina -= 6
            print("She looks embarrassed and said that she was just curious.")
        elif q2b_a == 2:
            valentina += 10
            print("Pink is my favorite color too! We're so similar!")
        else:
            q2b_a = int(input("Enter a valid number:"))
    else:
        q2a = int(input("Enter a valid number:"))
else:
    q1 = int(input("Enter a valid number:"))

#Q3
print("The bell rings and it's lunch time! Somehow none of your friends showed up to school today.")
print("You have to choose who to sit with, because you don't feel like sitting alone.")
print("Emma is sitting with a big group of girls. You can hear them chatting and giggling.")
print("Mia is sitting by herself with her headphones on, drawing on her notebook.")
print("Valentina is with another girl who is helping her revise her essay assignment.")
print("Who do you sit with?")
print("     1) Emma")
print("     2) Mia")
print("     3) Valentina")
q3 = int(input())

if q3 == 1:
    if emma > 7:
        print("She makes space for you and asks you for her pen back.")
    else:
        emma -= 2
        print("They are all really confused on why you're sitting there and decide to just ignore you.")
elif q3 == 2:
    if mia > 8:
        print("She says hi to you and shows you her weird, kind of scary drawings.")
    else:
        print("She tells you that she would rather sit alone. You find an empty table to eat lunch at.")
elif q3 == 3:
    print("She waves at you excitedly and tell you to help her with her essay.")
    print("She asks you what you think she should change.")
    print("You don't actually know, so you say the first thing you think of.")
    essay = random.randint(0, 1)
    if essay > 0.5:
        valentina -= 3
        print("You tell her to change her font size to 15. She shakes her head and ignores you the whole lunch.")
    else:
        valentina += 7
        print("You help her rephrase her thesis statement. She nods in agreement.")

#Q4
print("It's the end of the day, and since you're tired of being single, you're gonna ask for a girl's number.")
print("Who's number will you ask for?")
print("     1) Emma")
print("     2) Mia")
print("     3) Valentina")
q4 = int(input())

if q4 == 1:
    ff
elif q4 == 2:
    ff
elif q4 == 3:
    ff
else:
    q4 = int(input("Choose a valid number"))
print(emma)
print(mia)
print(valentina)