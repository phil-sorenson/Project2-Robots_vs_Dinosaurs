
from weapon import Weapon




class Robot:
    
  
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Lazer Beam', 50)
        pass
         
    
    def attack(self, dinosaur):
        print(f'{self.name} attacked {dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} damage!')
        print(f'{dinosaur.name} has {dinosaur.health - self.active_weapon.attack_power} health remaining! ')
         
       
        
    
        

        

        

                                       

        

   # QQQ since 'dinosaur' is parameter, we will have to be re-calling it elsewhere (maybe battlefield attack sequence?)
   # QQQ Since attack_power is defined in Battlefield module, how can I pull that info to be used in Robot attack function?
        
        




    
        
        