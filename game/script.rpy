label start:

    $ gg_name = renpy.input("Как зовут вашего персонажа?\n")
    scene bg ggroom with fade
    show gg_sprite_

    play music "audio/sounds/ringtone_nokia_heheheha.mp3"
    voice "dictor/line1_8am.ogg"
    "8 утра ☠️"

    voice "main_character/start_lines_whos_calling.ogg"
    maincharacter "Кто-то звонит?\nКому я вообще сдался в такую рань?"

    scene bg phone_call
    with fade
    ""
    play music "audio/music/doors_parameters.mp3"
    
    "Генеральный директор" "Напоминаем вам, что для успешного принятия на работу вы должны были сделать видеоигру, иначе мы будем вынуждены отказать вам в трудоустройстве"
    "Генеральный директор" "До дедлайна осталось 7 дней"
    "Генеральный директор" "Хотелось поинтересоваться, как ваш прогресс?"
    "Генеральный директор" "С уважением,  директор компании."

    stop music

    voice "main_character/start_lines_a_WEEK.ogg"
    maincharacter "НЕДЕЛЯ?!"

    play music "audio/music/Ben Salisbury, Geoff Barrow - The Alien.mp3"
    scene bg ggroom_bright
    with Dissolve(10.0)

    ""
    voice "main_character/start_lines_i_forgor.ogg"
    maincharacter "ЧЁРТ! КАК Я МОГ ОБ ЭТОМ ЗАБЫТЬ? РАБОТА МОЕЙ МЕЧТЫ, А Я ПРО НЕЁ ПРОСТО ЗАБЫЛ!!"

    scene bg ggroom with fade
    show gg_sprite_
    voice "main_character/start_lines_clueles.ogg"
    maincharacter "Не стоило откладывать это дело на потом." 

    voice "main_character/start_lines_shurly_the_game_is_ready.ogg"
    maincharacter "Нужно написать, что всё в порядке, и игра почти готова."


    "Ты отправляешь ответное письмо работодателю, в котором пишешь, что всё под контролем, и нужно сделать финальные штрихи перед отправкой"
    maincharacter "Так, [gg_name], сосредоточься, нужно придумать что-то."

    stop music fadeout 1.0

    menu what_to_do:
        "Что же мне делать?"
        "Попросить помощи у коллег":
            jump seeking_for_team
        "Попытаться найти нужную информацию самим, без посторонней помощи":
            jump solo_game
    return

label solo_game:
    scene bg think_fast_chucklenuts with fade
    voice "audio/sounds/think-fast-chucklenuts.mp3"
    ""
    scene bg white_space
    voice "audio/sounds/bzzzzzzzzzzzzzzzzzzzzzz.mp3"
    ""
    jump start
    return

label seeking_for_team:
    scene bg ggroom with fade
    show gg_sprite_

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

label coffee_house:
    scene bg think_fast_chucklenuts with fade
    voice "audio/sounds/think-fast-chucklenuts.mp3"
    ""
    scene bg white_space
    voice "audio/sounds/bzzzzzzzzzzzzzzzzzzzzzz.mp3"
    ""
    jump seeking_for_team
    return

label street:
    scene bg ggroom with fade
    show gg_sprite_

    maincharacter "Коворкинг. Место, куда люди приходят, чтобы вместе или в одиночку поработать над чем-то."
    "Ты выходишь из дома и направляешься в офисный коворкинг компании, в которую трудоустраиваешься."

    scene bg street_test with fade
    show gg_sprite_
    with moveinright

    "Среди всех прохожих ты замечаешь коллегу, который присутствовал на твоём собеседовании на работу."
    "Он всем своим видом кричит, что он - программист и любитель видеоигр:"
    'толстовка с надписью "Atomic Heart", браслеты с названиями старых пиксельных видеоигр, рюкзак со множеством тематических наклеек, очки, джинсы и... неопрятная причёска.'
    menu:
        "Поговорить с ним":
            # jump talking_on_the_street
            return
        "Пройти мимо":
            # jump
            return 
    return

label talking_on_the_street:
    scene bg street_test with fade
    show gg_sprite_ at right
    with moveinright
    show seva_sprite_ at left
    with moveinleft
    menu:
        'Что ты собираешься ему сказать?'
        "Классный прикид!":
            return
        "Привет! Не против, если задам пару вопросов?":
            return
        "П-п-привет...":
            return

label umgunpuk:
    "Ты проходишь мимо. Вряд ли он дал бы тебе какую-то нужную информацию, он всё-таки куда-то торопился. Не каждого же встречного опрашивать."
    return