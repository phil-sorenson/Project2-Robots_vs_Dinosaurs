
from weapon import Weapon




class Robot:

   
  
    def __init__(self, name):
        self.name = name
        self.health = 100            # Should Health be left open bracket? or should I set a health?
        self.active_weapon = Weapon('Lazer Beam', 50)
        pass
         
    
    def attack_dino(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        if dinosaur.health > 0:
            print(f'{self.name} attacked {self.dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} damage!')
            print(f'{dinosaur.name} health is now {dinosaur.health}' )
    

       
        
        
        
       
        

        

        

        

                                       

        

   # QQQ since 'dinosaur' is parameter, we will have to be re-calling it elsewhere (maybe battlefield attack sequence?)
   # QQQ Since attack_power is defined in Battlefield module, how can I pull that info to be used in Robot attack function?
        
        




    
        
        