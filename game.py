
from characters import Character
from combat import attack

def game_loop(player, monster):
    player_defense = 0
    monster_defense = 0

    while player.is_alive() and monster.is_alive():
        player_action = input("Choose your action: [attack] or [defend] ")
        if player_action.lower() == "attack":
            attack(player, monster, 2, monster_defense)
            monster_defense = 0  # Reset defense after it's used
        elif player_action.lower() == "defend":
            player_defense = player.defend()  # Set up defense for the next round

        if monster.is_alive():
            monster_choice = "attack"  # Monster strategy (simplified)
            if monster_choice == "attack":
                attack(monster, player, 1, player_defense)
                player_defense = 0  # Reset defense after it's used
            elif monster_choice == "defend":
                monster_defense = monster.defend()

        if not player.is_alive():
            print("You have been defeated!")
        elif not monster.is_alive():
            print("You defeated the monster!")

# Initialize characters
player = Character("Hero", 30)
monster = Character("Goblin", 20)

# Start the game
game_loop(player, monster)
