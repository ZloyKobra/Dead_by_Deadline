label yellow_scene_1:


    "Очередной день. Кажется, ты уже начинаешь уставать. Но не время унывать!"
    "Игра уже считай готова, нужны лишь пара механик, случайные события, спрайты."
    "И вот ты решил сделать себе небольшой отдых, вкусно пообедать, и тут..."
    jump big_scene_2

label yellow_scene_2:
    
    maincharacter "Без паники! у меня уже почти всё готово! Нужны лишь пара механик и спрайтов..."
    maincharacter "Не будет мне никакого отдыха в эти 2 дня!"
    maincharacter "За работу!!"
    maincharacter "Найду модельки в интернете, чёрт с ними!"

    "Отлично! Примерно час поиска в открытых источниках и подходящие модели есть!"
    "Ты подобрал те самые спрайты, которые хотел - инопланетные посетители, кафе, космос."
    "Ты начинаешь программировать механику обслуживания, случайные события, улучшения, приготовление блюд. Всё это без сюжета, ведь на это просто нет времени."
    "Эту ночь ты практически не спишь... До четырёх часов ночи ты программируешь и попутно исправляешь придуманные механики, и у тебя..."
    "...Получилось! Ты сделал это! Ты засыпаешь прямо на столе перед ноутбуком."
    jump end_day_3

label yellow_scene_3:
    maincharacter "Я работаю над казуалкой, где нужно управлять кафешкой, но некоторые вещи всё еще не успел реализовать."
    maincharacter "Если честно, мне бы очень пригодилась помощь с финальными доработками — багами и оптимизацией."

    show pavel calm1:
        xalign 0.8
        yalign 1.05
    "Ты даёшь ему сыграть в твой прототип игры."
    show gg calm1:
        xalign 0.2
        yalign 1.05

    pavel "Хм, ну, выглядит неплохо, давай проверим механики..."
    pavel "Ага! Если слишком часто нажимать на потребность клиента, то всё ломается. Сейчас исправим!"

    "Он молниеносно находит эту механику в коде и исправляет её, а ты даже не успеваешь уследить за его действиями"
    jump big_scene_4



label yellow_scene_END_IS_NEAR:
    show boss hands_:
        xalign 0.3
        yalign 1.05
    boss "Итак, [gg_name]. Я ждал вас."
    boss "Не будем тянуть. Начнём."

    "Твоя ладонь крепче сжимает флешку, и ты быстро подходишь к компьютеру, подключаешь её к порту." 
    "Ты включаешь игру, и на экране появляется главное меню — результат дней и ночей работы, испытание для твоих навыков и терпения."
    "Открывается первый уровень, и ты слышишь..."

    boss "Прошу, сначала расскажите про вашу игру. Что она из себя представляет?"

    show gg speak_:
        xalign 0.8
        yalign 1.05
    maincharacter "Симулятор управления межпланетным кафе! Приходят инопланетные клиенты, заказывают какое-то блюдо, иногда очень специфичное, ты должен достать нужные ингредиенты, приготовить блюдо, отдать клиенту."
    maincharacter "Чем быстрее сделано блюдо, тем больше денег получаешь, при условии что блюдо сделано по рецепту правильно. Можно улучшать кафе и нанимать персонал."
    
    show boss speak_:
        xalign 0.3
        yalign 1.05
    boss "Очень оригинальный концепт. Воображение то, что нужно."
    show boss hands_:
        xalign 0.3
        yalign 1.05
    boss "Ну, посмотрим, как ты всё это реализовал. Продемонстрируй, как ты играешь."

    "Ты нажимаешь кнопку \"ИГРАТЬ\" в главном меню. Начинает играть приятная музыка из интернета, появляется кафешка, приходит клиент, он заказывает простой бургер, ты нажимаешь на нужные для приготовления кнопки, проходишь мини-игру - бургер готов, клиент доволен, +10 внутриигровой валюты."
    "Босс, кажется, не впечатлён."

    boss "Понятно... Теперь позволь сыграть мне."   

    show gg calm2:
        xalign 0.8
        yalign 1.05
    maincharacter "Да, конечно... прошу."

    show boss calm:
        xalign 0.3
        yalign 1.05
    "Ты передаешь клавиатуру и мышь Боссу"
    "Он делает то же самое, исполняет более сложные заказы посетителей, накапливает денег на улучшение кафешки, ставит новый стол, всё работает нормально."
    "Однако в один момент клиенты просто перестают уходить из кафе даже после исполнения заказа, что препятствует дальнейшему прохождению. Странно, раньше такого не было."

    boss "Мгм, Софтлок... понятно. Ну, я узнал достаточно"
    boss "Ещё и спрайты взяты из интернета."

    boss "Так, ладно. Баги. Расскажи, как ты с ними справлялся?"

    show gg calm1:
        xalign 0.8
        yalign 1.05
    maincharacter "Когда я сделал первую версию игры, у меня было довольно много багов, таких как неработающая механика клиентов, невозможность приготовить блюдо."
    maincharacter "Критические баги мне помог пофиксить ваш сотрудник, Павел. Некоторую часть я исправил после встречи с ним, после того, как я научился правильно находить и фиксить баги."
    maincharacter "Часть багов также отпала, когда я делал рефакторинг кода. На исправление оставшихся багов просто не хватило времени..."
    
    show boss hands_:
        xalign 0.3
        yalign 1.05
    boss "Оу, так ты уже и с сотрудниками познакомился? И даже поработать с ними успел? Это, несомненно, большой плюс."

    maincharacter "Да, ваши сотрудники довольно отзывчивы, и не только Павел. Они мне помогли в разработке игры."

    boss "Да, именно таких мы и берём в нашу команду."
    boss "А теперь скажи-ка мне честно, мы дали тебе на разработку игры полгода, сколько из этого времени вы потратили на свою игру, что тебе не хватило времени, чтобы исправить баги?"
    menu:
        "4 Дня. (сказать правду)":
            jump yellow_end
        "Ну... где-то месяц (солгать)":
            jump ouuuu_eeee_mister_krabs_end

label yellow_end:
    show gg calm2:
        xalign 0.8
        yalign 1.05
    maincharacter "Я начал разработку 4 дня назад, когда пришло ваше письмо..."
    maincharacter "Я так увлёкся видеоиграми и развлечениями, что забыл о дедлайне..."

    show boss speak_:
        xalign 0.3
        yalign 1.05
    boss "То есть ты хочешь сказать, что ты создал ЭТУ игру за 4 дня?!"
    boss "Красивая казуалка с кучей классных реализованных механик?!"

    maincharacter "Ну... Получается так."

    "Он проверяет дату изменения файлов и убеждается, что ты говоришь правду"
    show boss hands_:
        xalign 0.3
        yalign 1.05
    boss "Это было глупо с твоей стороны так относиться к дедлайну." 
    boss "Если ты смог сделать ТАКОЕ за 4 дня, то представь, что бы ты мог сделать, потратив на игру гораздо больше времени."
    boss "Это просто невероятно, [gg_name]!"
    boss "Теперь я вовсе не виню тебя за то, что ты взял готовые спрайты из интернета, это было лучшее решение, чтобы больше времени потратить на разработку."
    boss "Так это всё ещё и очень хорошо смотрится в твоей игре!"
    boss "Что касается багов..."
    boss "Это совершенно нормально! Всего 4 дня разработки, полного отсутствия багов невозможно добиться в такой короткий срок, это полностью оправдано."
    boss "Уверен, будь у тебя больше времени, ты бы несомненно справился, ведь так?"
    show gg calm1:
        xalign 0.8
        yalign 1.05
    maincharacter "Так точно, сэр!"

    boss "Я и не сомневался."   
    boss "Я готов сделать вердикт."

    maincharacter "Я вас слушаю..."

    "Твоё сердце начинает биться сильнее и сильнее, как будто оно сейчас улетит в космос пить межгалактический кофе."
    show boss calm:
        xalign 0.3
        yalign 1.05
    boss "Несмотря на то, что вы безответственно отнеслись к дедлайну, и потратили всего четыре дня из шести месяцев..."
    boss "Вы сумели сделать отличную игру в такой короткий срок!"
    boss "Я готов принять вас к себе полноценным разработчиком в нашу Компанию!"    
    boss "Ну, [gg_name], что скажете?"

    show gg shock_:
        xalign 0.8
        yalign 1.05
    maincharacter "Да! Да, чёрт возьми!"
    maincharacter "Попасть к вам - вот моя мечта. И она сбывается. Спасибо вам, я вас не подведу!"

    boss "Добро пожаловать в команду!"
    jump yellow_epilog


label yellow_epilog:
    scene bg yay with fade
    "И вот ты официально стал частью команды, и теперь ты работаешь вместе с теми, кто тебе помогал и продолжает помогать до сих пор."
    "Сева, Павел, Настя, Костян - все рады видеть тебя в дружном коллективе."
    "Вам сразу был назначен проект - соревновательная 2D-игра для четырёх игроков с элементами платформера."
    "Ты легко реализуешь все те механики, которые вы вместе продумали."
    "Вы обсуждаете код, исправляете баги, придумываете что-то новое, проектируете."
    "Ты явно добиваешься успеха в этой команде, поэтому Босс радует тебя частыми премиями."
    "Твоя мечта сбылась - ты наконец становишься разработчиком видеоигр в одной из лучших компаний в окружении людей, которые всегда готовы помочь."
    "И вот так заканчивается, или же только начинается история одного амбициозного разработчика видеоигр..."
    jump credits


label ouuuu_eeee_mister_krabs_end:
    show gg calm2:
        xalign 0.8
        yalign 1.05
    maincharacter "Ну... На разработку ушло где-то месяц, вроде."

    show boss speak_:
        xalign 0.3
        yalign 1.05
    boss "Ты целый месяц разрабатывал эту игру, и ты не удосужился пофиксить критический баг?"

    maincharacter "Но я..."

    show boss calm:
        xalign 0.3
        yalign 1.05
    boss "Что ты?"
    boss "Тебе нужно было больше времени?"
    boss "У тебя было полгода! Нужно было уделять больше времени для своей игры!"
    boss "Ты еще и ассеты из интернета взял..."

    "Ты очень сильно облажался, когда соврал про время разработки."
    "Теперь он зол, и перечисляет все недостатки твоей игры."
    "Тебе так стыдно, что ты уже просто не можешь сказать правду, потому что Босс уже не поверит."

    show boss hands_:
        xalign 0.3
        yalign 1.05
    boss "Но в целом... Игра очень оригинальна и разнообразна."
    boss "А ещё она затягивает. Честно, мне действительно хочется в неё продолжить играть."
    boss "И да, дизайн игры, украденный тобой из интернета, действительно смотрится органично с твоим геймплеем."
    boss "Это задание было дано, чтобы проверить тебя, и я узнал о тебе всё, что нужно."
    boss "Я готов сделать вердикт."

    show gg calm1:
        xalign 0.8
        yalign 1.05
    maincharacter "Правда? Вот так сразу?"

    boss "Конечно, зачем тянуть?"

    maincharacter "Я вас слушаю..."

    "Твоё сердце начинает биться сильнее и сильнее, как будто оно сейчас улетит в космос пить межгалактический кофе."
    
    show boss calm:
        xalign 0.3
        yalign 1.05
    boss "Учитывая, что вы безответственно отнеслись к дедлайну, и потратили всего месяц, при этом сделав финальный продукт, не протестировав его..."
    boss "Также учитывая, что задумка игры это что-то с чем-то, и геймплей реализован достойно..."
    boss "В общем..."
    boss "Я вижу вы очень способны, поэтому я готов принять вас на испытательный срок в 1 месяц, а дальше уже посмотрим, брать вас или нет."
    boss "Надеюсь, мы сможем выделить средства и команду на дальнейшую проработку этой игры."
    boss "Ну, [gg_name], что скажете?"

    show gg shock_:
        xalign 0.8
        yalign 1.05
    maincharacter "Да! Я готов к вам присоединиться!"
    maincharacter "Это была моя мечта, и она сбывается. Спасибо вам!"

    boss "Добро пожаловать в команду!"
    jump mister_crabs_epilog

label mister_crabs_epilog:
    scene bg yay with fade
    "И вот ты официально стал частью команды, и теперь ты работаешь вместе с теми, кто тебе помогал и продолжает помогать до сих пор."
    "Сева, Павел, Настя, Костян - все рады видеть тебя в дружном коллективе."
    "Весь свой испытательный срок тебя назначили доработать одну из игру компаний - Mecha Strike, 3D-шутер, где игроки в роботах уничтожают друг друга."
    "По началу тебе трудно работать с 3D-игрой, но ты довольно быстро привыкаешь."
    "Ты явно добиваешься успеха в этой команде, поэтому после испытательного срока Босс назначает тебя главным программистом той самой игры, которую ты показывал Боссу при устройстве на работу."
    "Теперь ты вместе с командой будешь полноценно разрабатывать и развивать свою игру. И имя ей - Intergalactic Cafe."
    "И вот так заканчивается, или же только начинается история одного амбициозного разработчика видеоигр..."
    jump credits