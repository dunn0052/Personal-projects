from char_gen_obj import wChar

m = wChar("default")
path = ("default.csv")
data = []
data.extend(m.final_touches.items())
data.extend(m.physical.items())
data.extend(m.mental.items())
data.extend(m.social.items())
data.extend(m.traits.items())
data.extend(m.physical_skills.items())
data.extend(m.mental_skills.items())
data.extend(m.social_skills.items())
data.extend(m.physical_merits.items())
data.extend(m.mental_merits.items())
data.extend(m.social_merits.items())
data.extend(m.virtue.items())
data.extend(m.vice.items())
data.extend(m.derangements.items())

with open(path, "w", newline='') as char_file:
    writer = csv.writer(char_file, delimiter=',')
    for stat in data:
        writer.writerow(stat)
