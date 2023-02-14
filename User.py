from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# create a chatbot instance
chatbot = ChatBot('MyBot')

# create a new trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# train the chatbot with the english corpus
trainer.train("chatterbot.corpus.english")

# create a Flask app instance
app = Flask(__name__)

# create a route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# create a route for the chatbot API
@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    bot_response = str(chatbot.get_response(user_text))
    return bot_response

if __name__ == "__main__":
    app.run()
