from weapon import Weapon
from dino import Dinosaur

class Robot:

    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Lazer Beam', 50)
        pass
         
    
    def attack(self, dinosaur):
        self.dinosaur = Dinosaur('Godzilla', 50)
        print(f'{self.name} attacked {self.dinosaur.name} with {self.active_weapon} for {self.active_weapon.attack_power} damage!')
        self.dino_health_remaining = (self.dinosaur.health) - (self.active_weapon.attack_power)
        print(f'{self.dinosaur.name} has {self.dino_health_remaining} health remaining!')
    
        

        

        

                                       

        

   # QQQ since 'dinosaur' is parameter, we will have to be re-calling it elsewhere (maybe battlefield attack sequence?)
   # QQQ Since attack_power is defined in Battlefield module, how can I pull that info to be used in Robot attack function?
        
        




    
        
        