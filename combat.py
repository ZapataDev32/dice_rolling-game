# combat.py
from dice import roll_dice, generate_dice_faces_diagram
from characters import Character  

def attack(attacker, defender, num_dice):
    roll_results = roll_dice(num_dice)
    dice_face_diagram = generate_dice_faces_diagram(roll_results)
    damage = sum(roll_results)

    print(f"{attacker.name} prepares to attack {defender.name}!")
    print(dice_face_diagram)  # Displaying the dice art
    print(f"Total damage: {damage}")

    defender.take_damage(damage)
    print(f"{defender.name} takes {damage} damage! {defender.name} has {defender.health} health remaining.\n")
