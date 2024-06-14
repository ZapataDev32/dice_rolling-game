# combat.py
import time

from dice import roll_dice, generate_dice_faces_diagram
from characters import Character  

def attack(attacker, defender, num_dice, prepped_defense=0):
    roll_results = roll_dice(num_dice)
    dice_face_diagram = generate_dice_faces_diagram(roll_results)
    damage = sum(roll_results)

    print(f"{attacker.name} attacks {defender.name}!")
    print(dice_face_diagram)
    time.sleep(1.5)
    
    net_damage = defender.take_damage(damage, prepped_defense)
    if prepped_defense > 0:
        print(f"Total damage: {damage}, reduced by defense to {net_damage}")
    else:
        print(f"Total damage: {damage}")
    print(f"{defender.name} has {defender.health} health remaining.\n")
    time.sleep(1.5)

    return net_damage  # Return this if you need to check for effects based on the damage dealt
