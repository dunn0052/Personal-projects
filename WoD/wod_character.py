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

        self.dict_map = {
        "Physical Attribute" : self.physical, "Mental Attribute" : self.mental,
        "Social Attribute" : self.social, "Physical Skill" : self.physical_skills,
        "Mental Skill" : self.mental_skills, "Social Skill" : self.social_skills,
        "Trait" : self.traits, "Physical Merit" : self.physical_merits,
        "Mental Merit" : self.mental_merits, "Social Merit" : self.social_merits,
        "Derangement" : self.derangements, "Virtue" : self.virtue, "Vice" : self.vice,
        "Final Touches" : self.final_touches, "Inventory Weapon" : self.weapons,
        "Inventory Item" : self.inventory
        }
        self.change_name(name)

    def add_field(self, file):
        # reads data from a file and adds to dictionary
        data = []
        with open(file + ".csv", 'rt') as data_file:
            reader = csv.reader(data_file, delimiter=',')
            header = next(reader) # header of data file
            type_index = self.parse_header(header, "Type")
            attribute_index = self.parse_header(header, "Attribute")
            name = self.parse_header(header, "Name")
            for row in reader:
                #find the proper dictionary and fill entry with clean data
                if row != header and type_index != None and attribute_index != None and attribute_index != "":
                    self.find_dict(self.clean_item(row[type_index]), self.clean_item(row[attribute_index]))[self.clean_item(row[name])] = self.clean_row(row[1:])
                elif row != header and type_index != None:
                    self.find_dict(self.clean_item(row[type_index]))[self.clean_item(row[name])] = self.clean_row(row[1:])
                else:
                    continue


    def parse_header(self, header, key):
        # find index of header
        clean_key = self.clean_key(key)
        if key in header:
            return header.index(key)
        else:
            return None

    def clean_key(self, key):
        return (str(key).lower()).title()

    def clean_row(self, row):
        # turns .csv row back into proper python types
        n = []
        for item in row:
            n.append(self.clean_item(item))
        return n

    def clean_item(self, item):
        # Could be misevaluated if string really meant to be "TRUE" or "FALSE"
        if item.capitalize() == "TRUE":
            return True
        elif item.capitalize() == "FALSE":
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
        # Returns proper dictionary based on index
        if(attribute != None):
            return self.dict_map[self.clean_key(attribute) + " " + self.clean_key(type)]
        else:
            return self.dict_map[self.clean_key(type)]


    def increase_exp(self, num = 1):
        self.final_touches["Experience"] += num


    def change_name(self, name):
        self.final_touches["Name"] = [str(name)]

    def find_stat(self, key):
         a = self.find_att(key)
         if(a != None):
             return a[self.clean_key(key)]
         else:
             return None

    def find_att(self,key):
        clean_key = self.clean_key(key)
        for attribute in self.dict_map.values():
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

    def save_char(self, path):
        if ("Name" not in self.final_touches or self.final_touches["Name"] == None or self.final_touches["Name"] == ""):
            print("The Characer needs a name to save. Use change_name().")
            return
        data = [["Name", "Current", "Type", "Attribute"]]
        for item in self.dict_map.values():
            if any(item):
                for key in item:
                    # can't do data.append([key].extend(item[key])) ??
                    row = [key]
                    row.extend(item[key])
                    data.append(row)
        with open(path + ".csv", "w", newline='') as char_file:
            writer = csv.writer(char_file, delimiter=',')
            for stat in data:
                writer.writerow(stat)

    def print_attributes(self, attributes, index = 0, present = False):
        # present to print attributes even if they have a value of 0
        if present:
            for attribute in attributes:
                print(attribute + " " + str(attributes[attribute][index]))
        else:
            for attribute in attributes:
                if (attributes[attribute] != 0):
                   print(attribute + " " + str(attributes[attribute][index]))

    def print_char(self):
        # @TODO finish printing sheet
        self.print_attributes(self.final_touches, 0, True)
        print("")
        print("Attributes")
        print("---------------------------------------------------------------")
        self.print_attributes(self.physical, 0, True)
        self.print_attributes(self.mental, 0, True)
        self.print_attributes(self.social, 0, True)
        print("")
        print("Traits")
        print("---------------------------------------------------------------")
        self.print_attributes(self.traits, 0, True)
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
