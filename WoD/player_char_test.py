from wod_character import wChar
from player_char import playerCharacter

a = wChar("test")

x = playerCharacter(a)

for dict in x.character.dict_map.values():
    for item in dict:
        x.increase_stat(item, free = True)
x.character.print_char()
