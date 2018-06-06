# data char generator
import csv
import random

class wChar:
    def __init__(self, name = None):

        # All attributes must begin every word with capital for search to work
        self.physical = {}
        self.mental = {}
        self.social = {}
        self.virtue = {}
        self.vice = {}
        self.traits = {}
        self.mental_skills = {}
        self.physical_skills = {}
        self.social_skills = {}
        self.derangements = {}
        self.mental_merits = {}
        self.physical_merits = {}

        self.social_merits = {}
        self.final_touches = {}
        self.skill_specialization = {}

        self.weapons = {}

        self.inventory = {}

        self.search_list = [self.physical, self.mental, self.social,
        self.physical_skills,self.mental_skills, self.social_skills, self.traits,
        self.physical_merits, self.mental_merits, self.social_merits,
        self.derangements, self.virtue, self.vice, self.final_touches]

        self.dict_map = {
        "PhysicalAttribute" : self.physical, "MentalAttribute" : self.mental, "SocialAttribute" : self.social, "PhysicalSkill" : self.physical_skills,
        "MentalSkill" : self.mental_skills, "SocialSkill" : self.social_skills, "Trait" : self.traits,
        "PhysicalMerit" : self.physical_merits, "MentalMerit" : self.mental_merits, "SocialMerit" : self.social_merits,
        "Derangement" : self.derangements, "Virtue" : self.virtue, "Vice" : self.vice, "FinalTouch" : self.final_touches

        }
        self.change_name(name)

    def add_field(self, file, dictionary):
        # reads data from a file and adds to dictionary
        data = []
        with open(file + ".csv", 'rt') as data_file:
            reader = csv.reader(data_file, delimiter=',')
            header = next(reader) # header of data file
            for row in reader:



    def clean_row(self, row):
        n = []
        for item in row:
            n.append(self.clean_item(item))
        return n

    def clean_item(self, item):
        if item == "True":
            return True
        elif item == "False":
            return False
        elif isinstance(item, bool):
            return item
        elif isinstance(item, int):
            return item
        elif item.isnumeric():
            return int(item)
        elif item == "None":
            return None
        else:
            return item

    def find_dict(self, type, attribute = None):
        if(attribute != None):
            return self.dict_map[type]
        else:
            return self.dict_map[type + attribute]


    def increase_exp(self, num = 1):
        self.final_touches["Experience"] += num


    def change_name(self, name):
        self.final_touches["Name"] = str(name)

    def find_stat(self, key):
         a = self.find_att(key)
         if(a != None):
             return a[(str(key).lower()).title()]
         else:
             return None

    def find_att(self,key):
        clean_key = (str(key).lower()).title()
        for attribute in self.search_list:
            if clean_key in attribute:
                return attribute
        print(str(key) + " not found.")
        return None

    def char_calc(self):
        self.traits["Size"] = 5
        self.traits["Health"] = self.traits["Size"] + self.physical["Stamina"]
        self.traits["Willpower"] = self.mental["Resolve"] + self.social["Composure"]
        self.traits["Defense"] = min(self.physical["Dexterity"], self.mental["Wits"])
        self.traits["Initiative"] = self.physical["Dexterity"] + self.social["Composure"]
        self.traits["Speed"] = self.physical["Strength"] + self.physical["Dexterity"] + 5
        self.traits["Morality"] = 7

    def write_attribute(self, dict, writer):
        return

    def save_char(self):
        if (self.final_touches["Name"]== None):
            print("The Characer needs a name to save. Use change_name().")
            return
        path = str(self.final_touches["Name"]) + ".csv"
        with open(path, "w", newline='') as char_file:
            writer = csv.writer(char_file, delimiter=',')
            for stat in data:
                writer.writerow(stat)

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
        print("Derangements")
        print("---------------------------------------------------------------")
        self.print_attributes(self.derangements)
        print("")
        print("Virtue and Vice")
        print("---------------------------------------------------------------")
        self.print_attributes(self.virtue)
        self.print_attributes(self.vice)
