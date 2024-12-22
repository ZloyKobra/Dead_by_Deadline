label salat_scene_1:
    "Рисование очень увлекает, ты даже не заметил как прошёл целый день, и всё ещё полон сил"
    "Ты нарисовал кучу спрайтов для локаций, персонажей, окружения и способностей, которые навряд ли даже будут в игре."
    "Все рисунки выполнены в жанре постапокалипсиса, где всё грязное, заброшенное, в тёмных тонах."
    "И вот, после всей этой проделанной работы, ты решаешь немного отдохнуть, но тут..."
    jump big_scene_2

label salat_scene_2:
    maincharacter "Но ведь... У меня вообще ничего не готово кроме чёртовых рисунков!!"
    "Ты начинаешь работу в усиленном темпе. Выбираешь первый попавшийся в интернете игровой движок - Unity."
    "Ты начинаешь реализовывать двойной прыжок, подключать свои спрайты через инструмент в движке {bt=6}{color=#1cd3a2}Tilemap{/color}{/bt}, а также просто воровать"
    "нет"
    "ВДОХНОВЛЯТЬСЯ* уровнями с препятствиями из других популярных платформеров, попутно переделывая их, немного упрощая."
    "Эту ночь ты практически не спишь... До четырёх часов ночи ты программируешь и попутно исправляешь придуманные в спешке уровни, и у тебя..."
    "...Более-менее получилось! Слабоватые механики, однообразие, один иногда неработающий уровень, баги, но оно работает!"
    "Ты засыпаешь прямо на столе перед ноутбуком."
    jump end_day_3

label salat_scene_3:
    maincharacter "Я работаю над платформером, но некоторые вещи всё еще не успел реализовать."
    maincharacter "Если честно, мне бы очень пригодилась помощь с финальными доработками — багами и оптимизацией."
    
    "Ты даёшь ему сыграть в твой прототип игры."

    pavel "Хм, ну, выглядит неплохо, правда геймплей... мягко говоря хромает."
    pavel "Давай по-быстрому добавим механику рывка и прыжка по стенам - классические фичи в платформерах, много раз такое делал."

    "н молниеносно вводит механики в код, исправляет код прыжка, а ты даже не успеваешь уследить за его действиями"
    jump big_scene_4



label salat_scene_END_IS_NEAR:
    show boss hands_:
        xalign 0.3
        yalign 1.05

    boss "Итак, [gg_name]. Я ждал вас."
    boss "Не будем тянуть. Начнём."

    "Твоя ладонь крепче сжимает флешку, и ты быстро подходишь к компьютеру, подключаешь её к порту." 
    "Ты включаешь игру, и на экране появляется главное меню — результат дней и ночей работы, испытание для твоих навыков и терпения."
    "Открывается первый уровень, и ты слышишь..."

    boss "Прошу, сначала расскажите про вашу игру. Что она из себя представляет?"

    maincharacter "Пиксельный платформер. Весь дизайн, как вы видите, выполнен в жанре постапокалипсиса в тёмных тонах.  Всё это я нарисовал сам."
    maincharacter "В игре имеются такие механики, как двойной прыжок, прыжки от стен и рывок вперёд. Также присутствуют враги с простейшим ИИ. Есть несколько уровней с секретными комнатами."

    boss "Что делает твою игру особенной?"

    maincharacter "Ну... Уникальный стиль, наверное..."

    boss "Хм. Действительно. Мне очень даже нравится дизайн игры в целом."
    boss "Хорошо, продолжим. Покажи, как ты проходишь этот уровень."

    "Ты демонстрируешь управление, двойной прыжок, рывок вперёд, трёх врагов, секретную комнату в уровне. Когда ты прыгал от стен, твой персонаж вылетел за пределы уровня, поэтому тебе пришлось начать уровень заново."

    boss "Что этот уровень из себя представляет? Что он показывает игроку?"

    maincharacter "Он показывает все механики в игре, демонстрирует, как вообще работает игра."

    boss "Все возможности механик предоставлены в самом же первом уровне? Ах да, у тебя механик-то не так уж и много."
    boss "Хотя, рывок вперёд можно было дать в одном из следующих уровней, чтобы новые уровни открывали для игрока новые возможности, чтобы он не терял интерес."

    "Босс записывает что-то в блокнот."

    boss "С этим разобрались, а теперь..."
    boss "Позволь мне пройти следующие уровни."

    maincharacter "Да, конечно... прошу."

    "Ты передаешь клавиатуру и мышь Боссу"
    "Он не спеша проходит второй уровень, прыгая в различные стороны и задевая все стены. Вдруг персонаж опять игры вылетает за пределы уровня."
    "Перезапуск. Босс не реагирует, перепроходит уровень. В третьем уровне он пытается умереть от лёгких врагов, но безуспешно."
    "Кажется, главный герой не получает от них урона. Снова никакой реакции. Босс находит секретную комнату и проходит уровень."
    "Никакой реакции." 
    "Игра пройдена."

    boss "Ещё и двойной прыжок как-то криво работает..."
    boss "Мгм."
    "Oн снова записывает что-то в блокнот"
    boss "Баги. Расскажи, как ты с ними справлялся?"

    maincharacter "Когда я сделал первую версию игры, у меня было довольно много багов, таких как неработающие платформы, сломанная физика."
    maincharacter "Критические баги мне помог пофиксить ваш сотрудник, Павел. Некоторую часть я исправил после встречи с ним, после того, как я научился правильно находить и фиксить баги."
    maincharacter "Часть багов также отпала, когда я делал рефакторинг кода. На исправление оставшихся багов просто не хватило времени..."

    boss "Оу, так ты уже и с сотрудниками познакомился? И даже поработать с ними успел? Это, несомненно, большой плюс."

    maincharacter "Да, ваши сотрудники довольно отзывчивы, не только Павел. Они мне помогли в разработке игры."

    boss "Да, именно таких мы и берём в нашу команду."
    boss "А теперь скажи-ка мне честно, мы дали тебе на разработку игры полгода, сколько из этого времени вы потратили на свою игру, что тебе не хватило времени, чтобы исправить баги?"
    menu:
        "4 Дня. (сказать правду)":
            jump salat_end
        "Ну... где-то месяц (солгать)":
            jump weird_salat_end

label salat_end:
    maincharacter "Я начал разработку 4 дня назад, когда пришло ваше письмо... "
    maincharacter "Я так увлёкся видеоиграми и развлечениями, что забыл о дедлайне..."

    boss "Это всё объясняет... Однако. Ты за 4 дня успел сделать дизайн игры так, чтобы при этом получилось красиво?"
    boss "И ещё успел реализовать играбельный платформер?"

    maincharacter "Ну... Получается так."

    "Он проверяет дату изменения файлов и убеждается, что ты говоришь правду"

    boss "Это было глупо с твоей стороны так относиться к дедлайну."
    boss "Если ты смог сделать ТАКОЕ за 4 дня, то представь, что бы ты мог сделать, потратив на игру гораздо больше времени. Уверен, у тебя очень много времени ушло на дизайн."
    boss "И ещё кое-что. Я считаю, ты хорошо справился с дизайном, но допустил одну главную ошибку."
    boss "Ты не рассчитал свои силы. Чтобы сделать платформер за 4 дня, тебе нужно было полностью сосредоточиться на геймплее и механиках, а спрайты для окружения и персонажа взять из интернета. Так было бы гораздо лучше."
    boss "Что касается багов..."
    boss "Их просто множество!"
    boss "Да, 4 дня, времени мало, понимаю. Но как я уже говорил, нужно уметь распределять время."
    boss "Я готов сделать вердикт."
    
    maincharacter "Правда? Вот так сразу?"

    boss "Конечно, зачем тянуть?"

    maincharacter "Я вас слушаю..."

    "Твоё сердце начинает биться сильнее и сильнее, как будто оно сейчас вырвется из твоей груди и побежит делать платформер, где нужно прыгать, когда стучит сердце. Прыгать придётся очень часто."

    boss "Учитывая, что вы безответственно отнеслись к дедлайну, и потратили всего четыре дня из шести месяцев..."
    boss "При этом сделав довольно сырую игру..."
    boss "Также учитывая ваш довольно уникальный стиль рисования, в котором выполнен платформер..."
    boss "Я принимаю решение..."
    boss "...О готовности принять вас на должность стажёра дизайнера или геймдизайнера, поскольку я вижу в вас потенциал в креативной области."
    boss "Вы также совместили работу дизайнера с работой полноценного разработчика, а это очень ценный опыт."
    boss "Ну, [gg_name], что скажете?"

    maincharacter "Да! Да, чёрт возьми!"
    maincharacter "Попасть к вам - вот моя мечта. И она сбывается. Спасибо вам, я вас не подведу!"

    boss "Добро пожаловать в команду!"

label salat_epilog:
    scene bg yay with fade

    "И вот ты официально стал частью команды, и теперь ты работаешь вместе с теми, кто тебе помогал и продолжает помогать до сих пор."
    "Сева, Павел, Настя, Костян - все рады видеть тебя в дружном коллективе."
    "Вам сразу был назначен проект - соревновательная 2D-игра для четырёх игроков с элементами платформера."
    "Вы с Настей работаете над дизайном, создавая новые образы, делая интересное окружение."
    "Тебе обычно поручают что-то вроде \"укрась уровень\" или \"придумай, что тут можно добавить\"."
    "С такими задачами ты справляешься слишком легко и хочешь чего-то большего, поэтому ты решаешь взять на себя задачи по-масштабнее."
    "Ты полностью проектируешь и дизайнишь уровень в игре."
    "Ты явно добиваешься успеха в этой команде, поэтому после месяца стажировки ты становишься штатным сотрудником компании."
    "Твоя мечта стать разработчиком видеоигр не исполнилась, однако ты понял, что профессия геймдизайнера нравится тебе даже больше, и ты рад заниматься тем, чем тебе по душе."
    "И вот так заканчивается, или же только начинается история одного амбициозного геймдизайнера..."
    jump credits



label weird_salat_end:
    maincharacter "Ну... На разработку ушло где-то месяц, вроде."

    boss "Ты целый месяц разрабатывал эту игру, и ты не удосужился пофиксить эту огромную кучу багов?"

    maincharacter "Но я..."

    boss "Что ты?" 
    boss "Тебе нужно было больше времени?"
    boss "У тебя было полгода!"
    boss "Нужно было уделять больше времени для своей игры!"
    boss "Ключевая фраза здесь \"ДЛЯ ИГРЫ\", а не для дизайна. Может, если бы взял спрайты из интернета, ты бы сэкономил кучу времени и пофиксил всё это."
    
    "Ты очень сильно облажался, когда соврал про время разработки. Теперь он зол, и перечисляет все недостатки твоей игры."
    "Тебе так стыдно, что ты уже просто не можешь сказать правду, потому что Босс уже не поверит."

    boss "Но в целом... дизайн хороший. Не платформер, а именно дизайн."
    boss "Слушай, [gg_name], я вижу в тебе потенциал, просто..."
    boss "Это задание было дано, чтобы проверить тебя, и я узнал о тебе всё, что нужно."
    boss "Я готов сделать вердикт."

    maincharacter "Правда? Вот так сразу?"

    boss "Конечно, зачем тянуть?"

    maincharacter "Я вас слушаю..."

    "Твоё сердце начинает биться сильнее и сильнее, как будто оно сейчас вырвется из твоей груди и побежит делать платформер, где нужно прыгать, когда стучит сердце. Прыгать придётся очень часто."

    boss "Учитывая, что вы безответственно отнеслись к дедлайну, и потратили всего месяц из шести..."
    boss "При этом сделав довольно сырую игру..."
    boss "Также учитывая ваш довольно уникальный стиль рисования, в котором выполнен платформер..."
    boss "Я принимаю решение..."
    
    boss "..О готовности принять вас на должность стажёра-дизайнера или стажёра-геймдизайнера, поскольку я вижу в вас потенциал в креативной области."
    boss "Вы также совместили работу дизайнера с работой полноценного разработчика, а это очень ценный опыт."

    maincharacter "Ну, [gg_name], что скажете?"

    maincharacter "Да! Да, чёрт возьми!"
    maincharacter "Попасть к вам - вот моя мечта. И она сбывается. Спасибо вам, я вас не подведу!"
    
    boss "Добро пожаловать в команду!"
    jump weird_salat_epilog


label weird_salat_epilog:
    scene bg yay with fade
    "И вот ты официально стал частью команды, и теперь ты работаешь вместе с теми, кто тебе помогал и продолжает помогать до сих пор."
    "Сева, Павел, Настя, Костян - все рады видеть тебя в дружном коллективе."
    "Вам сразу был назначен проект - соревновательная 2D-игра для четырёх игроков с элементами платформера. Вы с Настей работаете над дизайном, создавая новые образы, делая интересное окружение."
    "Тебе обычно поручают что-то вроде \"укрась уровень\" или \"придумай, что тут можно добавить\"." 
    "С такими задачами ты справляешься слишком легко и хочешь чего-то большего, поэтому ты решаешь взять на себя задачи по-масштабнее. Ты  полностью проектируешь и дизайнишь уровень в игре."
    "Ты явно добиваешься успеха в этой команде, поэтому после месяца стажировки ты становишься штатным сотрудником компании."
    "Твоя мечта стать разработчиком видеоигр не исполнилась, однако ты понял, что профессия геймдизайнера нравится тебе даже больше, и ты рад заниматься тем, чем тебе по душе."
    "И вот так заканчивается, или же только начинается история одного амбициозного геймдизайнера..."
    jump credits