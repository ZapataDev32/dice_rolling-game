from dice import roll_dice


class Character:
    def __init__(self, name, health, defense_dice=1):
        self.name = name
        self.health = health
        self.defense_dice = defense_dice

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage, defense=0):
        net_damage = max(damage - defense, 0) #ensuring damage cannot go negative
        self.health -= net_damage
        self.health = max(self.health, 0)
        return net_damage

    def __str__(self):
        return f"{self.name} with {self.health} health left."

    def defend(self):
        defense_roll = roll_dice(self.defense_dice)
        total_defense = sum(defense_roll)
        print(f"{self.name} defends and rolls {defense_roll} for a total defense of {total_defense}")
        return total_defense
