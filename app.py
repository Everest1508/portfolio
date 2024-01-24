from flask import Flask,render_template, request,send_file
from telegram import ParseMode,InlineKeyboardButton, InlineKeyboardMarkup
import telegram.ext
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext import ConversationHandler,CallbackQueryHandler
from telegram.ext.filters import Filters
API_KEY = ""
updater =Updater(API_KEY,use_context=True)
app = Flask(__name__)

app.use_static_for = "static"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forms/contact.php', methods=['POST'])
def contact_form():
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")
    print(name)
    print(email)
    print(subject)
    print(message)
    updater.bot.sendMessage(chat_id='964837397', text ="Name : {0}\nEmail : {1}\nSubject : {2}\nMessage : {3}".format(name,email,subject,message))
    return "Contact form submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True)
