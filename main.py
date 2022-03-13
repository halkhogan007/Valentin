import vk_api
import random
import datetime
import requests
import json
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def write_message(sender, message):
    authorize.method('messages.send',
                     {'chat_id': sender,
                      'message': message,
                      "random_id": get_random_id(),
                      }
                     )


global kassa
global kassa1
token = "b792fe3f28bcc1a1ddefaf1c0af97b8f81836f51491b795b48ce448937410d38e27633557bed67d069924"
authorize = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(authorize, group_id=207618594)
monetka_list = ['орел', 'решка']
koronka_list = ['Лучше быть хорошим чем плохим', 'Награда найдет своего героя', 'И Тюниса позовите',
                ' в 8:15 все сержанты около моего кабинета']
spisok_vzvoda = ['Макрицкий А.М.\nБуйко А.А.\nБегунец П.О.\nВоронкович А.С.\n'
                 'Крот А.А.\nГридюшко И.Г.\nПетров В.Д.\nНовак А.А.\nСвириденко Е.В.\nКузьменков С.В.\n'
                 'Мартыненков Ю.Ю.\nМончиков А.Е.\nЧернов К.И.\nКот Е.Л.\nИванюкович И.А.\n'
                 'Мелеховец К.А.\nГалабурда С.И.\n']
vzvod_list = ['Макрицкий А.М.', 'Буйко А.А.', 'Бегунец П.О.', 'Воронкович А.С.', 'Крот А.А.',
              'Гридюшко И.Г.', 'Петров В.Д.', 'Новак А.А.', 'Свириденко Е.В.', 'Кузьменков С.В.',
              'Мартыненков Ю.Ю.', 'Мончиков А.Е.', 'Чернов К.И.', 'Кот Е.Л.', 'Иванюкович И.А.',
              'Мелеховец К.А.', 'Галабурда С.И.']
help_list = ['Команды для Валентиныча:\n1.Взводка - баланс взводной кассы'
             '\n2.Выпускная касса - показывает сколько собрали на выпуск'
             '\n3.Назначить человека - выбирает случайного человека из всего списка взвода'
             '\n4.Список взвода - выводит список взвода\n5.Коронная фраза - ну тут итак все понятно'
             '\n6.Монетка\n7.Карты - карточки для перевода\n8.ДМБ - показывает сколько осталось до выпуска']


def vpskkassa():
    write_message(sender, "Укажите значение")
    global kassa1
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            kassa1 = event.message.get('text')
            write_message(sender, "Выпускная касса: " + kassa1 + "$")
            return 0
def vzvkassa():
    write_message(sender, "Укажите значение")
    global kassa
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            kassa = event.message.get('text')
            write_message(sender, "Взводная касса: " + kassa)
            return 0


def time():
    now = datetime.datetime.now()
    then = datetime.datetime(2022, 6, 25)
    delta = then - now
    write_message(sender, "ВНИМАНИЕ!!! До выпуска осталось:")
    write_message(sender, delta)
    return 0


current_date_time = datetime.datetime.now()
current_time = current_date_time.time()
if current_time == 0:
    time()
else:
    None
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat and event.message.get('text') != "":
        reseived_message = event.message.get('text')
        sender = event.chat_id
        if reseived_message == "Изменить взводную кассу":
            vzvkassa()
        elif reseived_message == "Старт":
            write_message(sender, 'Я бот - Валентиныч, созданный в декабре 2021, могу назначать людей на работы,'
                                  'знаю сколько лежит во взводной и выпскной кассе, и еще кое что другое.Все подреложения по '
                                  'добавлению новых функций можете присылать сюда. Для просмотра доступных фонкций пропишите "Команды"')
        elif reseived_message == "Команды":
            write_message(sender, help_list)
        elif reseived_message == "Взводка":
            write_message(sender, "Взводная касса: " + kassa)
        elif reseived_message == "Изменить выпускную кассу":
            vpskkassa()
        elif reseived_message == "Выпускная касса":
            write_message(sender, "Собрано на выпуск: " + kassa1 + "$")
        elif reseived_message == "Назначить человека":
            write_message(sender, random.choice(vzvod_list))
        elif reseived_message == "Список взвода":
            write_message(sender, spisok_vzvoda)
        elif reseived_message == "Коронная фраза":
            write_message(sender, random.choice(koronka_list))
        elif reseived_message == "Монетка":
            write_message(sender, random.choice(monetka_list))
        elif reseived_message == "ДМБ":
            time()
        elif reseived_message == "Карты":
            write_message(sender,
                          'Карта для выпуска:\n6711 7700 1429 3364\n11/23\n\nКарта для взводной кассы:\n4255 1901 2325 2069\n06/23')
        else:
            None
