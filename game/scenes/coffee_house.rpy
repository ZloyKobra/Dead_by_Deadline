label coffee_house:
    scene bg think_fast_chucklenuts with fade
    play sound "audio/sounds/think-fast-chucklenuts.mp3"
    ""
    scene bg white_space
    play sound "audio/sounds/bzzzzzzzzzzzzzzzzzzzzzz.mp3"
    ""
    "🤣😂🤣😂🤣🤣😂🤣😂🤣🤣😂🤣😂🤣🤣😂🤣😂🤣🤣😂🤣😂🤣🤣😂🤣😂🤣"
    jump start
    return

init:
    transform txt_up:
        yalign 1.5
        linear 300 yalign -50

init python:
    f = open(renpy.loader.transfn("resources/b_movie_script.txt"),"r")
    s = f.readlines()
    my_credits = ''.join(s)
    f.close()

label credits:
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene bg end with fade
    pause 5
    # scene black with dissolve
    # show text my_credits at txt_up
    # pause 15
    return