label seeking_for_team:
    scene bg ggroom_bright with fade
    show gg_sprite

    maincharacter "Нужно найти информацию о том, как сделать игру. Но где?"
    maincharacter "Где можно встретить коллег, у которых можно что-то спросить?"
    menu:
        "Куда мне пойти?"
        "Кофейня в здании офиса": 
            jump coffee_house

        'Коворкинг. Там всегда сидят коллеги, которые чем-то заняты. 
        Быть может, кто-то там сейчас делает игру и сможет помочь мне?':
            jump street
    return start