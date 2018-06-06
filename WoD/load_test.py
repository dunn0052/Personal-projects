from char_gen_obj import wChar

a = wChar("test")
a.debug()
x = wChar("test2")
x.load_char("test")
x.print_char()
x.increase_stat("Strength")
x.add_skill_specialization("Strength", "pull teeth")
x.add_skill_specialization("Expression", "pull teeth")
x.increase_exp(6)
x.add_skill_specialization("Expression", "pull teeth")
x.add_skill_specialization("Expression", "pull teat")
print(x.skill_specialization)
