import json, telebot, sqlite3, os, subprocess, base64
from time import sleep
from telebot import types
from Texts import TextContain
from Images import Text2ImageAPI

txt = TextContain()

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

#Класс базы данных
class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect('UsersData.db')
        self.cursor = self.conn.cursor()
    
    #Создание базы данных
    def create(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users_data_table
                          (id TEXT PRIMARY KEY,
                           image BOOLEAN,
                           comm BOOLEAN,
                           smm BOOLEAN,
                           brainst BOOLEAN,
                           advertising BOOLEAN,
                           headlines BOOLEAN,
                           seo BOOLEAN,
                           email BOOLEAN)''')
        self.conn.close()
        
    #Функция для вставки или обновления данных в базе
    def insert_or_update_data(self, record_id: str, values: list):
        conn = sqlite3.connect('UsersData.db')
        cursor = conn.cursor()
        placeholders = ', '.join(['?'] * len(values))
        update_query = f"REPLACE INTO users_data_table (id, image, comm, smm, brainst, advertising, headlines, seo, email) VALUES (?, {placeholders})"
        cursor.execute(update_query, [record_id] + values)
        conn.commit()
        conn.close()

    #Функция обновления массива
    def load_data_from_db(self) -> dict:
        loaded_data = {}
        conn = sqlite3.connect('UsersData.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, image, comm, smm, brainst, advertising, headlines, seo, email FROM users_data_table")
        rows = cursor.fetchall()
        for row in rows:
            record_id = row[0]
            values_list = [bool(col) for col in row[1:]]
            loaded_data[record_id] = values_list
        conn.close()
        return loaded_data
        
#Класс с нейросетями
class neural_networks:
    #Cloud curl request
    def cloud_sonnet(self, prompt: str) -> str:
        payload = {
            "model": "claude-3-sonnet-20240229",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1024
        }

        cmd = ["curl", "-X", "POST",
               "https://api.proxyapi.ru/anthropic/v1/messages",
               "-H", "Content-Type: application/json",
               "-H", f"Authorization: Bearer {os.environ['CLOUDE_ID']}",
               "-H", "Anthropic-Version: 2023-06-01",
               "-d", json.dumps(payload)]

        process = subprocess.run(cmd, capture_output=True, text=True)
        sleep(5)
        response = json.loads(process.stdout)
        return response.get('content')[0]['text']
    
    #Кандинский
    def FusionBrain(self, prompt: str) -> str:
        api = Text2ImageAPI('https://api-key.fusionbrain.ai/', os.environ["API_KEY"], os.environ["SECRET_KEY"])
        model_id = api.get_model()
        uuid = api.generate(prompt, model_id)
        images = api.check_generation(uuid)
        return base64.b64decode((images[0]))
        
#commands functions class
class ToolBox(keyboards, neural_networks):
    def __init__(self, tg_token: str):
        #telebot
        self.tg_token = tg_token
        self.bot = telebot.TeleBot(self.tg_token)
        self.hello = txt.hello
            
    #Ожидание ответа
    def delay(self, message):
        return self.bot.send_message(message.chat.id, "Подождите, это должно занять несколько секунд . . .", parse_mode='html')

    #Start
    def start_request(self, message):
        name = ["Текст 📝", "Изображения 🎨", "Аудио 🗣️"]
        data = ["text", "images", "audio"]
        keyboard = super().keyboard_two_blank(data, name)
        return self.bot.send_message(message.chat.id, self.hello, reply_markup=keyboard, parse_mode='html')
    
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