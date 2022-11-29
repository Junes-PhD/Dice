import random

class sides:
    def __init__(self, sides) -> None:
        self.sides = sides
        self.results = {}
        self.reset()

    def __str__(self):
        return str(self.results)

    def sides_check(self, number):
        if number > 0 and number <= self.sides:
            return number
        else:
            print("Invalid Dice Side Number")
            return 0

    def reset(self):
        self.results = {}
        for n in range(self.sides):
            self.results[n + 1] = 0
        # print(self.results)

    def roll(self, rolls):
        print("Rolling", rolls, "dice")
        self.reset()
        for n in range(rolls):
            trial = random.randint(1, self.sides)
            self.results[trial] += 1
        return self.results

    def reroll_single(self, number):
        number = self.sides_check(number)
        if not number:
            return
        print("Re-rolling ", number, "'s", sep="")
        rerolls = self.results[number]
        self.results[number] = 0
        for n in range(rerolls):
            trial = random.randint(1, self.sides)
            self.results[trial] += 1
        return self.results

    def reroll_failed(self, number):
        number = self.sides_check(number)
        if not number:
            return
        print("Re-rolling ", number, "+ fails", sep="")
        rerolls = 0
        for n in range(number - 1):
            rerolls += self.results[n + 1]
            self.results[n + 1] = 0
        for n in range(rerolls):
            trial = random.randint(1, self.sides)
            self.results[trial] += 1
        return self.results

    def reroll_fish(self):
        print("Fishing for 6's")
        rerolls = 0
        for n in range(6 - 1):
            rerolls += self.results[n + 1]
            self.results[n + 1] = 0
        for n in range(rerolls):
            trial = random.randint(1, self.sides)
            self.results[trial] += 1
        return self.results

    def num_plus(self, number):
        number = self.sides_check(number)
        if not number:
            return
        successes = 0
        for n in range(number, self.sides + 1):
            successes += self.results[n]
        return successes

    def num_minus(self, number):
        number = self.sides_check(number)
        if not number:
            return
        successes = 0
        for n in range(1, number):
            successes += self.results[n]
        return successes