#char generator

import random


class WoDChar:
    def __init__(self):

        self.experience = 0

        self.attributes = {
            "Strength" : 0,
            "Dexterity" : 0,
            "Stamina" : 0,
            "Intelligence" : 0,
            "Wits" : 0,
            "Resolve" : 0,
            "Presence" : 0,
            "Manipulation" : 0,
            "Composure" : 0
            }

        self.virtue = {
            "Charity" : False,
            "Faith" : False,
            "Fortitude" : False,
            "Hope" : False,
            "Justice" : False,
            "Prudence" : False,
            "Temperance" : False
            }

        self.vice = {
            "Envy" : False,
            "Gluttony" : False,
            "Greed" : False,
            "Lust" : False,
            "Pride" : False,
            "Sloth" : False,
            "Wraith" : False
            }
        self.traits = {
            "Health" : 0,
            "Willpower" : 0,
            "Speed" : 0,
            "Size" : 0,
            "Defense" : 0,
            "Initiative" : 0,
            "Morality" : 0
            }

    def rand_att(self):
        # one dot per attribute
        a = [1]*3
        b = [1]*3
        c = [1]*3
        n = []



        # random values for a[] b[] c[]
        for i in range (5):
            n = random.randint(0,2)
            # decide whether to add the 2 points into a 5th dot
            if(a[n] == 4 and i == 3 and random.randint(0,1)):
                a[n] += 1
                break
            else:
                a[n] += 1

        for i in range (4):
            n = random.randint(0,2)
            while(b[n] == 4):
                n = random.randint(0,2)
            b[n] += 1

        for i in range (3):
            c[random.randint(0,2)] += 1

        #randomize order of stat values
        n = [a,b,c]
        random.shuffle(n)
        f = []
        for att in n:
            f.extend(att)

        #probably a better way to iterate, but works for now
        i = 0
        for stat in self.attributes:
            self.attributes[stat] = f[i]
            i+=1
        self.char_calc()
        self.virtue_gen()
        self.vice_gen()


    def virtue_gen(self):
        self.virtue[random.choice(list(self.virtue))] = True

    def vice_gen(self):
        self.vice[random.choice(list(self.vice))] = True

    def char_calc(self):
        self.traits["Size"] = 5
        self.traits["Health"] = self.traits["Size"] + self.attributes["Stamina"]
        self.traits["Willpower"] = self.attributes["Resolve"] + self.attributes["Composure"]
        self.traits["Defense"] = min(self.attributes["Dexterity"], self.attributes["Wits"])
        self.traits["Initiative"] = self.attributes["Dexterity"] + self.attributes["Composure"]
        self.traits["Speed"] = self.attributes["Strength"] + self.attributes["Dexterity"] + 5
        self.traits["Morality"] = 7

    def print_char(self):
        # @TODO finish printing sheet
        print("Experience " + str(self.experience))
        print("")
        for att in self.attributes:
            print(att + " " + str(self.attributes[att]))
        print("")
        for trait in self.traits:
            print(trait + " " + str(self.traits[trait]))
        for v in self.virtue:
            if self.virtue[v]:
                print(v)
                break
        for v in self.vice:
            if self.vice[v]:
                print(v)
                break
        
