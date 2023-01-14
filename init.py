import random
from array import array
import display
import buttons
import dice
import player


class shooting:
    def __init__(self, attacker, defender) -> None:
        self.attacker = attacker
        self.defender = defender
        self.attacks = self.attacker["BA"]
        self.ballistic_skill = self.attacker["BS"]
        self.dmg = self.attacker["BH"]
        self.crit_dmg = self.attacker["BC"]
        self.ap = 0
        self.save_rolls = self.defender["DF"]
        self.save = self.defender["Sv"]
        self.hits = 0
        self.crits = 0
        self.saves = 0
        self.crit_saves = 0
        self.total_damage = 0
        self.cover = self.defender["Cover"]
        
        self.d6=dice.sides(6)
        

    def __str__(self):
        pass

    def report(self):
        print("Attacker:", self.attacker["Name"])
        print("BS:", self.attacker["BS"])
        print("Attacks:", self.attacker["BA"])
        print("DMG:", self.attacker["BH"], "/", self.attacker["BC"])

    def auto(self):
        self.hit_round(self.attacks, self.ballistic_skill)
        self.wound_round(self.hits, self.crits, self.save_rolls, self.ap, self.cover)
    
    def hit_round(self, attacks, bs, trait1="", trait2=""):
        self.d6.roll(attacks)
        self.hits, self.crits = self.d6.num_plus_with_crits(bs)
        
        print(self.d6.results)
        print("BS:", bs)
        print(self.hits, "hits")
        print(self.crits, "crits")
        
        return self.hits, self.crits

    def wound_round(self, hits, crits, save_rolls, AP, cover):

        if cover == 1:
            save_rolls -= 1

        self.d6.roll(save_rolls)
        print(self.d6.results)

        self.saves, self.crit_saves = self.d6.num_plus_with_crits(self.save)
        if cover == 1:
            self.saves += 1
        print(self.save, "+ save")
        print(self.saves, "saves")
        print(self.crit_saves, "crit saves")

        while self.crit_saves > 0:
            if crits > 0:
                self.crit_saves -= 1
                crits -= 1
            elif hits > 0:
                self.crit_saves -= 1
                hits -= 1
        while self.saves > 0:
            if self.saves >= 2 and hits <2 and crits > 0:
                self.saves -= 2
                crits -= 1
            elif self.saves > 0 and hits > 0:
                self.saves -= 1
                hits -= 1
            else:
                self.saves -= 1
        print(hits, "hits")
        print(crits, "crits")
        total_damage = hits * self.dmg + crits * self.crit_dmg
        print(total_damage, "wounds")
        return self.total_damage

    def parse_specials(self):


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
    
    shot = shooting(player.a1, player.d1)
    #shot.report()
    shot.auto()


    #d6 = dice.sides(6)
    #show = display.display()
    
    #dice_calc = manual(0,0,0,0,"")
    #dice_calc.manual()
    
    
    #shoot = manual(10, 3, 4, 3, "")
    #shoot.auto()
    #roll_set = d6.roll(10)
    #print(roll_set)
    #show.terminal(roll_set)
    #test = shooting(p1, d1)
    #test.report()


if __name__ == "__main__":
    main()
