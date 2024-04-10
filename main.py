import random

print("You're a normal student trying to get through the day. Choose your actions, test your luck, and see how your day turns out!")

emma = 10
mia = 5
valentina = 10

#Q1
print("You wake up late for school and rush to get ready. ")
print("You could either shower and possibly be late, or show up to school a little stinky. What do you do?")
print("     1) Shower")
print("     2) Show up stinky")

while True:
    q1 = int(input())
    if q1 == 1:
        tardy = random.randint(0, 1)
        if tardy > 0:
            print("You barely made it to class!")
        else:
            emma -= 1
            print("You were twenty minutes late and tripped when running into class.")
        break
    elif q1 == 2:
        print("The air had a certain stench, and everyone realized it was coming from you with your greasy hair.")
        emma -= 1
        mia -= 1
        valentina -= 1
        break
    else:
        print("Enter a valid number: ")

#Q2
print("The teacher is handing out quizzes and you realize that you didn't bring a pen!")
print("Who will you ask to borrow one from?")
print("     1) The popular girl, Emma")
print("     2) The emo kid, Mia")
print("     3) The try-hard, Valentina")

while True:
    q2 = int(input())
    if q2 == 1:
        if q1 == 2:
            emma -= 2
            print("She hands it to you but makes a face once she smells your stench.")
        else:
            emma += 3
            print("She hands it to you and gives you a smile.")
        print("She sprays some perfume on herself and you smell it. What do you say?")
        print("     1) That smells really good.")
        print("     2) Oh my god, is that the Chanel No. 5? My favorite!")
        while True:
            q2a = int(input())
            if q2a == 1:
                emma += 5
                print("Thank you! It was really expensive.")
                break
            elif q2a == 2:
                emma -= 2
                print("Uhuh... Cool...")
                break
            else:
                print("Enter a valid number.")
        break
    elif q2 == 2:
        print("She sees that you are wearing a Radiohead shirt. She asks you name your favorite song.")
        print("     1) Creep")
        print("     2) How to disappear")
        while True:
            q2b = int(input())
            if q2b == 1:
                mia -= 3
                print("You tell her it was 'Creep' and she reluctantly hands you the pen, looking disappointed")
                break
            elif q2b == 2:
                mia += 4
                print("You told her it was 'How to disappear' and she smiled and said it was also her favorite.")
                break
            else:
                print("Enter a valid number: ")
        break
    elif q2 == 3:
        print("She shows you her pen collection and ask you to pick a color.")
        print("     1) Black")
        print("     2) Pink")
        while True:
            q2c = int(input())
            if q2c == 1:
                valentina += 5
                print("she tells you that you chose well and that it's her most expensive pen")
                break
            elif q2c == 2 :
                print("She's baffled and asks why in the world would you not choose black. What do you tell her?")
                print("     1) Why do you even care?")
                print("     2) I just really like pink.")
                q2c_a = int(input())
                if q2c_a == 1:
                    valentina -= 6
                    print("She looks embarrassed and said that she was just curious.")
                    break
                elif q2c_a == 2:
                    valentina += 10
                    print("Pink is my favorite color too! We're so similar!")
                else:
                    print("Enter a valid number: ")
                break
            else:
                print("Enter a valid number: ")
        break
    else:
        print("Enter a valid number: ")
    break

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

while True:
    q3 = int(input())
    if q3 == 1:
        if emma > 7:
            print("She makes space for you and asks you for her pen back.")
            pen = random.randint(0, 1)
            if pen > 0:
                emma -= 4
                print("You checked all your pockets and can't find it. She looks annoyed and says it's fine. It's not.")
            else:
                emma += 6
                print("You took her pen from your pocket and gave it to her. She thanks you for actually returning it.")
            break
        else:
            emma -= 2
            print("They are all really confused on why you're sitting there and decide to just ignore you.")
        break
    elif q3 == 2:
        if mia > 8:
            print("She says hi and shows you her weird, cary drawings. It looks like there's real blood on it.")
            print("What do you say?")
            print("     1) I love how raw and emotional it is.")
            print("     2) Is that real fucking blood?")

            while True:
                q3b = int(input())
                if q3b == 1:
                    mia += 6
                    print("She thanks you and tells you that was the idea.")
                    break
                elif q3b == 2:
                    mia -= 5
                    print("She looks ashamed and says yes. She doesn't speak to you the rest of the time.")
                    break
                else:
                    print("Enter a valid number.")
        else:
            mia -= 2
            print("She tells you that she would rather sit alone. You find an empty table to eat lunch at.")
        break
    elif q3 == 3:
        print("She waves at you excitedly and tell you to help her with her essay.")
        print("She asks you what you think she should change.")
        print("You don't actually know, so you say the first thing you think of.")
        essay = random.randint(0, 1)
        if essay > 0:
            valentina -= 3
            print("You tell her to change her font size to 15. She shakes her head and ignores you the whole lunch.")
        else:
            valentina += 7
            print("You help her rephrase her thesis statement. She nods in agreement.")
        break
    else:
        print("Enter a valid number: ")

#Q4
print("It's the end of the day, and since you're tired of being single, you're gonna ask for a girl's number.")
print("Who's number will you ask for?")
print("     1) Emma")
print("     2) Mia")
print("     3) Valentina")

while True:
    q4 = int(input())
    if q4 == 1:
        if emma > 10:
            print("She types her number into your phone and tells you to call her. You win!")
        else:
            print("She tells you that you're not her type. You lose.")
        break
    elif q4 == 2:
        if mia > 12:
            print("She meekly smiles and slips a piece of paper with her number on it. You win!")
        else:
            print("She tells you that she had something to do and left. She never came back. You lose.")
        break
    elif q4 == 3:
        if valentina > 10:
            print("She jumps in excitement and types her number into your phone. You win!")
        else:
            print("She tells you that she's not interested in doing your homework for you. You lose.")
        break
    else:
        print("Enter a valid number: ")
print(emma)
print(mia)
print(valentina)