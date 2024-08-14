#!/usr/bin/env python3

# Are you a Camper or Glamper?

question = 0
camper_score = 0
glamper_score = 0

# so the whole game is in this while loop, and it ends when the max rounds are reached
# and depending on what round it is, that's what question you get asked
# so almost alllll of these lines need indented under line 12

while question <2:
    question += 1

    if question == 1:
        print("On your camping trip to the Smokey Mountains, you bring what item to carry your belongings?")
        answer = input("Choose your preferrence (backpack or suitcase): ")

        if answer == "backpack":
            print("You sound like a camper!")
            camper_score += 1

        elif answer == "suitcase":
            print("You sound like a glamper!")
            glamper_score += 1

        else:
            print("Chile, that is not even an option!")

    # all the text below is pink because there must be an absent or mis-matched quotation mark somewhere
    elif question == 2:
        print("For your day hike to Mount Leconte, you wear the following footwear? ") # <<-- here it is; you star answer = input("Choose your preference (hiking boots or Gucci sneakers): ")
        
        if answer == "hiking boots":
            print("You sound like a camper!")
            camper_score += 1

        if answer == "Gucci Sneakers ":
            print("You sound like a glamper!")
            glamper_score +1

        elif question == 3:
            print("What is your ideal fireside meal while in Shenandoah National Park?")
            answer = input("Choose your preference (weiners and s'mores or filet mignon): ")

        if answer.lower() == "weiners and s'mores":
            print("You sound like a camper!")
            camper_score += 1
        elif answer.lower() == "filet mignon":
            print("You sound like a glamper!")
            glamper_score += 1
        else:
            print("Chile, that is not even an option!")

    elif question == 4:
        print("If high winds 20 mph are expected on your camping site in Paonia. Would you use a tarp or rocks to secure your tent?")
        answer = input("Choose your preference (set up a tarp or lay rocks): ")

        if answer.lower() == "lay rocks":
            print("You sound like a camper!")
            camper_score += 1
        elif answer.lower() == "set up a tarp":
            print("You sound like a glamper!")
            glamper_score += 1
        else:
            print("Chile, that is not even an option!")

    elif question == 5:
        print("The week before camping at Sandy Pines Campground, do you check the weather forecast?")
        answer = input("Choose your preference (yes, I need to be prepared or no, I’ll just wing it): ")

        if answer.lower() == "yes, i need to be prepared":
            print("You sound like a camper!")
            camper_score += 1
        elif answer.lower() == "no, i’ll just wing it":
            print("You sound like a glamper!")
            glamper_score += 1
        else:
            print("Chile, that is not even an option!")

    elif question == 6:
        print("While exploring Shabbona Lake, do you scream at the sight of cicadas or wonder how they taste?")
        answer = input("Choose your preference (scream or wonder how they taste): ")

        if answer.lower() == "wonder how they taste":
            print("You sound like a camper!")
            camper_score += 1
        elif answer.lower() == "scream":
            print("You sound like a glamper!")
            glamper_score += 1
        else:
            print("Chile, that is not even an option!")

    elif question == 7:
        print("You are chomping on lamb chops at your cabin in Gatlinburg, TN and all of a sudden you notice a black bear charging at you. Do you reach in your pocket for your bear spray or phone?")
        answer = input("Choose your preference (bear spray  or phone): ")

        if answer.lower() == "bear spray":
            print("You sound like a camper!")
            camper_score += 1
        elif answer.lower() == "phone":
            print("You sound like a glamper!")
            glamper_score += 1
        else:
            print("Chile, that is not even an option!")


total_questions = 7

camper_percentage = (camper_score / total_questions) * 100

glamper_percentage = (glamper_score / total_questions) * 100
#figure this out
print(f"\nFinal Scores:\nCamper: {camper_percentage:.0f}%\nGlamper: {glamper_percentage:.0f}%")
