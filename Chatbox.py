from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

# create a chatbot instance
chatbot = ChatBot('MyBot')

# create a new trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# train the chatbot with the english corpus
trainer.train("chatterbot.corpus.english")
