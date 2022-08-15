from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    
    robot = Robot("Bender")
    dinosaur = Dinosaur("Godzilla", 50) # QQQ What is the best way instantiate the robot and dino? This? or with the __init__ function
    
    def __init__(self):
       self.robot = Robot('Bender')
       self.dinosaur = Dinosaur('Godzilla', 50)
    


    def run_game(self):
        



    def display_welcome(self):
        print('\nWelcome to the battle of the ages! \nOnly one can win!\n')     # \n allows their to be a break in the line 

    
    def battle_phase(self):
       
        


    def display_winner(self):
        self.winner