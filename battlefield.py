
from robo import Robot
from dino import Dinosaur


class Battlefield:
      
      
   # robot = Robot("Bender")
   # dinosaur = Dinosaur("Godzilla", 50)
   # dinosaur.attack(robot)
   # robot.attack(dinosaur)
 
   
   def __init__(self):
      self.robot = Robot("Bender").attack()
      self.dinosaur = Dinosaur("Godzilla", 50).attack()
     
         
   def run_game(self):
      input('If you are ready to begin, press "Enter" ')
      self.display_welcome()

   def display_welcome(self):
         print('\nWelcome to the battle of the ages! \nOnly one can win!\n')     # \n allows their to be a break in the line 
         

   def battle_phase(self):     
   
      print(f'{self.name} attacks {self.robot.name} for {self.attack_power} damage! ')
      print(f'{self.robot.name} has {self.robot.health - self.attack_power} health remaining! ')

          
      print(f'{self.name} attacked {self.dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} damage!')
      print(f'{self.dinosaur.name} has {self.dinosaur.health - self.active_weapon.attack_power} health remaining! ')

      print(f'{self.name} attacks {self.robot.name} for {self.attack_power} damage! ')
      print(f'{self.robot.name} has {self.robot.health - self.attack_power} health remaining! ')

      print(f'{self.name} attacked {self.dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} damage!')
      print(f'{self.dinosaur.name} has {self.dinosaur.health - self.active_weapon.attack_power} health remaining! ')




   
   def display_winner(self):
      if self.dinosaur.health == 0:
         print(f'{self.robot.name} has emerged victorious!' )
      else:
         print(f'{self.dinosaur.name} has emerged victorious! ')

    
   

   
