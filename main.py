from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
#make Python speak
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

bot= ChatBot('Test')
conv=open('chats.txt','r').readlines()
bot.set_trainer(ListTrainer)
bot.train(conv)
while True:

	request=input('You:')
	response=bot.get_response(request)
	print('Bot:',response)
	speak.Speak(response)