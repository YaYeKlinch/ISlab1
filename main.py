import telebot
import re
import random
from array import *

answer1 = ["dont know","yes","no"] #for questions
answer2 = ["Yes, I " ,"No I do not"] #for do you questions
answer3 = ["You" , "Somebody","Me"] #for who questions
answer4 = ["Ukraine" ,"Somewhere","Kyiv"] #where answer
questions = ["what" , "where" , "why" , "who" "when" , "which"]

bot = telebot.TeleBot("1695581677:AAH8nmrRLTyyqVrojW4PufCsBLGN0qCuQLE", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привіт, як справи")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "slava ukraini":
      bot.send_message(message.from_user.id, "Героям Слава!")
    elif message.text.lower() == "gachi":
      bot.send_message(message.from_user.id, "muchi")
    elif do_you_find(message.text.lower()):
        bot.send_message(message.from_user.id, do_you_answer(message.text.lower()))
    elif question_find(message.text.lower()):
        bot.send_message(message.from_user.id,random_answer1())
    elif find_who(message.text.lower()):
        bot.send_message(message.from_user.id, who_answer())
    elif find_where(message.text.lower()):
        bot.send_message(message.from_user.id, where_answer(message.text.lower()))
    elif find_when(message.text.lower()):
        bot.send_message(message.from_user.id, when_answer())
    else:
      bot.send_message(message.from_user.id , "каво")

def random_answer2():
    x = random.randint(0,1)
    return answer2[x]
def do_you_find(message):
    return "do you" in message
def do_you_answer(message):
    result = re.findall("do you", message)
    if "do you" in message:
        return random_answer2() + message.partition("do you")[2]

def random_answer1():
     x = random.randint(0, 2)
     return answer1[x]

def question_find(message):
     for x in questions:
         if x not in message:
             continue
         else:
             return False
     if message.endswith("?"):
             return True
     return False

def who_answer():
    x = random.randint(0, 1)
    return answer3[x]
def find_who(message):
    if "who" in message:
        return True
    return False

def find_where(message):
    if "where" in message:
        return True
    return False
def random_where():
    x = random.randint(0, 2)
    return answer4[x]
def where_answer(message):
    answer_part = message.partition("where")[2]
    if len(answer_part)==0:
        return "kavo"
    answer_array = answer_part.split()
    return answer_array[1].replace("you" , "I") + " in " + random_where()

def find_when(message):
    if "when" in message:
        return True
    return False
def when_answer():
    x = random.randint(0, 2021)
    return "It was in " + str(x)

bot.polling(none_stop=True)

