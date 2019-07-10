import requests
import vk_api
import random
from config import *

vkBot = vk_api.VkApi(token=ACCESS_TOKEN) #'48c97284e8badaca0fea456a422089106f29affcf431c73093bd0c32bbbc875a4109e56bcf5fe609a3811'
vk_user = vk_api.VkApi(token=USER_TOKEN) #'e7b346f1aeb552ba964aa70f25ecebe39bb31fb0d102264c68455d077d389453ddc56b4f8bc1446d7a20e'
USER_ID = 446927861



def write_msg_post(user_id, post):
    vkBot.method('messages.send',
                 {'user_id': user_id,
                  'random_id': random.randint(0, 2147483648),
                  'attachment': post})

def write_msg(user_id, text):
    vkBot.method('messages.send',
                 {'user_id': user_id,
                  'random_id': random.randint(0, 2147483648),
                  'message': text})

lp_server = vkBot.method('messages.getLongPollServer',
                         {'lp_version': 3,
                          'need_pts': 0})
print(lp_server)

ts, key, server = lp_server['ts'], lp_server['key'], lp_server['server']

print("Готов к работе")



while True:
    long_poll = requests.get(
        'https://{server}?act={act}&key={key}&ts={ts}&wait=500'.format(server=server,
                                                                       act='a_check',
                                                                       key=key,
                                                                       ts=ts)).json()
    update = long_poll['updates']
    print(update)
    ts = long_poll['ts']
    domain_1 = ['reallydank', 'dank_memes_ayylmao', 'daily.shit', 'reddit', 'ru9gag']
    domain_2 = ['sciencemems', 'sciencemem', 'sciencememein', 'intellectualmems','math_and_physics', 'typ_math', 'typical_olimp']
    domain_3 = ['4ch', 'canikms', 'dobriememes', 'mudakoff']
    if update[0][0] == 4:
        USER_ID= update[0][3]
    if update[0][0] == 4 and ((update[0][-1].lower() == 'старт') or (update[0][-1].lower() == 'Старт')):
        write_msg(USER_ID,
                  'Привет! Я - мем-бот! Здесь ты найдешь только свежайшие мемасы для всех: для умных и глупых, для шарящих и нешарящих, для олдов и новеньких. Выбирай категорию: \n 1) Зарубежные мемы\n 2) Мемы для умненьких\n 3) Мемы для особенных (постирония, открывать на свой страх и риск)\n')

    if ((update[0][0] == 4) and (update[0][6] == '1')): #first group
        response = vk_user.method('wall.get',
                                  {'domain': random.choice(domain_1),
                                   'offset': random.randint(1, 10),
                                   'count': 1,
                                   'filter': 'owner'})
        post = 'wall{from_id}_{id}'.format(from_id=response['items'][0]['from_id'],
                                           id=response['items'][0]['id'])

        write_msg_post(USER_ID, post)


    if ((update[0][0] == 4) and (update[0][6] == '2')): #second group
        response = vk_user.method('wall.get',
                                  {'domain': random.choice(domain_2),
                                   'offset': random.randint(1, 10),
                                   'count': 1,
                                   'filter': 'owner'})
        post = 'wall{from_id}_{id}'.format(from_id=response['items'][0]['from_id'],
                                           id=response['items'][0]['id'])

        write_msg_post(USER_ID, post)


    if ((update[0][0] == 4) and (update[0][6] == '3')):  # third group
        response = vk_user.method('wall.get',
                                  {'domain': random.choice(domain_3),
                                   'offset': random.randint(1, 10),
                                   'count': 1,
                                   'filter': 'owner'})
        post = 'wall{from_id}_{id}'.format(from_id=response['items'][0]['from_id'],
                                           id=response['items'][0]['id'])

        write_msg_post(USER_ID, post)
