class Player:
    def __init__(self, name, atk, pwr, hp, moves, defn):
        self.name = name
        self.atk = atk
        self.pwr = pwr
        self.hp = hp
        self.moves = moves
        self.defn = defn
 
def attack(self, move, target):
    move_index = self.player.moves.index(move)
    move_power = self.player.defn[move_index]
    target.hp -= 10 + move_power + self.player.atk - target.defn[1]
    
 
    def display_stats(self):
        print(self.hp)
        