import telebot
from random import choice
import json

bot = telebot.TeleBot('5555273889:AAFWKNbyyL182bXjXwqxZCspqGdrG0Z3lyM')
command_list = ['аууу', 'лан, нет никаких команд']


def take_list():
    file = open('items.json')
    json_string = file.read()
    json_data = json.loads(json_string)
    _items = list(json_data)
    file.close()
    return _items


def add_to_list(item):
    _items = take_list()
    _items.append(item)
    _items = list(set(_items))
    file = open('items.json', 'w')
    json.dump(_items, file, indent=4)
    items.append(item)
    file.close()


items = take_list()


@bot.message_handler(content_types=['text'])
def start(message):
    add_to_list(message.text)
    print(f'added {message.text}')
    bot.send_message(message.from_user.id, choice(list(items)))
    # print(list(set_items))


@bot.message_handler(commands=['help'])
def helper(message):
    bot.reply_to(message.from_user.id, 'вот список команд:\n' + '\n'.join())


bot.polling(none_stop=True)
