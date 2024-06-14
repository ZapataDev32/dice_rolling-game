# combat.py
import time

from dice import roll_dice, generate_dice_faces_diagram
from characters import Character  

def attack(attacker, defender, num_dice):
    roll_results = roll_dice(num_dice)
    dice_face_diagram = generate_dice_faces_diagram(roll_results)
    damage = sum(roll_results)

    print(f"{attacker.name} prepares to attack {defender.name}!")
    time.sleep(1)
    print(dice_face_diagram)  # Displaying the dice art
    time.sleep(1.5)

    # print(f"Total damage: {damage}")
    # time.sleep(1)
    # defender.take_damage(damage)

    total_defense = defender.defend()  # Defender rolls for defense
    actual_damage = defender.take_damage(damage, total_defense)

    print(f"Total damage: {damage}, reduced by defense to {actual_damage}")
    print(f"{defender.name} has {defender.health} health remaining.\n")
    time.sleep(1.5)

    # print(f"{defender.name} takes {damage} damage! {defender.name} has {defender.health} health remaining.\n")
    # time.sleep(1.5)
