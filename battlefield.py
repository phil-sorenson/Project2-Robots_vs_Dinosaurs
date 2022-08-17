
from robo import Robot
from dino import Dinosaur
from weapon import Weapon

class Battlefield:
      
      
   robot = Robot("Bender")
   dinosaur = Dinosaur("Godzilla", 50)
   dinosaur.attack(robot)
   robot.attack(dinosaur)
 
   
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
      if self.robot.health == 100:
         print(f'{self.dinosaur.name} attacks {self.robot.name} for {self.dinosaur.attack_power} damage! ')
         print(f'{self.robot.name} has {self.robot.health - self.dinosaur.attack_power} health remaining! ')
         
        
          
      print(f'{self.robot.name} attacked {self.dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} damage!')
      print(f'{self.dinosaur.name} has {self.dinosaur.health - self.active_weapon.attack_power} health remaining! ')

      print(f'{self.dinosaur.name} attacks {self.robot.name} for {self.attack_power} damage! ')
      print(f'{self.robot.name} has {self.robot.health - self.attack_power} health remaining! ')

      print(f'{self.name} attacked {self.dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} damage!')
      print(f'{self.dinosaur.name} has {self.dinosaur.health - self.active_weapon.attack_power} health remaining! ')




   
   def display_winner(self):
      if self.dinosaur.health == 0:
         print(f'{self.robot.name} has emerged victorious!' )
      else:
         print(f'{self.dinosaur.name} has emerged victorious! ')

    
   

   
