import vk_api
import random
from config import *

vkBot = vk_api.VkApi(token=ACCESS_TOKEN)

USER_ID = 446927861
def write_msg(user_id, text):
    vkBot.method('messages.send',
                       {'user_id' : USER_ID,
                        'random_id' : random.randint(0,2147483648),
                        'message' : text})
write_msg(USER_ID, 'Hey')

lp_server = vkBot.method('messages.getLongPollServer',
                         {'lp_version' : 3,
                         'need_pts' : 0})
print(lp_server)

ts,key,server = lp_server['ts'], lp_server['key'], lp_server['server']

print("Готов к работе")


while True:
    long_poll = requests.get(
        'https://{srver}?act={act}&key={key}&ts={ts}&wait=500'.format(server=server,
                                                                      act='a_check',
                                                                      key=key,
                                                                      ts=ts)).json()
    update = long_poll['updates']

    ts = long_poll['ts']