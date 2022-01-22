# Dice Game
Dice is a game in which the player seeks to earn as many points as possible by repeatedly rolling five dice and accumulating the score until they are no longer able to continue.

## dice.py
This program has the purpose of use class definitions to simulate an actual game of Dice. To accomplish this three aspect of the game were considerate at the moment of define the 
classes. 

### Class Dice:
First, the Dice, in real life a dice have 6 edges the dice class contains then an array of length 6 with the respective values from 1 to 6. Another characteristic is the fact 
that after rolling they always show a value in the top edge, we simulate this importing the random function and aplying it over the dice values array.

### Class Player:
Second we have the Player class. The game requires a "player" and this player us who will holds the score and throw the dices, this last action was simulated by defining a function
that calls the get_value for each Dice, this function at the same time is what execute the random funcion in the dice array.

### Class Game:
Finally we have the Game, the Game is composed by rules that define it, one of this is that the Game needs a Player and five dices. A game can start and as long as the game's conditions
to continue exist the game remains active.

## How run this program:

- Download or clone the repository.
- Extract the project.
- Open a terminal and move to the with the cd command to the path where the folder was extract: $ cd "/path/to/project/folder"
- Run the file: $ python dice.py (in case you are using old versions of python 3 you must change the command to $ python3 dice.py)
