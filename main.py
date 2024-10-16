import sys
import random
from player import Player






class Game:
    def __init__(self):
        self.player_turn = True
        self.player = None
        self.computer = None

        warrior = Player("Waldo", 10, 5, 100, ["stab", "slash"], [20, 30])
        archer = Player("Alex", 5, 3, 100, ["stab", "shoot"], [15, 25])
        wizard = Player("Wilmoth", 5, 1, 100, ["slap", "magicmissile"], [1, 60])
        rogue = Player("Remy", 15, 7, 200, ["stab", "rararatsputin"], [20, 80])



    def turn(self):
        if self.player_turn:
            player_move_index = int(input("Choose a move (0: first move, 1: second move): "))
            player_move = self.player.moves[player_move_index]
            if player_move == "quit":
                self.exit()
            self.attack(player_move, self.computer)
            self.player_turn = False
        else:
            computer_move = '1'
            self.attack(computer_move, self.player)
            self.player_turn = True
        print(self.player.moves)
        print(self.computer.moves)
        self.player.hp -= 10
        print(self.player.hp)
        print(self.computer.hp)


    def attack(self, move, target):
        if move == 'q':
            exit()
        elif move in self.player.moves:
            move_index = self.player.moves.index(move)
            move_power = self.player.defn[move_index]
            target.hp -= 10 + move_power + self.player.atk - target.defn[1]
        else:
            print("Invalid move selected. Please choose a valid move.")

    def check_winner(self):
        if self.player.hp <= 0:
            print("Computer AI wins!")
            self.playing == False
        elif self.computer.hp <= 0:
            print("Player wins!")
            self.playing == False

    def restart(self):
        self.player.hp = 100
        self.computer.hp = 100
        print("Game restarted.")

    def exit(self):
        print("Exiting Game...")
        print("Game Closed Successfully.")
        sys.exit()

    def run(self):
        player_choice = int(input("Choose your character (0: Waldo, 1: Alex, 2: Wilmoth, 3: Remy:) > "))
        characters = [
            Player("Waldo", 10, 5, 100, ["stab", "slash"], [20, 30]),
            Player("Alex", 5, 3, 100, ["stab", "shoot"], [15, 25]),
            Player("Wilmoth", 5, 1, 100, ["slap", "magicmissile"], [1, 60]),
            Player("Remy", 15, 7, 200, ["stab", "rararatsputin"], [20, 80]),
            Player("HitMan", 20, 15,  900, ["shoot","Tactical nuke"], [90,169])
        ]

        self.player = characters[player_choice]
        characters.remove(self.player)  # Remove the player's choice from available characters
        self.computer = random.choice(characters)



        print(f"Player: {self.player.name}")
        print(f"Computer: {self.computer.name}")

        self.playing = True
        while self.playing:
            self.turn()
            self.check_winner()


def main():
    game = Game()
    game.run()

main()