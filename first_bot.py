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