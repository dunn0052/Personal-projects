# Player Character creation

import wod_character

class playerCharacter:
    def __init__(self, character):
        self.character = character

    def increase_stat(self, stat, dot = 1, free = False, override = False):
        # free = True if increase doesn't cost exp - for GM override
        # could be made less messy by searching through type
        # change header attribut to something better
        stat_dict = self.character.find_att(stat)
        stat_data = self.character.find_stat(stat)
        if stat_dict == None:
            print(stat + " does not exist. Check .csv data")
            return
        if "Attribute" in stat_data:
            mult = 5
            max_val = stat_data[3]
        elif "Skill" in stat_data:
            mult = 3
            max_val = stat_data[3]
        elif "Merit" in stat_data or stat == "Morality":
            mult = 2
            max_val = 10 if stat == "Morality" else stat_data[3]
        elif "Inventory" in stat_data:
            stat_dict[stat][0] += 1
            return
        elif isinstance(stat_data[0], bool):
            stat_data[0] = True
            return
        else:
            print(stat + " not found")
            return
        cost = stat_data[0] * mult
        if (cost <= self.character.final_touches["Experience"][0] and stat_data[0] + dot <= max_val or free and stat_data[0] + dot <= max_val or override):
             stat_dict[stat][0] += dot
             self.character.final_touches["Experience"][0] -= cost if not free else 0
        else:
             print("Can't increase " + stat)
        self.character.char_calc()

    def add_skill_specialization(self, skill, specialization):
          exp = self.character.final_touches["Experience"]
          skill_entry = self.character.find_stat(skill)
          # If actually a skill and have enough exp
          if(exp >= 3 and dictionary != None and "Skill" in skill_entry):
              exp -= 3
              if (skill not in self.character.skill_specialization):
                  self.character.skill_specialization[skill] = [specialization]
              else:
                  self.character.skill_specialization[skill].append(specialization)
          else:
              print("Could not add " + specialization + " to " + skill)
