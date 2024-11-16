# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define maincharacter = Character("[gg_name]", color="#44e010", callback=name_callback, cb_name="gg_sprite")
define seva = Character("Сева", color="#37362d", callback=name_callback, cb_name="seva_sprite")

image gg_calm1 = At("", sprite_highlight("gg_sprite"))
image seva_sprite_ = At("seva_sprite", sprite_highlight("seva_sprite"))
# image gg_test_ = At("gg_test", sprite_highlight("gg_test"))
# image friend_gandon_ = At("friend_gandon", sprite_highlight("friend_gandon"))




