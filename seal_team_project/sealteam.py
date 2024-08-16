import random
import time

# The attributes of Seal Team 6: a four man team.
seal_team_6 = {
    'sniper': {'name': 'Sniper', 'weapon': None, 'supply': None, 'health': 100, 'stealth': 5, 'attack': 10},
    'rifleman': {'name': 'Rifleman', 'weapon': None, 'supply': None, 'health': 100, 'stealth': 5, 'attack': 10},
    'medic': {'name': 'Medic', 'weapon': None, 'supply': None, 'health': 100, 'stealth': 5, 'attack': 10},
    'radio_guy': {'name': 'Radio Guy', 'weapon': None, 'supply': None, 'health': 100, 'stealth': 5, 'attack': 10},
    'inventory': []
}

# The weapons and supply items will be determined by the user's ability to answer the riddle. The weapon_supply levels range from 1:4, so the lower the level, the better the weapons/items will be.
weapon_supplies = {
    1: {'sniper': {'weapon': 'Sniper Rifle', 'supply': 'Camouflage Netting'},
        'rifleman': {'weapon': 'M16', 'supply': 'Grenades'},
        'medic': {'weapon': 'First Aid Kit', 'supply': 'Medications'},
        'radio_guy': {'weapon': 'Radio', 'supply': 'Signal Flare'}},
    2: {'sniper': {'weapon': 'Hand Gun', 'supply': 'Silencer'},
        'rifleman': {'weapon': 'Hand Gun', 'supply': 'Extra Ammo'},
        'medic': {'weapon': 'Scissors', 'supply': 'Bandages'},
        'radio_guy': {'weapon': 'Cell Phone', 'supply': 'Battery Pack'}},
    3: {'sniper': {'weapon': 'Knife', 'supply': 'Night Vision Goggles'},
        'rifleman': {'weapon': 'Knife', 'supply': 'Flashlight'},
        'medic': {'weapon': 'Bottle of Peroxide', 'supply': 'Surgical Tape'},
        'radio_guy': {'weapon': 'Walkie Talkie', 'supply': 'Backup Antenna'}},
    4: {'sniper': {'weapon': 'Stun Gun', 'supply': 'Pepper Spray'},
        'rifleman': {'weapon': 'Bottle of Mace', 'supply': 'Tactical Vest'},
        'medic': {'weapon': 'Stethoscope', 'supply': 'Portable Defibrillator'},
        'radio_guy': {'weapon': '2 Plastic Cups with String', 'supply': 'Map'}}
}

# The user will be presented with riddles for each SEAL member.
riddles = {
    'sniper': {
        "In the field, I lead with might,\nBronze stars shining, a daunting sight.\nI command with rank and authority,\nWhat title am I, can you see?": "general",
        "Silent and deep, I glide beneath,\nThrough oceans vast, in shadows I breathe.\nI carry power, unseen by the eye,\nWhat am I, lurking where the waters lie?": "submarine"
    },
    'rifleman': {
        "I march with pride, my boots on the ground,\nThrough forests and deserts, I make my round.\nIn every battle, I stand my post,\nWhat am I, a defender of the coast?": "soldier",
        "In the Navy, there’s a team so grand,\nThey fight on sea, in air, and land.\nTheir name’s a mix of earth and flight,\nCan you guess this force so tight?": "seals"
    },
    'medic': {
        "If a soldier’s gone, no one can grieve,\nThey’ve wandered off without their leave.\nWhat’s the term, can you recall?\nWhen they’re missing, what do we call?": "awol",
        "In the Army, rank is high,\nFive stars shining in the sky.\nThe highest rank that you can be,\nCan you name it, what’s the key?": "admiral"
    },
    'radio_guy': {
        "I link your devices with a simple wave,\nConnecting all, strong and brave.\nWho am I?": "router",
        "I connect devices, without a wire,\nI keep the team connected, when signals are dire.\nWho am I?": "wifi router"
    }
}

# Here a function is implemented to ask a riddle and determine weapon level.
def ask_riddle(seal_member_key, seal_member):
    print(f"\n{seal_member['name']}, answer this riddle to determine your weapon and supplies level:")
    riddle, correct_answer = random.choice(list(riddles[seal_member_key].items()))
    print(riddle)

    for attempt in range(1, 5):
        answer = input(f"Attempt {attempt} - Your answer: ").strip().lower()
        if answer == correct_answer:
            print(f"Correct on attempt {attempt}! You get Level {attempt} weapons and supplies.")
            return attempt
        else:
            print("Incorrect. Let's try again.")
    print("All attempts failed. You get Level 4 weapons and supplies.")
    return 4

# Now, you can set up the team with weapons and supplies:
def setup_team():
    for member_key, member in seal_team_6.items():
        if isinstance(member, dict):
            level = ask_riddle(member_key, member)
            member['weapon'] = weapon_supplies[level][member_key]['weapon']
            member['supply'] = weapon_supplies[level][member_key]['supply']
            print(f"{member['name']} is equipped with {member['weapon']} and {member['supply']}.")

# The warehouse rooms are described:
rooms = {
    'Abandoned Loading Dock': {
        'description': "You stand at the abandoned loading dock. The air is thick with dust, and the only sound is the distant hum of machinery. You can go north.",
        'north': 'Crates and Storage Area'
    },
    'Crates and Storage Area': {
        'description': "You enter a vast storage area filled with towering crates. The rustling of big black DC rats echoes in the distance. You can go south, east, or west.",
        'south': 'Abandoned Loading Dock', 'east': 'Security Control Room', 'west': 'Employee Break Room'
    },
    'Security Control Room': {
        'description': "This room is cluttered with servers and cables. The static from an old radio crackles in the background. You can go west or north.",
        'west': 'Crates and Storage Area', 'north': 'Underground Bunker',
        'trap': 'Alarm System'
    },
    'Employee Break Room': {
        'description': "The break room's ceiling lights are flickering on and off, with overturned chairs and a leftover tuna fish sandwich on the counter. The faint whispers of hostages can be heard from somewhere nearby. You can go east.",
        'east': 'Crates and Storage Area'
    },
    'Underground Bunker': {
        'description': "Hidden beneath a secret panel, this underground bunker is dark and stinky. Most of the hostages are likely held here. You can go south.",
        'south': 'Security Control Room',
        'hostages': True
    }
}

# initialize the game:
moves = 0
rescued_hostages = 0
start_time = time.time()

# This function will display the status of the team and their current room:
def show_status(current_room):
    print('---------------------------')
    print(f'Current Room: {current_room}')
    print(rooms[current_room]['description'])
    print(f"Total Moves: {moves}")
    print(f"Hostages Rescued: {rescued_hostages}")
    print(f"Inventory: {seal_team_6['inventory']}")
    print('---------------------------')

# The team can move and their moves can be counted:
def move_team(current_room, direction):
    global moves
    if direction in rooms[current_room]:
        moves += 1
        return rooms[current_room][direction]
    else:
        print("You can't go that way!")
        return current_room

# Items in the room are searchable:
def search_room(current_room):
    if random.choice([True, False]):
        item = random.choice(['ammo', 'health pack', 'intel'])
        print(f"You found a {item}!")
        seal_team_6['inventory'].append(item)
    else:
        print("Nothing of interest found.")

# Strategy meetings option:
def strategy_meeting():
    choice = input("Do you want to split the team (yes/no)? ").lower()
    if choice == 'yes':
        print("The team splits up to cover more ground.")
        # Implement logic for split team:
    else:
        print("The team stays together.")

# A function to handle environ hazards:
def disarm_trap(current_room):
    if "trap" in rooms[current_room]:
        print(f"A {rooms[current_room]['trap']} is triggered! You must disarm it.")
        if random.choice([True, False]):
            print("Trap disarmed successfully!")
            del rooms[current_room]['trap']
        else:
            print("Failed to disarm the trap! The team takes damage.")
            for member in seal_team_6.values():
                if isinstance(member, dict):
                    member['health'] -= 10

# Here you can interrogate rescued hostages for intel:
def interrogate_hostage():
    intel = random.choice([
        "The hostages are held in the Underground Bunker.",
        "Beware of the traps in the Security Control Room.",
        "Enemies are patrolling the Crates and Storage Area."
    ])
    print(f"Hostage reveals: {intel}")
    seal_team_6['inventory'].append('intel')

# Main game loop
def main():

    global rescued_hostages
    rescued_hostages = 0

    # Mission Briefing
    print("Welcome to SEAL Team 6: Operation Silent Thunder!\n")
    print("Mission Briefing:")
    print("- Time of Day: 1930 hours")
    print("- Location: Deserted Warehouse")
    print("- Hostage Situation: 10 international diplomats have been taken hostage by a terrorist cell.")
    print("- Ransom Demand: The captors demand 20 million dollars in Bitcoin and 10 extra-large pepperoni pizzas. Failure to comply will result in the execution of the hostages.")
    print("- Mission: Infiltrate the warehouse, disarm the traps, and rescue all hostages.\n")
    print("Good luck, Commander!\n")

    # Instructions
    print("GAME INSTRUCTIONS")
    print("Commands:")
    print("  go [direction] - Move your team a specific direction (north, south, east, west).")
    print("  search - Search the current room for hidden items.")
    print("  strategy - Hold a strategy meeting to decide whether to split up the team or stay together.")
    print("  quit - Abort the mission and end the game.")
    print("Objective: Rescue all 10 hostages and complete the mission as quickly and safely as possible.\n")

    setup_team()

    current_room = 'Abandoned Loading Dock'

    while rescued_hostages < 10:
        show_status(current_room)

        # Check for hostages in the secret room
        if current_room == 'Underground Bunker' and 'hostages' in rooms[current_room]:
            print("You found the hostages! Rescue them!")
            rescued_hostages += 1
            del rooms[current_room]['hostages']
            interrogate_hostage()
            if rescued_hostages == 10:
                print("Mission Accomplished! All hostages have been rescued.")
                break

        move = input('Enter your move (go [direction], search, strategy, or quit): ').lower().split()

        if move[0] == 'go':
            current_room = move_team(current_room, move[1])
            disarm_trap(current_room)
        elif move[0] == 'search':
            search_room(current_room)
        elif move[0] == 'strategy':
            strategy_meeting()
        elif move[0] == 'quit':
            print("Mission aborted. You have opted to quit.")
            break
        else:
            print("Invalid command.")

    end_time = time.time()
    mission_time = round(end_time - start_time, 2)
    score = (rescued_hostages * 100) - (moves * 10) + (len(seal_team_6['inventory']) * 20)

    print(f"\nMission Complete!")
    print(f"Time taken: {mission_time} seconds")
    print(f"Final Score: {score}")

if __name__ == "__main__":
    main()


