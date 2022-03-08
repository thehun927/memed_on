# discord.py

from time import sleep
from datetime import datetime
from websocket import WebSocket
from json import loads, dumps
from requests import post, get
from utils import shared


def gateway(token):
    ws = WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=10&encoding=json")
    loads(ws.recv())

    ws.send(dumps({
        "op": 2,
        "d": {
            "token": token,
            "properties": {
                "$os": "windows",
                "$browser": "chrome",
                "$device": "pc"
            }
        }
    }))

    return loads(ws.recv())["d"]["sessions"][0]["session_id"]


def send_message(channel_id, token, config, username, command):
    while True:
        request = post(f"https://discord.com/api/v10/channels/{channel_id}/messages", headers={"authorization": token},
                       json={"content": command})
        if request.status_code == 200 or request.status_code == 204:
            return True
        else:
            if request.status_code == 429:
                request = loads(request.content)
                sleep(request["retry_after"])
                continue
            return False


def retrieve_message(channel_id, token, config, username, command, user_id, session_id=None):
    time = datetime.strptime(datetime.now().strftime("%x-%X"), "%x-%X")

    while (datetime.strptime(datetime.now().strftime("%x-%X"), "%x-%X") - time).total_seconds() < config["cooldowns"][
        "timeout"]:
        request = get(f"https://discord.com/api/v10/channels/{channel_id}/messages", headers={"authorization": token})

        if request.status_code != 200:
            continue

        latest_message = loads(request.text)[0]

        if latest_message["author"]["id"] == "270904126974590976":
            if "referenced_message" in latest_message.keys():
                if latest_message["referenced_message"]["author"]["id"] == user_id:
                    break
            else:
                break
        else:
            continue

    if latest_message["author"]["id"] != "270904126974590976":
        return None

    return latest_message


def interact_button(channel_id, token, config, username, command, custom_id, latest_message, session_id):
    data = {
        "application_id": 270904126974590976,
        "channel_id": channel_id,
        "type": 3,
        "data": {
            "component_type": 2,
            "custom_id": custom_id
        },
        "guild_id": latest_message["message_reference"]["guild_id"] if "message_reference" in latest_message.keys() else
        shared.data[f"{channel_id}_guild"],
        "message_flags": 0,
        "message_id": latest_message["id"],
        "session_id": session_id
    }

    request = post(f"https://discord.com/api/v10/interactions", headers={"authorization": token}, json=data)

    if request.status_code == 200 or request.status_code == 204:
        return True
    else:
        return False