from discord import send_message, retrieve_message, interact_button
from time import time, sleep
from utils.shared import data


def highlow(username, channel_id, token, config, user_id, session_id):
    sleep(1)
    send_message(channel_id, token, config, username, "p highlow")
    latest_message = retrieve_message(channel_id, token, config, username, "p highlow", user_id, session_id)
    sleep(1)

    if latest_message is None:
        return

    number = int(latest_message["embeds"][0]["description"].split("**")[-2])
    interact_button(channel_id, token, config, username, "p highlow",
                    latest_message["components"][0]["components"][0]["custom_id"] if number > 50 else
                    latest_message["components"][0]["components"][2]["custom_id"] if number < 50 else
                    latest_message["components"][0]["components"][1]["custom_id"], latest_message, session_id)


def highlow_master(username, channel_id, token, config, user_id, session_id):
    while True:
        while not data[channel_id]:
            pass

        data[channel_id] = False
        start = time()
        highlow(username, channel_id, token, config, user_id, session_id)
        end = time()
        data[channel_id] = True

        if config["cooldowns"]["patron"]:
            cooldown = 15 - (end - start)
        else:
            cooldown = 45 - (end - start)

        if cooldown > 0:
            sleep(cooldown)
