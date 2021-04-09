# import pytelegrambotapi
import telebot, os
from telebot import types
import time

import config
import osint_nickname
import osint_bomber
import dev_phrases
import randompic
import downloaders

bot = telebot.TeleBot(config.TOKEN)
keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('[OSINT]', '[Downloader]')
keyboard.row('[Bomber]', '[Netstalking]')

back_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
back_keyboard.row('[Назад]')


# ============== #
#    COMMANDS    #
# ============== #
@bot.message_handler(commands = ['start', 'nickname', 'randompic', 'youtube_loader'])
def start_message(message):
    if (message.text.lower() == '/start'):
        bot.send_message(message.chat.id, dev_phrases.hello, reply_markup = keyboard)
    
    if (message.text.lower() == '/randompic'):
    	bot.send_message(message.chat.id, dev_phrases.photo_searching)
    	randompic.searching(5, message.chat.id)
    	files = os.listdir(path = os.path.join(os.getcwd(), 'pics'))
    	for file in files:
    		try:
    			photo_path = os.path.join(os.getcwd(), 'pics', file)
    			link = 'http://i.imgur.com/' + file
    			bot.send_photo(message.chat.id, open(photo_path, 'rb'), caption = link)
    			
    		except BaseException:
    			print('ERROR HERE')

    	for file in files:
    		photo_path = os.path.join(os.getcwd(), 'pics', file)
    		os.remove(photo_path)

    if (message.text.lower().find('/nickname') != -1):
    	# обрезать строчку с ником (сделать объявление по кнопке)
    	# закинуть строчку в функцию из osint_nickname.py
    	# обработать файл с сайтами, создав сообщение с гиперссылками

    	nick = message.text[message.text.find(' ') + 1 : len(message.text)]
    	nick = nick.replace(' ', '')

    	bot.send_message(message.chat.id, "Ищем никнейм " + nick + " на сайтах Интернета...", reply_markup = back_keyboard)
    	osint_nickname.nickname(nick)

    	time.sleep(1)
    	filename = nick + '.txt'
    	msg = osint_nickname.converting(filename)
    	for m in msg:
    		bot.send_message(message.chat.id, m, disable_web_page_preview = True)

    if (message.text.lower().find('/youtube_loader') != -1):
    	print('yt downloading pls')
    	msg = message.text
    	link = msg[msg.find(' ') + 1 : len(msg)].replace(' ', '')

    	bot.send_message(message.chat.id, dev_phrases.youtube_video_downloading)

    	filename = os.path.join('youtube_vids', downloaders.youtube_downloader(link))

    	os.rename(filename, filename.replace(' ', '_'))
    	filename = filename.replace(' ', '_')

    	with open(filename, 'rb') as video_path:
    		bot.send_video(message.chat.id, video_path, reply_markup = back_keyboard)

    	os.remove(filename)

# ============== #
# 	   TEXT      #
# ============== #
@bot.message_handler(content_types = ['text'])
def send_text(message):
	if (message.text == '[OSINT]'):
		bot.send_message(message.chat.id, dev_phrases.osint_basic_phrase, reply_markup = back_keyboard)

	if (message.text == '[Downloader]'):
		bot.send_message(message.chat.id, dev_phrases.downloader_basic_phrase, reply_markup = back_keyboard)

	if (message.text == '[Bomber]'):
		bot.send_message(message.chat.id, dev_phrases.bomber_basic_phrase, reply_markup = back_keyboard)

	if (message.text == '[Netstalking]'):
		bot.send_message(message.chat.id, dev_phrases.netstalking_basic_phrase, reply_markup = back_keyboard)

	if (message.text == '[Назад]'):
		bot.send_message(message.chat.id, dev_phrases.hello, reply_markup = keyboard)

bot.polling(none_stop = True, timeout = 123)