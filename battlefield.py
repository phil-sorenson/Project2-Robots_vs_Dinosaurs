
from robo import Robot
from dino import Dinosaur


class Battlefield:
      
      
   robot = Robot("Bender")
   dinosaur = Dinosaur("Godzilla", 50)
   # dinosaur.attack_robot(robot)
   # robot.attack_dino(dinosaur)
 
   
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
         # print(f'{self.dinosaur.name} attacks {self.robot.name} for {self.dinosaur.attack_power} damage! ')
         # print(f'{self.robot.name} has {self.robot.health - self.dinosaur.attack_power} health remaining! ')
         self.robot.attack_dino(self.dinosaur)
         self.dinosaur.attack_robot(self.robot)
         self.robot.attack_dino(self.dinosaur)
        
          
      

      

      




   
   def display_winner(self):
      if self.dinosaur.health == 0:
         print(f'{self.robot.name} has emerged victorious!' )
      else:
         print(f'{self.dinosaur.name} has emerged victorious! ')

    
   

   
