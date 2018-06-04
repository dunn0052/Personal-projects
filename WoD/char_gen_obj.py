#char generator
import csv
import random


class wChar:
    def __init__(self, n = None):
        
        self.name = str(n)

        self.experience = 0

        self.physical = {
            "Strength" : 0,
            "Dexterity" : 0,
            "Stamina" : 0
            }
        self.mental = {
            "Intelligence" : 0,
            "Wits" : 0,
            "Resolve" : 0
            }
        self.social = {
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
        for stat in self.physical:
            self.physical[stat] = f[i]
            i+=1
        for stat in self.mental:
            self.mental[stat] = f[i]
            i+=1
        for stat in self.social:
            self.social[stat] = f[i]
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
        self.traits["Health"] = self.traits["Size"] + self.physical["Stamina"]
        self.traits["Willpower"] = self.mental["Resolve"] + self.social["Composure"]
        self.traits["Defense"] = min(self.physical["Dexterity"], self.mental["Wits"])
        self.traits["Initiative"] = self.physical["Dexterity"] + self.social["Composure"]
        self.traits["Speed"] = self.physical["Strength"] + self.physical["Dexterity"] + 5
        self.traits["Morality"] = 7

    def print_char(self):
        # @TODO finish printing sheet
        print("Experience " + str(self.experience))
        print("")
        for att in self.physical:
            print(att + " " + str(self.physical[att]))
        print("")
        for att in self.mental:
            print(att + " " + str(self.mental[att]))
        print("")
        for att in self.social:
            print(att + " " + str(self.social[att]))
        print("")
        for trait in self.traits:
            print(trait + " " + str(self.traits[trait]))
        print("")
        for v in self.virtue:
            if self.virtue[v]:
                print(v)
                break
        for v in self.vice:
            if self.vice[v]:
                print(v)
                break

    def save_char(self):
        path = str(self.name) + ".csv"
        data = []
        data.extend(self.physical.items())
        data.extend(self.mental.items())
        data.extend(self.social.items())
        data.extend(self.traits.items())
        with open(path, "w", newline='') as char_file:
            writer = csv.writer(char_file, delimiter=',')
            writer.writerow(("Name", str(self.name)))
            for stat in data:
                writer.writerow(stat)
            for v in self.virtue:
                if self.virtue[v]:
                    writer.writerow(("Virtue", str(v)))
                    break
            for v in self.vice:
                if self.vice[v]:
                    writer.writerow(("Vice", str(v)))
                    break
        writer.writerow(("Experience", self.experience))

    def load_char(self, name):
        #reads data from save file - name must be in quotes
        data = []
        with open(str(name) + ".csv", 'rt') as char_file:
            reader = csv.reader(char_file, delimiter=',')
            for row in reader:
                data.append(row)
        self.name = data[0][1]
        for i in range(1,4):
            self.physical[data[i][0]] = data[i][1]
        for i in range(4,7):
            self.mental[data[i][0]] = data[i][1]
        for i in range(7,10):
            self.social[data[i][0]] = data[i][1]
        for i in range(10,17):
            self.traits[data[i][0]] = data[i][1]
        self.virtue[data[17][1]] = True
        self.vice[data[18][1]]= True
        self.experience = data[19][1]
        
    def debug(self):
        self.rand_att()
        self.print_char()
        self.save_char()
