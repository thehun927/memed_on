from discord import send_message, retrieve_message, interact_button
from random import choice
from time import time, sleep
from utils.shared import data


def postmeme(username, channel_id, token, config, user_id, session_id):

    try:
        sleep(2)
        send_message(channel_id, token, config, username, "p postmeme")
        latest_message = retrieve_message(channel_id, token, config, username, "p postmeme", user_id)
        sleep(1)

        if latest_message is None:
            return

        interact_button(channel_id, token, config, username, "p postmeme",
                        choice(latest_message["components"][0]["components"])["custom_id"], latest_message, session_id)

    except IndexError:
        print("index error - sleeping for 45 sec & passing")
        sleep(45)
        return


def postmeme_master(username, channel_id, token, config, user_id, session_id):
    while True:
        while not data[channel_id]:
            pass

        data[channel_id] = False
        start = time()
        postmeme(username, channel_id, token, config, user_id, session_id)
        end = time()
        data[channel_id] = True

        if config["cooldowns"]["patron"]:
            cooldown = 20 - (end - start)
        else:
            cooldown = 45 - (end - start)

        if cooldown > 0:
            sleep(cooldown)
