from telebot import types, TeleBot
from random import choice
import requests
import meme_creator


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


bot = TeleBot('5555273889:AAFWKNbyyL182bXjXwqxZCspqGdrG0Z3lyM')
command_list = ['help', 'анекдот', 'видос', 'мем']
items = take_list()


@bot.message_handler(commands=['help'])
def helper(message):
    markup = types.ReplyKeyboardMarkup()
    for item in command_list:
        markup.row(types.KeyboardButton('/' + item))
    bot.reply_to(message, 'Вот команды кароч:', reply_markup=markup)


@bot.message_handler(commands=['анекдот'])
def joke(message):
    bot.reply_to(message, 'да пошел ты нафиг рэально, какие шутки')
    print('added joke')


@bot.message_handler(commands=['видос'])
def video(message):
    res = requests.get('https://randomvideo.pythonanywhere.com/')
    link_ind = res.text.find('https:')
    link = res.text[link_ind:link_ind + 52]
    bot.send_message(message.from_user.id, link)
    print('added video')


@bot.message_handler(commands=['мем'])
def photo_meme(message):
    _list = meme_creator.meme_list
    markup = types.ReplyKeyboardMarkup()
    for item in _list:
        markup.row(types.KeyboardButton(item))
    msg = bot.reply_to(message, 'выбирите шаблон', reply_markup=markup)
    bot.register_next_step_handler(msg, choose_photo_meme)


photo_meme_type = ''


def choose_photo_meme(message):
    photo_meme_type = message.text
    msg = bot.send_message(message.from_user.id, 'отлично, теперь введите текст')
    bot.register_next_step_handler(msg, sent_photo_meme)


def sent_photo_meme(message):
    text = message.text
    #func = getattr(meme_creator, photo_meme_type)
    bot.send_photo(message.from_user.id, meme_creator.ronaldo(text))


@bot.message_handler(content_types=['text'])
def start(message):
    txt = message.text
    if txt.lower()[:2] == 'ау':
        bot.send_message(message.from_user.id, txt + 'у')
    else:
        add_to_list(message.text)
        chosen_phrase = choice(list(items))
        bot.send_message(message.from_user.id, chosen_phrase)
        print(f'user {message.from_user.id} added: {message.text}')
        print(f'answer: {chosen_phrase}' + '-' * 20)


bot.polling(none_stop=True)
