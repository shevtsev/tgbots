import telebot, os, dotenv
from AuxiliaryClasses import TextContain, keyboards
from ToolBox_n_networks import neural_networks

txt = TextContain()

#Загрузка переменных окружения
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

#commands functions class
class ToolBox(keyboards, neural_networks):
    def __init__(self):
        #telebot
        self.bot = telebot.TeleBot(os.environ['TOOL_BOX_TG_ID'])
            
    #Ожидание ответа
    def delay(self, message):
        return self.bot.send_message(message.chat.id, "Подождите, это должно занять несколько секунд . . .", parse_mode='html')

    #Start
    def start_request(self, message):
        name = ["Текст 📝", "Изображения 🎨", "Аудио 🗣️"]
        data = ["text", "images", "audio"]
        keyboard = super().keyboard_two_blank(data, name)
        return self.bot.send_message(message.chat.id, txt.hello, reply_markup=keyboard, parse_mode='html')
    
    #Restart
    def restart(self, message):
        name = ["Текст 📝", "Изображения 🎨", "Аудио 🗣️"]
        data = ["text", "images", "audio"]
        keyboard = super().keyboard_two_blank(data, name)
        return self.bot.send_message(message.chat.id, "Выберите нужную вам задачу", reply_markup=keyboard)
        
    #Текст
    def text_area(self, call):
        name = ["Коммерческий  🛍️", "SMM 📱", "Брейншторм 💡", "Реклама 📺", "Заголовки 🔍", "SEO 🌐", "Email 📧"]
        data = ["comm-text", "smm-text", "brainst-text", "advertising-text", "headlines-text", "seo-text", "email"]
        keyboard = super().keyboard_two_blank(data, name)
        return self.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📝 Выберите тип текста", reply_markup=keyboard)
    
    #Запуск cloud sonnet
    def cloud_send(self, prompt: str, message):
        send = self.delay(message)
        self.bot.edit_message_text(chat_id=send.chat.id, message_id=send.message_id, text=super().cloud_sonnet(prompt))

    #Запуск Кандинского
    def kandinsky(self, prompt: str, message):
        send = self.delay(message)
        self.bot.send_photo(message.chat.id, super().FusionBrain(prompt))
        self.bot.delete_message(send.chat.id, send.message_id)
    
###Тексты
    def TextArea(self, call, ind: int):
        return self.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=txt.text_list[ind])
        
    def TextCommands(self, message, ind: int):
        info = message.text.split(';')
        if len(info)==txt.commands[ind][1]:
            prompt = txt.commands[ind][0](info)
            self.cloud_send(prompt, message)
        return self.restart(message)
###

###Изображения
    def ImageArea(self, call):
        return self.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введите ваш запрос для изображений 🖼")
    
    def ImageCommand(self, message):
        self.kandinsky(message.text, message)
        return self.restart(message)
###