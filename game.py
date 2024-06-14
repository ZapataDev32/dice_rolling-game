
from characters import Character
from combat import attack

def game_loop(player, monster):
    while player.is_alive() and monster.is_alive():
        player_action = input("Choose your action: [attack] or [defend] ")
        if player_action.lower() == "attack":
            attack(player, monster, 2)  # Example: player rolls 2 dice when attacking
        elif player_action.lower() == "defend":
            player.defend()

        if monster.is_alive():
            monster_choice = "attack"  # Simplified for example
            if monster_choice == "attack":
                attack(monster, player, 1)
            elif monster_choice == "defend":
                monster.defend()

        if not player.is_alive():
            print("You have been defeated!")
        elif not monster.is_alive():
            print("You defeated the monster!")

# Initialize characters
player = Character("Hero", 30)
monster = Character("Goblin", 20)

# Start the game
game_loop(player, monster)
