import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from project import*
from random import randint
from rfr import get_wiki_article


token = "vk1.a.bj7fnz9Ffh36_kB8qsae929jN5ZvpG3Yhyg-i1IAmWumWnNQjjKFZnIr-6V_Ez_Nve8LCQ-KOJtdgJR6i31WwV7QDuPRsRi-Io16Qwv9CXRV8y8IeASmmjtXC2RiB4GCu6xgQ5qdgsY2aIpVNEXvLE3TYXWL0U5puKeTF9zhyLWy5z6WcucNkkPG_UgtaOe46HUvBRkJqAmJiK0_HqzyPg"

vk_session_connection = vk_api.VkApi(token=token)
vk = vk_session_connection.get_api()
longpoll = VkLongPoll(vk_session_connection)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text
        user_id = event.user_id
        rand_id = randint(1, 10 ** 10)
        if '-k ДОЛЛАР' == text:
            res = f'1$ = {get_course(id2)} RUB'
        elif '-k ЕВРО' == text:
            res = f'1 EUR = {get_course(id1)} RUB'
        elif '-k ЮАНЬ' == text:
            res = f'1 CNY = {get_course(id3)} RUB'
        elif '-k ФУНТ' == text:
            res = f'1 GBP = {get_course(id4)} RUB'
        elif '-в' == text[:2]:
            res = get_wiki_article(text[3:])
        else:
            res = text
        vk.messages.send(user_id=user_id, random_id=rand_id, message=res)