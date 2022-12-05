import requests

def find_user_info(user_id, vk_token):
    user_info = f"https://api.vk.com/method/users.get?user_id={user_id}&fields=first_name,sex,online,last_seen,has_mobile,education&v=5.92&access_token={vk_token}"
    user_info_json = requests.get(user_info).json()
    return user_info_json


def extract_dict_from_json(json_response):
    dict_from_json  = list()
    for x in json_response['response']:
        dict_from_json.append(x)

    return dict_from_json[0]


def is_user_online(json_dic):
    name = json_dic['first_name'] + ' ' + json_dic['last_name']
    if json_dic['online'] == 1:
        print(f'{name} is online in this moment!')
    else:
        print(f'{name} is offline in this moment!')