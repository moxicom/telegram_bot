import telebot
from random import choice
import requests


def get_rand_video():
    res = requests.get('https://randomvideo.pythonanywhere.com/')
    link = res.text.find('https:')
    return res.text[link:link + 52]


def take_list():
    file = open('items.txt')
    _items = file.readlines()
    file.close()
    return _items


def add_to_list(item):
    if not (item + '\n' in item):
        file = open('items.txt', 'a')
        file.write(item + '\n')
        file.close()
        items.append(item + '\n')
    else:
        print('уже было')


def send_command_list(message, commands):
    markup = telebot.types.ReplyKeyboardMarkup()
    for item in commands:
        markup.row(telebot.types.KeyboardButton('/' + item))
    bot.reply_to(message, 'Вот команды кароч:', reply_markup=markup)


bot = telebot.TeleBot('5555273889:AAFWKNbyyL182bXjXwqxZCspqGdrG0Z3lyM')
command_list = ['help', 'анекдот', 'видос']
items = take_list()


@bot.message_handler(commands=['help'])
def helper(message):
    send_command_list(message, command_list)


@bot.message_handler(commands=['анекдот'])
def joke(message):
    bot.reply_to(message, 'да пошел ты нафиг рэально, какие шутки')
    print('added joke')


@bot.message_handler(commands=['видос'])
def video(message):
    bot.send_message(message.from_user.id, get_rand_video())
    print('added video')


@bot.message_handler(commands=['мем'])
def meme(message):
    bot.send_photo(message.from_user.id, photo=open('photo.jpg', 'rb'))
    bot.register_next_step_handler(message, message.text)


def take_next_message(message):
    bot.send_message(message.from_user.id, message.text)


@bot.message_handler(content_types=['text'])
def start(message):
    txt = message.text
    if txt.lower()[:2] == 'ау':
        bot.send_message(message.from_user.id, txt + 'у')
    else:
        bot.register_next_step_handler(message, take_next_message)
        add_to_list(message.text)
        chosen_phrase = choice(list(items))
        bot.send_message(message.from_user.id, chosen_phrase)
        print(f'user {message.from_user.id} added: {message.text}')
        print(f'answer: {chosen_phrase}' + '-' * 20)



bot.polling(none_stop=True)
