label street:
    scene bg street with fade
    show gg calm1

    with moveinright

    "Среди всех прохожих ты замечаешь коллегу, который присутствовал на твоём собеседовании на работу."
    "Он всем своим видом кричит, что он - программист и любитель видеоигр:"
    'толстовка с надписью "Atomic Heart", браслеты с названиями старых пиксельных видеоигр, рюкзак со множеством тематических наклеек, очки, джинсы и... очень растряпанная причёска.'
    menu:
        "Поговорить с ним":
            stop music fadeout 1.0
            jump talking_on_the_street
        "Пройти мимо":
            stop music fadeout 1.0
            jump skip_human
    return

label skip_human:
    stop music
    play sound "audio/sounds/spongebob_sad_sound.mp3"
    "Ты проходишь мимо. Вряд ли он дал бы тебе какую-то нужную информацию, он всё-таки куда-то торопился."
    "Не каждого же встречного опрашивать."
    stop sound
    play music seva_theme fadeout 1.0
    jump Now_its_definitely_coworking
    return


label talking_on_the_street:
    play music seva_theme fadeout 1.0
    show gg calm1 with moveinleft:
        xalign 0.8
        yalign 1.05
    show seva calm1 with moveinleft:
        xalign 0.2
        yalign 1.05
    menu:
        'Что ты собираешься ему сказать?'
        "Классный прикид!":
            show gg speak_:
                xalign 0.8
                yalign 1.05
            maincharacter "Классный прикид!"
            show seva thumbsup_:
                xalign 0.2
                yalign 1.05
            seva "Спасибо!"
            "Отблагодарив за комплимент, он просто пошёл дальше по своим делам."
            menu:
                "Привлечь его внимание, попытаться остановить.":
                    show gg calm2:
                        xalign 0.8
                        yalign 1.05
                    maincharacter "Эй! Помнишь меня? Я был на собеседовании.\nМне дали задание, игра, которую я... давно должен был начать делать."

                    show seva calm2:
                        xalign 0.2
                        yalign 1.05
                    seva "Что-то плохо помню, давно это было, да и задание такое мы дали довольно многим."
                    seva "А что? Ты что-то хотел?"
                    show gg speak_:
                        xalign 0.8
                        yalign 1.05
                    maincharacter "Да, мне нужна помощь. Можешь на пару вопросов ответить как опытный разработчик?"
                    show seva calm1:
                        xalign 0.2
                        yalign 1.05
                    seva "Я немного спешу, поэтому могу ответить только на один. Меня, кстати Сева звать."

                    maincharacter "Подскажи, какой язык лучше всего использовать для быстрой разработки игры?"
                    show seva thumbsup_:
                        xalign 0.2
                        yalign 1.05
                    seva "C#. Это база. Это знать надо. Я всю жизнь только на нём и пишу, он обычно и используется в игровом движке Unity."
                    seva "Во-первых, язык довольно производительный, во-вторых, огромное коммьюнити и куча библиотек и фреймворков."
                    seva "В-третьих, язык не слишком сложный для изучения и имеется колоссальное количество материалов, гайдов, видео для изучения. Ну что, подходящий ответ?"
                    show gg think_:
                        xalign 0.8
                        yalign 1.05
                    maincharacter "Ого. Да, это действительно хороший ответ. Я как раз этот язык и изучал. Не уверен был, точно ли мне стоит его использовать, спасибо что прояснил."

                    seva "Не за что, ну давай, мне пора, удачи в реализации игры!"

                    "Сева уходит, а ты направляешься в коворкинг"

                    jump Now_its_definitely_coworking

                "Пусть уходит. Не буду мешать.":
                    jump skip_human
                    return

        "Привет! Не против, если задам пару вопросов?":
            show gg speak_:
                xalign 0.8
                yalign 1.05
            maincharacter "Привет! Не против, если задам пару вопросов?"
            maincharacter "Привет, я [gg_name], был когда-то у вас на собеседовании, можно задам несколько вопросов по поводу игры, которую надо сделать"
            show seva calm2:
                xalign 0.2
                yalign 1.05
            seva "Ну привет. Думаю, у меня есть время только на один вопрос, немного спешу. Задавай"

            maincharacter "Подскажи, как разработчик,  какой язык лучше всего использовать для быстрой разработки игры?"
            show seva thumbsup_:
                xalign 0.2
                yalign 1.05
            seva "C#. Это база. Это знать надо. Я всю жизнь только на нём и пишу, он обычно и используется в игровом движке Unity."
            seva "Во-первых, язык довольно производительный, во-вторых, огромное коммьюнити и куча библиотек и фреймворков."
            seva "В-третьих, язык не слишком сложный для изучения и имеется колоссальное количество материалов, гайдов, видео для изучения. Ну что, подходящий ответ?"
            show gg think_:
                xalign 0.8
                yalign 1.05
            maincharacter "Ого. Да, это действительно хороший ответ. Я как раз этот язык и изучал. Не уверен был, точно ли мне стоит его использовать, спасибо что прояснил."

            seva "Не за что, ну давай, мне пора, удачи в реализации игры!"       

            jump Now_its_definitely_coworking
        "П-п-привет...":
            show seva calm2:
                xalign 0.2
                yalign 1.05
            seva "Э-э-э... Ты это мне?"

            "От твоей неуверенности и его вопроса тебе стало так неловко, что ты покраснел и засмущался"
            "Ты находишь набираешь уверенность и продолжаешь диалог"
            show gg calm2:
                xalign 0.8
                yalign 1.05
            maincharacter "Да, я [gg_name], был у вас на собеседовании когда-то, а тебя как зовут?"

            seva "Я Сева, ты что-то хотел?"

            maincharacter "Понимаю, ты торопишься, занят и всё такое, но..."

            seva "Ближе к делу."

            maincharacter "Так, да. Можешь посоветовать, какой язык лучше всего использовать для быстрой разработки игры?"
            show seva thumbsup_:
                xalign 0.2
                yalign 1.05
            seva "C#. Это база. Это знать надо. Я всю жизнь только на нём и пишу, он обычно и используется в игровом движке Unity."
            seva "Во-первых, язык довольно производительный, во-вторых, огромное коммьюнити и куча библиотек и фреймворков."
            seva "В-третьих, язык не слишком сложный для изучения и имеется колоссальное количество материалов, гайдов, видео для изучения. Ну что, подходящий ответ?"
            show gg think_:
                xalign 0.8
                yalign 1.05
            maincharacter "Ого. Да, это действительно хороший ответ. Я как раз этот язык и изучал. Не уверен был, точно ли мне стоит его использовать, спасибо что прояснил."

            seva "Не за что, ну давай, мне пора, удачи в реализации игры!"

            "Сева уходит, а ты направляешься в коворкинг"
            stop music fadeout 1.0
            jump Now_its_definitely_coworking
    return