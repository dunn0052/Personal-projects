#char generator

##@TODO
##
##- Add save/load features for skills/merits and such
##- Make an increase function based on experience
##- Make an increase function for character generation
##- Make GUI
##- Dot totals for merits
##- Add place for skill specialization
##- Add/change name
##- Other personal stats - Age/Player/Faction/Description
##- Increase experience
##- Add Equipment
##- Attack dice and modifiers
##- Skill modifier and roll
##- Merit modifiers

import csv
import random


class wChar:
    def __init__(self, name = None):

        self.name = name

        self.experience = 0

        self.physical = {
            "Strength" : 1,
            "Dexterity" : 1,
            "Stamina" : 1
            }
        self.mental = {
            "Intelligence" : 1,
            "Wits" : 1,
            "Resolve" : 1
            }
        self.social = {
            "Presence" : 1,
            "Manipulation" : 1,
            "Composure" : 1
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

        self.mental_skills = {
            "Academics" : 0,
            "Computer" : 0,
            "Crafts" : 0,
            "Investigation" : 0,
            "Medicine" : 0,
            "Occult" : 0,
            "Politics" : 0,
            "Science" : 0
        }

        self.physical_skills = {
            "Athletics" : 0,
            "Brawl" : 0,
            "Drive" : 0,
            "Firearms" : 0,
            "Larceny" : 0,
            "Stealth" : 0,
            "Survival" : 0,
            "Weaponry" : 0
        }

        self.social_skills = {
            "Animal Ken" : 0,
            "Empathy" : 0,
            "Expression" : 0,
            "Intimidation" : 0,
            "Persuasion" : 0,
            "Socialize" : 0,
            "Streetwise" : 0,
            "Subterfuge" : 0
        }

        self.derangements = {
            "Depression" :  False,
            "Melancholia" :  False,
            "Phobia"  :  False,
            "Hysteria" :  False,
            "Narcissism" :  False,
            "Megalomania" :  False,
            "Fixation" :  False,
            "Obsessive Compulsion" :  False,
            "Suspicion" :  False,
            "Paranoia" :  False,
            "Inferiority Complex" :  False,
            "Anxiety" :  False,
            "Vocalization" :  False,
            "Schizophrenia" :  False,
            "Irrationality" :  False,
            "Multiple Personality" :  False,
            "Avoidance" :  False,
            "Fugue" :  False
        }

        self.mental_merits = {
            "Common Sense" : 0,
            "Danger Sense" : 0,
            "Eidetic Memory" : 0,
            "Encyclopedic Knowledge" : 0,
            "Holistic Awareness" : 0,
            "Language" : 0,
            "Meditative Mind" : 0,
            "Unseen Sense" : 0,
        }

        self.physical_merits = {
            "Ambidextrous" : 0,
            "Brawling Dodge" : 0,
            "Direction Sense" : 0,
            "Disarm" : 0,
            "Fast Reflexes" : 0,
            "Fighting Finesse" : 0,
            "Fighting Style: Boxing" : 0,
            "Fighting Style: Kung Fu" : 0,
            "Fighting Style: Two Weapons" : 0,
            "Fleet Of Foot" : 0,
            "Fresh Start" : 0,
            "Giant" : 0,
            "Gunslinger" : 0,
            "Iron Stamina" : 0,
            "Iron Stomach" : 0,
            "Natural Immunity" : 0,
            "Quick Draw" : 0,
            "Quick Healer" : 0,
            "Strong Back" : 0,
            "Strong Lungs" : 0,
            "Stunt Driver" : 0,
            "Toxin Resistance" : 0,
            "Weaponry Dodge" : 0,
        }

        self.social_merits = {
            "Allies" : 0,
            "Barfly" : 0,
            "Contacts" : 0,
            "Fame" : 0,
            "Inspiring" : 0,
            "Mentor" : 0,
            "Resources" : 0,
            "Retainer" : 0,
            "Status" : 0,
            "Stunning Looks" : 0,
        }

        self.final_touches = {
            "Name" : "",
            "Experience" : 0,
            "Age" : -1,
            "Player" : "",
            "Faction" : "",
            "Group Name" : "",
            "Concept" : "",
            "Group Name" : ""
        }

    def find_stat(self, key):
         a = self.find_att(key)
         if(a != None):
             return a[(str(key).lower()).title()]
         else:
             return None

    def find_att(self,key):
        clean_key = (str(key).lower()).title()
        n = [self.physical, self.mental, self.social, self.physical_skills,
        self.mental_skills, self.social_skills, self.traits,
        self.physical_merits, self.mental_merits, self.social_merits,
        self.derangements, self.virtue, self.vice, self.final_touches]
        for attribute in n:
            if clean_key in attribute:
                return attribute
        print(str(key) + " not found.")
        return None

    def rand_dot_dist(self, phys, ment, socl, first = 0, second = 0, third = 0):
        n = [first,second,third]
        random.shuffle(n)
        self.rand_point_distribute(n[0], phys)
        self.rand_point_distribute(n[1], ment)
        self.rand_point_distribute(n[2], socl)


    def rand_point_distribute(self, dots, attributes, max_val = 5):
        i = 0
        while (i < dots):
            choice = random.choice(list(attributes))
            if(attributes[choice] < max_val):
                attributes[choice] += 1
                i+= 1
            elif(attributes[choice] == max_val - 1 and i == dots - 2):
                if(random.randint(0,1)):
                    attributes[choice] +=1
                    i += 2
            elif(attributes[choice] == max_val - 1 and i != dots - 1):
                #bug if every value is max besides this one it will inf loop -- too bad cheaters
                attributes[choice] += 1
                i += 2


    def rand_merit_dist(self, dots):
        for i in range(dots):
            r = random.randint(0,2)
            if(r == 0):
                self.rand_point_distribute(1, self.mental_merits)
            elif(r == 1):
                self.rand_point_distribute(1, self.physical_merits)
            else:
                self.rand_point_distribute(1, self.social_merits)

    def rand_att(self):

        self.rand_dot_dist(self.physical, self.mental, self.social, 5, 4, 3)
        self.rand_dot_dist(self.physical_skills, self.mental_skills, self.social_skills, 11, 7, 4)
        self.rand_merit_dist(7)

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

    def print_attributes(self, attributes, present = False):
        # present to print attributes even if they have a value of 0
        if present:
            for attribute in attributes:
                print(attribute + " " + str(attributes[attribute]))
        else:
            for attribute in attributes:
                if attributes[attribute] or int(attributes[attribute]) > 0:
                   print(attribute + " " + str(attributes[attribute]))

    def print_char(self):
        # @TODO finish printing sheet
        self.print_attributes(self.final_touches, True)
        print("")
        print("Attributes")
        print("---------------------------------------------------------------")
        self.print_attributes(self.physical, True)
        self.print_attributes(self.mental, True)
        self.print_attributes(self.social, True)
        print("")
        print("Traits")
        print("---------------------------------------------------------------")
        self.print_attributes(self.traits, True)
        print("")
        print("Skills")
        print("---------------------------------------------------------------")
        self.print_attributes(self.physical_skills)
        self.print_attributes(self.mental_skills)
        self.print_attributes(self.social_skills)
        print("")
        print("Merits")
        print("---------------------------------------------------------------")
        self.print_attributes(self.physical_merits)
        self.print_attributes(self.mental_merits)
        self.print_attributes(self.social_merits)
        print("")
        print("Derangements, virtue, vice")
        print("---------------------------------------------------------------")
        self.print_attributes(self.derangements)
        self.print_attributes(self.virtue)
        self.print_attributes(self.vice)

    def save_char(self):
        if (self.name == None):
            print("The Characer needs a name to save.")
            return
        path = str(self.name) + ".csv"
        data = []
        data.extend(self.physical.items())
        data.extend(self.mental.items())
        data.extend(self.social.items())
        data.extend(self.traits.items())
        data.extend(self.physical_skills.items())
        data.extend(self.mental_skills.items())
        data.extend(self.social_skills.items())
        data.extend(self.physical_merits.items())
        data.extend(self.mental_merits.items())
        data.extend(self.social_merits.items())
        data.extend(self.derangements.items())
        with open(path, "w", newline='') as char_file:
            writer = csv.writer(char_file, delimiter=',')
            for stat in data:
                writer.writerow(stat)
            for v in self.virtue:
                if self.virtue[v]:
                    writer.writerow((str(v), True))
                    break
            for v in self.vice:
                if self.vice[v]:
                    writer.writerow((str(v), True))
                    break


    def load_char(self, name):
        #reads data from save file - name must be in quotes
        data = []
        with open(str(name) + ".csv", 'rt') as char_file:
            reader = csv.reader(char_file, delimiter=',')
            for row in reader:
                data.append(row)
##        self.name = data[0][1]
##        for i in range(1,4):
##            self.physical[data[i][0]] = data[i][1]
##        for i in range(4,7):
##            self.mental[data[i][0]] = data[i][1]
##        for i in range(7,10):
##            self.social[data[i][0]] = data[i][1]
##        for i in range(10,17):
##            self.traits[data[i][0]] = data[i][1]
##        self.virtue[data[17][1]] = True
##        self.vice[data[18][1]]= True
##        self.experience = data[19][1]
        for item in data:
            print(item)
            self.find_att(item[0])[item[0]] = item[1]


    def debug(self):
        self.rand_att()
        self.print_char()
        self.save_char()
