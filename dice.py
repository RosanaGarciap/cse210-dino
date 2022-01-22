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

    # Function constructor for class Player
    ''' A method that initializa an instance of the class Dine 
        each dine have six edges with values from 1 to 6.
    '''
    def __init__(self):
        
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
        '''An abstract template representation of a Games of Dine.
        Each Game needs a Player and five Dines.
        '''
        self.player = player
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.dice3 = Dice()
        self.dice4 = Dice()
        self.dice5 = Dice()

    def calculate_score(self, dices):
        '''This method increas the score of the Game's player 100 points by each dine with value 1, 
        and 50 points by each dine with value 5, for both cases the number of win cases increase in 1

        Arguments: 
            - dices: a set of 5 intergers that represent the current values on the top edge of 5 dices. 
        '''
        # Case variable represents the number of times 1 and 5 appears in the dices set
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
        '''This method keeps the control flow of the game. As long as the user wishes to play and the dices
        retrive 1's or 5's the game continue. If the user decides to quit or the dices don't show 1s or 5's
        the game finish.

        Arguments: 
            - self: this argument is a pointer to the current object 
        '''

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
            print("Invalid input, try again and follow the instructions.\n")
            return True

    def start_playing(self):
        '''This method assures the game will continue until the function Keep_playing returns False
        making the game finish.

        Arguments: 
            - self: this argument is a pointer to the current object 
        '''
        keep_throwing = True
        while(keep_throwing):
            keep_throwing = self.keep_playing()
        
def main():
    '''This is the main funtion and is responsible of initialize the Player and the Game.
    
        Arguments: None
    '''
    player1 = Player()
    play = Game(player1)
    play.start_playing()

if __name__ == "__main__":
    main()
