from discord import send_message, retrieve_message
from random import randint
from time import time, sleep
from utils.shared import data


def guess(username, channel_id, token, config, user_id, session_id):
    send_message(channel_id, token, config, username, "p guess")

    latest_message = retrieve_message(channel_id, token, config, username, "p guess", user_id, session_id)

    if latest_message is None:
        return

    send_message(channel_id, token, config, username, "10")

    latest_message = retrieve_message(channel_id, token, config, username, "10", user_id, session_id)

    if latest_message is None:
        return

    if latest_message["content"] == "not this time, `3` attempts left and `2` hints left.":
        send_message(channel_id, token, config, username, "hint")

        latest_message = retrieve_message(channel_id, token, config, username, "hint", user_id, session_id)

        if latest_message is None:
            return

        if latest_message[
            "content"] == "Your last number (**10**) was too low\nYou've got `3` attempts left and `1` hint left.":
            send_message(channel_id, token, config, username, "15")

            latest_message = retrieve_message(channel_id, token, config, username, "15", user_id, session_id)

            if latest_message is None:
                return

            if latest_message["content"] == "not this time, `2` attempts left and `1` hint left.":
                send_message(channel_id, token, config, username, "hint")

                latest_message = retrieve_message(channel_id, token, config, username, "hint", user_id, session_id)

                if latest_message is None:
                    return

                if latest_message[
                    "content"] == "Your last number (**15**) was too low\nYou've got `2` attempts left and `0` hints left.":
                    num = randint(16, 20)

                    send_message(channel_id, token, config, username, num)

                    latest_message = retrieve_message(channel_id, token, config, username, num, user_id, session_id)

                    if latest_message is None:
                        return

                    if latest_message["content"] == "not this time, `1` attempt left and `0` hints left.":
                        num = randint(16, 20)

                        send_message(channel_id, token, config, username, num)

                        return
                elif latest_message[
                    "content"] == "Your last number (**15**) was too high\nYou've got `2` attempts left and `0` hints left.":
                    num = randint(11, 14)

                    send_message(channel_id, token, config, username, num)

                    latest_message = retrieve_message(channel_id, token, config, username, num, user_id, session_id)

                    if latest_message is None:
                        return

                    if latest_message["content"] == "not this time, `1` attempt left and `0` hints left.":
                        num = randint(11, 14)

                        send_message(channel_id, token, config, username, num)

                        return


        elif latest_message[
            "content"] == "Your last number (**10**) was too high\nYou've got `3` attempts left and `1` hint left.":
            send_message(channel_id, token, config, username, "5")

            latest_message = retrieve_message(channel_id, token, config, username, "5", user_id, session_id)

            if latest_message is None:
                return

            if latest_message["content"] == "not this time, `2` attempts left and `1` hint left.":
                send_message(channel_id, token, config, username, "hint")

                latest_message = retrieve_message(channel_id, token, config, username, "hint", user_id, session_id)

                if latest_message is None:
                    return

                if latest_message[
                    "content"] == "Your last number (**5**) was too low\nYou've got `2` attempts left and `0` hints left.":
                    num = randint(6, 9)

                    send_message(channel_id, token, config, username, num)

                    latest_message = retrieve_message(channel_id, token, config, username, num, user_id, session_id)

                    if latest_message is None:
                        return

                    if latest_message["content"] == "not this time, `1` attempt left and `0` hints left.":
                        num = randint(6, 9)

                        send_message(channel_id, token, config, username, num)

                        return
                elif latest_message[
                    "content"] == "Your last number (**5**) was too high\nYou've got `2` attempts left and `0` hints left.":
                    num = randint(1, 4)

                    send_message(channel_id, token, config, username, num)

                    latest_message = retrieve_message(channel_id, token, config, username, num, user_id, session_id)

                    if latest_message is None:
                        return

                    if latest_message["content"] == "not this time, `1` attempt left and `0` hints left.":
                        num = randint(1, 4)

                        send_message(channel_id, token, config, username, num)

                        return


def guess_master(username, channel_id, token, config, user_id, session_id):
    while True:
        while not data[channel_id]:
            pass

        data[channel_id] = False
        start = time()
        guess(username, channel_id, token, config, user_id, session_id)
        end = time()
        data[channel_id] = True
        cooldown = 30 - (end - start)

        if cooldown > 0:
            sleep(cooldown)
