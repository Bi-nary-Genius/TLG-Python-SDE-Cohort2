#MODULE
import random


globin = 6
hero = 10

hero_damage = random.randint(1,8)
globin_damage = random.randint(1,6)

# Module.Function()

print(f"The hero attacks dealing {hero_damage} points of damage! The globin is now at {globin - hero_damage} health!")
