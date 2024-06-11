
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        self.health = max(self.health, 0)

    def __str__(self):
        return f"{self.name} with {self.health} health left."
