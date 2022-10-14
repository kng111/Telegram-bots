from telegram.ext.dispatcher import run_async
import requests
import telebot
import sqlite3
bot = telebot.TeleBot('TOKEN')
img = open('fotoWOman.jpg', 'rb')

while True:
        db = sqlite3.connect('drMO.db')
        cur = db.cursor()

        photo2 = 'fotoWOman.jpg'
        photo = 'fotoMan.jpg'


        # vremy1 = '09:00:00' МО
        vremy1 = '20:07:00'

        chat_id1 = id_chat


        TOKEN = 'TOKEN'
        URL = 'https://api.telegram.org/bot'
        import datetime
        import time
        now = datetime.datetime.now()
        data = str(now.strftime("%m"))
        dr = str(now.strftime("%m"))
        dr = (f'{data}/{now.day}')
        def send_photo_file1(chat_id, img,text):
                                    files = {'photo': open(img, 'rb')}
                                    data = {'caption': text}
                                    requests.post(f'{URL}{TOKEN}/sendPhoto?chat_id={chat_id}', files=files,data=data)
        while True:
            time.sleep(1)
            now = datetime.datetime.now()
            vremy = (now.strftime("%H:%M:%S"))
            print(vremy)
            data = str(now.strftime("%m"))
            dr = str(now.strftime("%m"))
            dr = (f'{data}/{now.day}')
            # print(dr)
            def pereborEND(dr):
                                        cur.execute(f'SELECT imy FROM table1 WHERE DR = "{dr}"')
                                        result = cur.fetchall()

                                        list = []
                                        for i in range(len(result)):
                                            x = result[i]
                                            list.append(x)
                                        for i in range(len(list)):
                                            x2 = (str(list[i])[2:-3])
                                            # print(x2)
                                            def pozdarvPol(x2,dr):
                                                        print(dr)
                                                        cur.execute(f'SELECT pol FROM table1 WHERE imy = "{x2}" AND dr = "{dr}"')
                                                        result = cur.fetchall()
                                                        for i in range(len(result)):
                                                            if result[i] == ('М',):
                                                                text = [f'Уважаемый, {x2}!Поздравляем Вас с Днём рождения!\nЖелаем Вам оставаться таким же внимательным, тактичным, целеустремлённым, понимающим и справедливым.\nПусть все Ваши планы и идеи реализуются. Успехов Вам в Вашей работе, силы и энергии, благополучия, взаимопонимания и крепкого здоровья!\nКоллектив Союза директоров ССУЗ Московской области']
                                                                if vremy == vremy1:
                                                                        send_photo_file1(chat_id1,photo,text)
                                                        for i in range(len(result)): 
                                                            if result[i] == ('Ж',):
                                                                # imy1 = (perebor1(dr)[i])
                                                                text = [f'Дорогая, незаменимая {x2}!\nВсем коллективом Союза директоров ССУЗ Московской области поздравляем Вас с Днём Вашего рождения! Пусть Вам всегда сопутствует удача, пусть дом будет полная чаша, радует достаток, а работа приносит только удовольствие!С днем рождения!']
                                                                if vremy == vremy1:
                                                                        send_photo_file1(chat_id1,photo2,text)
                                            pozdarvPol(x2,dr)
            pereborEND(dr)

