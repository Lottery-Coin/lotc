from random import choice
from random import shuffle

class Jackpot:
    def __init__(self):
        self.jackpot = 0
        self.draw = []
        self.nums = []
    def __repr__(self):
        print(f'{self.draw}')
    
    def draw_jackpot(self):
        self.nums = [n for n in range(1, 145, 1)]
        for a in range(11):
            shuffle(self.nums)
            x = choice(self.nums)
            self.draw.append(x)
            self.nums.remove(x)
            if a == 10:
                x = choice(self.entry)
                self.draw.sort()
                self.draw.append(x)
        return f'{self.draw}'

class Rafflepot:
    def __init__(self):
        self.rafflepot = 0
        
        
