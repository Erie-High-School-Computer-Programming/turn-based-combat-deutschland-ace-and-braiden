import sys

# Create a game that allows players to choose between multiple characters
# and fight against each other. The game should have a simple combat system
# where characters can deal damage to each other. The game should also have
# a way to display the current health of each character.

# The game should have turned based combat where each player takes turns
# Players should have an attack, defense, and health stat

# Combat should involve a level of randomness.

# The game should have a way to display the current health of each character after each turn.

# Combat should continue until one of the characters health reaches 0.

# The game should have a way to display the winner of the game.

# The game should have a way to restart the game.

# The game should have a way to exit the game.

class Game:
    def __init__(self):
        """Initializes the game,
        It should give the game a list of at least 4 characters to choose from
        It should also give the game a list of moves for each character
        It should show player a list of characters to choose from
        and allow them to select a character,
        then have the computer choose a character at random
        It should randomly select a player to go first"""
        pass

    def turn(self, current_turn):
        """This method should show the current health of both players, 
        and allow the player to select a move to use on the opponent
        If it is the computer player's turn, it should select a move at random"""
        pass

    def check_winner(self):
        def check_winner(self):
            if self.player1_health <= 0:
                print("A.I. wins!")
            elif self.computer_health <= 0:
                print("Player wins!")

    def restart(self):
        #resets player health##
        self.player_health = 100
        self.computer_health = 100
        print("game restarted.")


    def exit(self):
        sys.exit()


    
def main():
    pass