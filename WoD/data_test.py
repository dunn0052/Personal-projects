from wod_character import wChar

a = wChar("test_data")
a.add_field("char_data/Attributes")
a.add_field("char_data/Final_Touches")
a.add_field("char_data/Merits")
a.add_field("char_data/Skills")
a.add_field("char_data/Virtue_Vice")
a.add_field("char_data/Derangements")
a.save_char("test_data")
x = wChar("test2")
x.add_field("test_data")
x.print_char()
