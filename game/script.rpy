label start:

    $ gg_name = renpy.input("Как зовут вашего персонажа?\n")
    scene bg ggroom_bright with fade
    show gg_sprite

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

    scene bg ggroom_bright with fade
    show gg_sprite
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
            jump pass_scene
    return

