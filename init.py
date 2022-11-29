import random
from array import array
import display
import buttons
import dice



class shooting:
    def __init__(self, attacker, defender) -> None:
        self.attacker = attacker
        self.defender = defender

    def __str__(self):
        pass

    def report(self):
        print(self.attacker["Name"])
        print(self.attacker["Sv"])

class manual:
    def __init__(self, attacks, skill, wound, save, mods) -> None:
        self.attacks = attacks
        self.skill = skill
        self.hits = 0
        self.wound = wound
        self.wounds = 0
        self.save = save
        self.saved = 0
        self.mods = mods

        self.d6=dice.sides(6)
        
        

    def __str__(self):
        pass

    def roll_report(self):
        #print(self.d6)
        pass

    def report(self):
        print('Hits:' , self.hits)
        print('Hit %:' , round(100*self.hits/self.attacks,1),"%")
        print('Wounds:' , self.wounds)
        print('Wound %:' , round(100*self.wounds/self.hits,1),"%")
        print('Save:' , self.saves)
        print('Save %:' , round(100*self.saves/self.wounds,1),"%")
        print('Damage:', self.wounds-self.saves, "times weapon damage")

    def hit_round(self):
        self.d6.roll(self.attacks)
        self.hits = self.d6.num_plus(self.skill)
        self.roll_report()
        return self.hits

    def wound_round(self):
        self.d6.roll(self.hits)
        self.wounds = self.d6.num_plus(self.wound)
        self.roll_report()
        return self.wounds

    def save_round(self):
        self.d6.roll(self.wounds)
        self.saves= self.d6.num_plus(self.save)
        self.roll_report()
        return self.saves

    def auto(self):
        self.hit_round()
        self.wound_round()
        self.save_round()
        self.report()

    def manual(self):
        input = buttons.user_select
        show = display.display()

        results = self.d6.roll(int(input.rolls()))
        show.terminal(results)
        n = input.dice_num()
        x = self.d6.num_plus(n)
        print("Hits:",x)
        print("Roll Dice?")
        if input.agree() == "no":
            print("exiting")
            return            
        self.d6.roll(x)
        


def main():
    d6 = dice.sides(6)
    show = display.display()
    
    dice_calc = manual(0,0,0,0,"")
    dice_calc.manual()
    
    
    #shoot = manual(10, 3, 4, 3, "")
    #shoot.auto()
    #roll_set = d6.roll(10)
    #print(roll_set)
    #show.terminal(roll_set)
    #test = shooting(p1, d1)
    #test.report()

p1 = {
    "Name": "Intercessor Squad",
    "M": 6,
    "WS": 3,
    "BS": 3,
    "S": 4,
    "T": 4,
    "W": 2,
    "A": 2,
    "Ld": 7,
    "Sv": 3,
    "Shooting": "Bolt Riftle",
    "Melee": "Knife",
}

d1 = {
    "Name": "Intercessor Sergeant",
    "M": 6,
    "WS": 3,
    "BS": 3,
    "S": 4,
    "T": 4,
    "W": 2,
    "A": 3,
    "Ld": 8,
    "Sv": 3,
    "Shooting": "Bolt Riftle",
    "Melee": "Knife",
}

guns = {
    "Plasma": {"Range": 12, "Type": "Pistol", "A":1, "S": 6, "AP": -1, "D": 1},
    "Bolt Rifle": {"Range":30, "Type": "Rapid Fire", "A":1, "S": 4, "AP": -1, "D": 1},
}

if __name__ == "__main__":
    main()
