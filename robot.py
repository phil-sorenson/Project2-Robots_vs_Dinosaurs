class Robot:

    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.active_weapon = weapon
        pass


    def attack(self):
        