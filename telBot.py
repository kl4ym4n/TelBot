import os
import telebot
import tokens
import random
from datetime import datetime
import urllib.request as urllib2
bot = telebot.TeleBot(tokens.token)
print(bot.get_me())


def log(message, answer):
    print("\n ---------")
    print(datetime.now())
    print('Message from [0] [1]. (id = [2]) \n Text = [3]'.format(message.from_user.user_first_name,
                                                                  message.from_user.user_last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print(answer)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, 'This is help settings')


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('Photo', 'Audio', 'Doc')
    user_markup.row('Sticker', 'Video', 'Voice', 'Location')
    bot.send_message(message.from_user.id, 'Welcome', reply_markup=user_markup)


@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '...', reply_markup=hide_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Photo':
        directory = 'C:\Data\Python_Projects\TelBot\photos'
        # urllib2.urlretrieve(url, 'url_image.jpg')
        # image = open('url_image.jpg', 'rb')
        all_files = os.listdir(directory)
        random_file = random.choice(all_files)
        image = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, image)
        image.close()
    elif message.text == 'Audio':
        audio = open('C:\Data\Python_Projects\TelBot\music\Who\'s With Me.mp3', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()
    elif message.text == 'Doc':
        bot.send_message(message.from_user.id, 'Not available')
    elif message.text == 'Video':
        bot.send_message(message.from_user.id, 'Not available')
    elif message.text == 'Voice':
        bot.send_message(message.from_user.id, 'Not available')
    elif message.text == 'Sticker':
        bot.send_sticker(message.from_user.id, 'CAADBAADXAADXSupATtI_RyIWnrvAg')
    elif message.text == 'Location':
        bot.send_chat_action(message.from_user.id, 'find_location')
        bot.send_location(message.from_user.id, '54.853661', '83.040308')


bot.polling(none_stop=True, interval=0)
