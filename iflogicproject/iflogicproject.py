#!/usr/bin/env python3

# Are you a Camper or Glamper?

round = 0
camper_score = 0
glamper_score = 0

# so the whole game is in this while loop, and it ends when the max rounds are reached
# and depending on what round it is, that's what question you get asked
# so almost alllll of these lines need indented under line 12 
while round <2:
    round += 1

    if round == 1:
        print("On your camping trip to the Smokey Mountains, you bring what item to carry your belongings? ")

        answer = input("Choose your preferrence (backpack or suitcase): ")

        if answer == "backpack":
            print("You sound like a camper! ")
            camper_score += 1

        elif answer == "suitcase":
            print("You sound like a glamper! ")
            glamper_score += 1

        else:
            print("Chile, that is not even an option!")

    # all the text below is pink because there must be an absent or mis-matched quotation mark somewhere
    elif round == 2:
        print("For your day hike to Mount Leconte, you wear the following footwear? ") # <<-- here it is; you start with a " but end with a '
        answer = input("Choose your preference (hiking boots or Gucci sneakers): ")
        
        if answer == "hiking boots":
            print("You sound like a camper! ")
            camper_score += 1

        if answer == "Gucci Sneakers ":
            print("You sound like a glamper! ")
            glamper_score +1

        # round ==3:
        # print("



