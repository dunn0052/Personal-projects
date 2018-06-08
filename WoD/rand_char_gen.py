# random char generator

# @TODO
# increase_stat to serch by type instead of direct dictionary access
import random
import wod_character

class wChar_rand:
    def __init__(self, character):
        self.character = character

    def rand_char(self, name = ""):
        self.character.add_field("char_data/Attributes")
        self.character.add_field("char_data/Final_Touches")
        self.character.add_field("char_data/Merits")
        self.character.add_field("char_data/Skills")
        self.character.add_field("char_data/Virtue_Vice")
        self.character.add_field("char_data/Derangements")
        self.character.add_field("char_data/Traits")
        self.rand_att()
        self.change_name(name)
        self.character.print_char()

    def add_skill_specialization(self, skill, specialization):
          exp = self.character.final_touches["Experience"]
          if(exp >= 3 and (skill in self.character.physical_skills or skill in self.character.social_skills or skill in self.character.mental_skills)):
              exp -= 3
              if (skill not in self.character.skill_specialization):
                  self.character.skill_specialization[skill] = [specialization]
              else:
                  self.character.skill_specialization[skill].append(specialization)
          else:
              print("Could not add " + specialization + " to " + skill)

    def add_weapon(self, name, list = "weapons"):
      # reads data from weapon list - could be made generic for all items
      # should probably use add_field from wod_character
      data = []
      with open(list + ".csv", 'rt') as weapon_file:
          reader = csv.reader(weapon_file, delimiter=',')
          for row in reader:
              if row[0] == name:
                  self.character.weapons[row[0]] = row[1:]
                  print("Added " + row[0] + " to weapons.")
                  break

    def increase_stat(self, stat, dot = 1, free = False, override = False):
        # free = True if increase doesn't cost exp - for GM override
        # could be made less messy by searching through type
        if (stat in self.character.physical or stat in self.character.mental or stat in self.character.social):
            mult = 5
            max_val = stat[3]
        elif(stat in self.character.physical_skills or stat in self.character.mental_skills or stat in self.character.social_skills):
            mult = 3
            max_val = stat[3]
        elif(stat in self.character.physical_merits or stat in self.character.mental_merits or stat in self.character.social_merits or stat == self.character.traits["Morality"]):
            mult = 2
            max_val = 10 if stat == self.character.traits["Morality"] else self.character.find_att(stat)[stat][3]
        else:
            print("Stat not found")
            return
        stat_val = self.character.find_stat(stat)
        cost = stat_val * mult
        if (cost <= self.character.final_touches["Experience"] and stat_val + dot <= max_val or free and stat_val + dot <= max_val or override):
             self.character.find_att(stat)[stat] += dot
             self.character.final_touches["Experience"] -= cost if not free else 0
        else:
             print("Can't increase " + str(stat))


    def change_name(self, name):
        self.character.final_touches["Character Name"] = [name, "Touches", "Final"]

    def find_stat(self, key):
        # duplicate of wod_character
         a = self.character.find_att(key)
         if(a != None):
             return a[(str(key).lower()).title()]
         else:
             return None

    def find_att(self,key):
        # duplicate of wod_character
        clean_key = (str(key).lower()).title()
        for attribute in self.character.search_list:
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


    def rand_point_distribute(self, dots, attributes):
        i = 0
        while (i < dots):
            choice = random.choice(list(attributes))
            if(attributes[choice][0] < attributes[choice][3] - 1):
                attributes[choice][0] += 1
                i+= 1
            elif(attributes[choice][0] == attributes[choice][3] - 1 and i < dots - 1):
                attributes[choice][0] += 1
                i+= 2

    def rand_merit_dist(self, dots):
        for i in range(dots):
            r = random.randint(0,2)
            if(r == 0):
                self.rand_point_distribute(1, self.character.mental_merits)
            elif(r == 1):
                self.rand_point_distribute(1, self.character.physical_merits)
            else:
                self.rand_point_distribute(1, self.character.social_merits)

    def rand_att(self):
        # Could make generic initial stat dots in __init__
        self.rand_dot_dist(self.character.physical, self.character.mental, self.character.social, 5, 4, 3)
        self.rand_dot_dist(self.character.physical_skills, self.character.mental_skills, self.character.social_skills, 11, 7, 4)
        self.rand_merit_dist(7)
        self.rand_der()
        self.character.char_calc()
        self.virtue_gen()
        self.vice_gen()


    def virtue_gen(self):
        self.character.virtue[random.choice(list(self.character.virtue))][0] = True

    def vice_gen(self):
        self.character.vice[random.choice(list(self.character.vice))][0] = True

    def rand_der(self, n = 3):
        chance = random.randint(0,n)
        for i in range(chance):
            pair = self.character.der_map(random.choice(list(self.character.derangements)))
            # if no derangment is present then make mild choice
            if not self.character.derangements[pair[0]][0] and not self.character.derangements[pair[1]][0]:
                self.character.derangements[pair[0]][0] = True
            # if mild derangment is present then upgrade to major
            elif self.character.derangements[pair[0]]:
                self.character.derangements[pair[0]][0] = False
                self.character.derangements[pair[1]][0] = True
            # if already major, then ignore
