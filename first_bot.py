import requests
import response as response
import vk_api
import random
from config import *

vkBot = vk_api.VkApi(token=ACCESS_TOKEN) #'48c97284e8badaca0fea456a422089106f29affcf431c73093bd0c32bbbc875a4109e56bcf5fe609a3811'
vk_user = vk_api.VkApi(token=USER_TOKEN)
USER_ID = 446927861



def write_msg_post(user_id, text, post):
    vkBot.method('messages.send',
                 {'user_id': USER_ID,
                  'random_id': random.randint(0, 2147483648),
                  'message': text,
                  'attachment': post})

def write_msg(user_id, text):
    vkBot.method('messages.send',
                 {'user_id': USER_ID,
                  'random_id': random.randint(0, 2147483648),
                  'message': text})


write_msg(USER_ID, 'Hey')

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


    if (update[0][0] == 4):
        response = vk_user.method('wall.get',
                                  {'domain': 'proglib',
                                   'offset': 1,
                                   'count': 1,
                                   'filter': 'owner'})
        post = 'wall{from_id}_{id}'.format(from_id=response['items'][0]['from_id'],
                                           id=response['items'][0]['id'])

        print(response)
        write_msg_post(USER_ID, response, post)