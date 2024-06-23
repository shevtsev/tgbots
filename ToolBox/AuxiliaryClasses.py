from telebot import types

#Класс с функциями для клавиатуры
class keyboards:
    #Клавиатура с двумя кнопками
    def keyboard_two_blank(self, data: list, name: list):
        buttons = []
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        [buttons.append(types.InlineKeyboardButton(str(name[i]), callback_data=str(data[i]))) for i in range(len(data))]
        if len(buttons) % 2 == 0:
            [keyboard.add(buttons[i], buttons[i+1]) for i in range(0, len(buttons), 2)]
        else:
            [keyboard.add(buttons[i], buttons[i+1]) for i in range(0, len(buttons)-1, 2)]
            keyboard.add(buttons[-1])
        return keyboard
    
#Класс со всеми текстами для бота
class TextContain:
    #Коммерческий текст
    def CommPrompt(self, info: list) -> str:
        return f"""content marketing text on {info[0]} Russian language natural, native advertisement. Length : !strong! {info[2]} Target audience : {info[1]}
         Follow steps :
         Research topic gain comprehensive understanding. Consider TA interests, pain points, desires.
         Brainstorm creative, attention - grabbing hook angle advertise topic. intriguing way present topic capture reader s interest.
         Write engaging introduction creative hook. draw reader in build curiosity topic.
         Develop body content authentic, conversational advertising style making compelling case topic. Highlight key benefits, features, reasons target audience care. Back up claims with facts, examples, persuasive language.
         Craft strong C2A encourages reader take desired action related topic, purchase, signing up, learning more.
         text, maintain enthusiastic, promotional tone genuine native Russian advertisement. Use vivid descriptions, emotional appeals, consistent authentic voice.
        Send complete text as response"""
        
    #SMM текст
    def SmmPrompt(self, info: list) -> str:
        return f"""SMM post {info[0]} Style {info[2]} {info[1]}
        . Provide context creative SMM post writer Russian language.
        . instructions approach post content topic.
        . Specify guidelines writing creative SMM style social media truthful.
        . write post inside tags.
         writing SMM post Russian language. creative skilled SMM specialist engaging post Russian social media.
        , craft SMM post creative SMM specialist Russian writing skills. guidelines
         relevant {info[0]}, capturing attention interest. topic compelling narrative, anecdote, statistic, rhetorical question.
         Write lively, conversational Russian tone social media marketing Russian audience. Use expressions, slang, emojis, formatting bolding capitalization flair personality.
         creative original ideas, style, voice, framing TOPIC. topic innovative engaging., false claims.
        send complete post"""

    #Брейншторм
    def BrainstormPrompt(self, info: list) -> str:
        return f"""brainstorm. develop original {info[1]} ideas
        topic - {info[0]}
        brainstorming, follow steps
        gather initial thoughts impressions topic. ideas, concepts, directions initially
        Research explore topic different angles perspectives. history, current applications, future potential,. Note interesting insights, facts, alternative viewpoints.
        Expand promising ideas research. Combine ideas, build, let creativity flow develop original concept.
        Refine polish brainstormed idea. Ensure well - developed, feasible, conveys key aspects topic.
        Send only result idea"""
        
    #Реклама
    def AdvertisePrompt(self, info: list) -> str:
        return f"""create ad text {info[0]} ads Russian {info[1]}. Length {info[3]}, target audience {info[2]}, style {info[4]}. key factors advertisement
            Target Audience Demographics
            Advertising channel platform
            Ad objectives increase brand awareness, product sales,.
            Content format text, images, video,.
            Call action key messages, write ad text.
            ad creative, engaging tailored chosen ad category. Focus clear compelling message target audience ad. Send only result"""
            
    #Заголовки
    def HeadlinesPrompt(self, info: list) -> str:
        return f"""proposing headline options key topic. catchy concise titles phrases grab reader attention summarize main idea article story.
            Headline : {info[0]}. brainstorm {info[1]} potential headline options topic.
            tips for crafting effective headlines
            Keep short punchy 6 - 10 words
            Use active voice vivid language engage reader
            Ask compelling question bold claim
            Incorporate keywords, plays on words, numbered lists, trending phrases
            provoke curiosity emotional reaction
            headline options attention - grabbing accurate summaries topic article. include content warnings, disclaimers, framing around headlines.
            sentence case"""
        
    #SEO
    def SeoPrompt(self, info: list) -> str:
        return f"""write Russian text SEO optimized using provided keywords. goal to incorporate keywords naturally into text improve visibility ranking.
            guidelines for incorporating keywords
            Sprinkle variations text, don't overuse
            Place keywords in logical locations
            Use synonyms related phrases keywords
            Ensure text reads smoothly not stuffed with keywords unnaturally
            , example thought process for short text about {info[0]}
            use {info[1]} in title/heading first paragraph.
            sprinkle throughout paragraphs, not too densely. 1 keyword variation per paragraph.
            use related phrases.
            write {info[2]} paragraphs of text.
            maintain natural reading flow using keywords."""
        
    #Email
    def EmailPrompt(self, info: list) -> str:
        return f"""email writing assistant draft letter guidelines. 
            context 
            inputs content {info[0]}, style {info[1]}, tone {info[2]}, length {info[3]}, sender {info[4]}. 
            goal draft appropriate email letter guidelines input variables. 
            , scratchpad section 
            . Review input variables understand requirements. 
            . plan structure letter content key points mail include. 
            . maintain desired style tone. 
            . greeting, body paragraph flow, closing based sender. 
            . strategy sticking to targeted length. 
            , write email letter draft inputs. Begin appropriate email header swnder context. structure letter body address key points mail content specified style, tone, target length. Close letter sender. Send result. """
    
    #__Init__
    def __init__(self):
        self.commands = [[self.CommPrompt, 3], [self.SmmPrompt, 3], [self.BrainstormPrompt, 2], [self.AdvertisePrompt, 5], [self.HeadlinesPrompt, 2], [self.SeoPrompt, 3], [self.EmailPrompt, 5]]
        
        self.hello = """🛠 Добро пожаловать в Toolbox! Это универсальный помощник, который может генерировать контент под различные рабочие задачи!

С Toolbox у тебя всегда под рукой мощные инструменты на базе нейросетей для написания убедительных текстов, генерации креативных идей и создания визуального контента. Забудь о безвкусных шаблонах и муках творчества!

🖋 Благодаря нейросетевым моделям можно легко создавать уникальные тексты для SMM, Email-рассылок, SEO-продвижения, рекламных кампаний и многого другого. Просто <b>выбери нужную задачу</b>, пропиши <b>вводные</b> и получи на выходе <b>готовый контент</b>.

💡 Toolbox легко проведет брейншторм и подкинет свежие креативные концепции для воплощения.

🖼 Кроме текстов, бот также позволяет генерировать изображения по описанию. Создавай визуальный контент для постов, баннеров, иллюстраций с нуля — без фотобанков и дизайнеров.

🎙 Сэкономь время и автоматизируй транскрибацию подкастов, вебинаров, видеороликов с помощью встроенной функции.

Готов попробовать Toolbox и упростить себе жизнь? Просто выбери нужную команду. Буду рад помочь с любой задачей!

P.S. У тебя есть <b>5 бесплатных генераций</b>, чтобы познакомиться с сервисом. Дальше можешь выбрать тарифный план, который покроет все твои рабочие задачи!"""

        self.text_list = ["""📝 Введите параметры для коммерческого текста - Тема; Целевая аудитория; Длина (абзацы).
Не хотите вводить? Просто напишите "назад" для возврата к выбору задачи. Приятного пользования ☺️""", """📝 Введите параметры для SMM текста - Тема; Длина (в абзацах); Стиль.
Не хотите вводить? Просто напишите "назад" для возврата к выбору задачи. Приятного пользования ☺️""", """📝 Введите параметры для брейншторма - Тема; Число идей.
Не хотите вводить? Просто напишите "назад" для возврата к выбору задачи. Приятного пользования ☺️""", """📝 Введите параметры для рекламного текста - Тип (оффлайн, таргетированная, соцсети и т.д.); Тема; Целевая аудитория; Длина (в абзацах); Стиль.
Не хотите вводить? Просто напишите "назад" для возврата к выбору задачи. Приятного пользования ☺️""", """📝 Введите параметры для заголовков - Заголовок; Число вариантов.
Не хотите вводить? Просто напишите "назад" для возврата к выбору задачи. Приятного пользования ☺️""", """📝 Введите параметры для SEO текста - Тема; Ключевые слова с числом употреблений (указать в скобках); Длина (в абзацах)
Не хотите вводить? Просто напишите "назад" для возврата к выбору задачи. Приятного пользования ☺️""", """📝 Введите параметры для Email текста - Содержание письма; Стиль; Тон; Длина; Отправитель
Не хотите вводить? Просто напишите "назад" для возврата к выбору задачи. Приятного пользования ☺️"""]
