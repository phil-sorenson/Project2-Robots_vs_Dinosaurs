
from robo import Robot
from dino import Dinosaur


class Battlefield:
      
      
   robot = Robot("Bender")
   dinosaur = Dinosaur("Godzilla", 50)

 
   
   def __init__(self):
      self.dinosaur = Dinosaur("Godzilla", 50)
      self.robot = Robot("Bender")
         
   def run_game(self):

      input('If you are ready to begin, press "Enter" ')
      self.display_welcome()
      self.battle_phase()
      self.display_winner()

   def display_welcome(self):
         print('\nWelcome to the battle of the ages! \nOnly one can win!\n')     # \n allows their to be a break in the line 
         

   def battle_phase(self):     
      while self.robot.health > 0 and self.dinosaur.health > 0:
         self.robot.attack_dino(self.dinosaur)
         if self.dinosaur.health == 0:
            self.display_winner()
            break
         self.dinosaur.attack_robot(self.robot)
         if self.robot.health == 0:
            self.display_winner()
            break
            
         
        
   def display_winner(self):
      if self.robot.health == 0:
         print(f'{self.dinosaur.name} has emerged victorious! ')
      elif self.dinosaur.health == 0:
         print(f'{self.robot.name} has emergerd victorious! ')
      
   
         
       

      
    
      
         
      
      
         
        
      
         
         

        
        
      
      
      


   

    
   

   
