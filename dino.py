



class Dinosaur:
    
     
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power   # Since attack_power is defined in Battlefield module, how can I pull that info to be used in Robot attack function?
        self.health = 100
        pass

    def attack(self, robot):
        
        print(f'{self.name} attacks {self.robot.name} for {self.attack_power} damage! ')
        self.robot_health_remaining = (self.robot.health) - (self.attack_power)
        print(f'{self.robot.name} has {self.robot_health_remaining} health remaining! ')
        pass

        