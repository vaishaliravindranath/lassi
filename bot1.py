#pip install chatterbot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

chatterbot = ChatBot("Training Example")
chatterbot.set_trainer(ChatterBotCorpusTrainer)
chatterbot.train("chatterbot.corpus.english")
while True:

	request=input('You:')
	response=chatterbot.get_response(request)
	print('Bot:',response)
	speak.Speak(response)