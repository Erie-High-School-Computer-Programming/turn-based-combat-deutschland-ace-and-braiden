class Player:
    def __init__(self, name, atk, defn, hp, movelist):
        self.name = name
        self.atk = atk
        self.defn = defn
        self.hp = hp
        self.movelist = movelist


    def attack(self, move, target):
        self.move = move
        self.target = target
        target.hp -= 10+move.pwr+self.atk-(target.defn*2)

    def display_stats(self):
        print(self.hp)



