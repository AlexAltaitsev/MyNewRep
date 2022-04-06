from random import random
from re import I, M
from telnetlib import GA
from tkinter import N
from unicodedata import name

    

class GameCharacter():
    def  __init__(self, name, gender, race) -> None:
        self.name = name
        self.gender = gender
        self.race = race

    def greeting(self):
            if self.gender is 'Male':
                print(f'Welcome warrior. You are {self.race}, that says a lot.')
            if self.gender is 'Female':
                print(f'Hello warrior. Glad to have {self.race} on our side')
            if self.gender is random:
                print(f'I cant figure out who you are {self.race}')
                

class TheСharacter(GameCharacter):
    def __init__(self, name, gender, race) -> None:
        super().__init__(name, gender, race)
        
    def greeting_v2(self):
        print(f'Welcome {self.name} to our world')



class Human:
    def person(self):
        print('I am a Human')

class Gamer(Human):
    def __init__(self, name) -> None:
        self.name = name
    
    def nameing(self):
        print(f'My name is {self.name}, and i love playing games')
    
    def person(self):
        print('I am a Gamer')

    
        


if __name__ == '__main__':

    nord_character = GameCharacter(
        'Geralt',
        'Male',
        'Nord'
    )

    nord_character.greeting()


    nord_character = TheСharacter(
        'Alex', None, None
    )
    nord_character.greeting_v2()
    
#-----------------------------------------------------------------------------------
        
    human = Human()
    human.person()
    gamer = Gamer(None) 
    gamer.person()
   
"""Вроде как сделал но есть сомнения в правильности, и постоянно кидало ошибку
        в переодпередление, решил сделать через другой класс """

   
    

    
    
    
