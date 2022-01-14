import telebot

bot = telebot.TeleBot("5041565448:AAFOIB1jmxHtAfZ94FVX_6CM5vLjCaBgLFI")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	#bot.reply_to(message, message.text)
	bot.send_message (message.chat.id, message.text)

bot.polling( none_stop = True)