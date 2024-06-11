
from characters import Character
from combat import attack

def game_loop(player, monster):
    while player.is_alive() and monster.is_alive():
        player_action = input("Choose your action: [attack] ")
        if player_action.lower() == "attack":
            attack(player, monster, 2)  # Example: player rolls 2 dice when attacking

        if monster.is_alive():
            attack(monster, player, 1)  # Monster attacks with 1 die

        if not player.is_alive():
            print("You have been defeated!")
        elif not monster.is_alive():
            print("You defeated the monster!")

# Initialize characters
player = Character("Hero", 30)
monster = Character("Goblin", 20)

# Start the game
game_loop(player, monster)
