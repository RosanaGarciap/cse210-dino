'''
Assignment: Game Dice
Author: Rosana Garcia
Course: CSE 210
'''

# import random
import random

class Dice():
    '''A Class that represents a dines.
    '''
    def __init__(self):
        '''A method that initializa an instance of the class Dine 
            each dine have six edges with values from 1 to 6.
        '''
        self.values = [1, 2, 3, 4, 5, 6]
        
    def get_value(self):
        '''A method that displays the dine's value after been throwed 
        '''
        # prints a random value from the list
        return random.choice(self.values)
        
class Player():
    '''An abstract template representation of a Games's Player. The
    responsibility of a Player is to play a game and throw the Dines.
    '''
    # class constructor
    def __init__(self):
        self.name = ""
        self.score = 0

    def throw_dice(self, dice1, dice2, dice3, dice4, dice5):
        '''A method that simulates the player action of tgrow dines 
        the resulting values after been "throwed" are updated in each indiviual Dine.
        '''
        d1 = dice1.get_value()
        d2 = dice2.get_value()
        d3 = dice3.get_value()
        d4 = dice4.get_value()
        d5 = dice5.get_value()
        return [d1, d2, d3, d4, d5]

class Game():
    '''An abstract template representation of a Games of Dine.
    Each Game needs a Player and five Dines.
    '''
    def __init__(self, player):
        self.player = player
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.dice3 = Dice()
        self.dice4 = Dice()
        self.dice5 = Dice()

    def calculate_score(self, dices):
        cases = 0
        for val in dices:
            if(val == 1):
                self.player.score = self.player.score + 100
                cases = cases + 1
            elif(val == 5):
                self.player.score = self.player.score + 50
                cases = cases+1
        return cases

    def keep_playing(self):
        val = input("Roll dice? [y/n] ")
        if(val == "y" or val == "yes"):
            dices_values = self.player.throw_dice(self.dice1, self.dice2, self.dice3, self.dice4, self.dice5)
            print("You rolled: %d %d %d %d %d" %(dices_values[0],dices_values[1],dices_values[2],dices_values[3],dices_values[4])) 
            if(self.calculate_score(dices_values) == 0):
                print("You score is: %d \n" %(self.player.score))
                return False
            else:
                print("You score is: %d \n" %(self.player.score))
                return True
        elif(val == "n" or val == "no"):
            return False
        else:
            print("Invalid input, try again and follow the instructions.")

    def start_playing(self):
        keep_throwing = True
        while(keep_throwing):
            keep_throwing = self.keep_playing()
        
def main():
    player1 = Player()
    play = Game(player1)
    play.start_playing()
main()
