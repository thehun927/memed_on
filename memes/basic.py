from discord import send_message
from time import time, sleep
from utils.shared import data


def beg(username, channel_id, token, config):
    send_message(channel_id, token, config, username, "p beg")


def dig(username, channel_id, token, config):
    send_message(channel_id, token, config, username, "p dig")


def fish(username, channel_id, token, config):
    send_message(channel_id, token, config, username, "p fish")


def hunt(username, channel_id, token, config):
    send_message(channel_id, token, config, username, "p hunt")


def beg_master(username, channel_id, token, config):
    sleep(45)

    while True:
        while not data[channel_id]:
            pass

        data[channel_id] = False
        start = time()
        beg(username, channel_id, token, config)
        end = time()
        data[channel_id] = True

        if config["cooldowns"]["patron"]:
            cooldown = 15 - (end - start)
        else:
            cooldown = 45 - (end - start)

        if cooldown > 0:
            sleep(cooldown)


def dig_master(username, channel_id, token, config):
    sleep(45)

    while True:
        while not data[channel_id]:
            pass

        data[channel_id] = False
        start = time()
        dig(username, channel_id, token, config)
        end = time()
        data[channel_id] = True

        if config["cooldowns"]["patron"]:
            cooldown = 15 - (end - start)
        else:
            cooldown = 45 - (end - start)

        if cooldown > 0:
            sleep(cooldown)


def fish_master(username, channel_id, token, config):
    sleep(45)

    while True:
        while not data[channel_id]:
            pass

        data[channel_id] = False
        start = time()
        fish(username, channel_id, token, config)
        end = time()
        data[channel_id] = True

        if config["cooldowns"]["patron"]:
            cooldown = 15 - (end - start)
        else:
            cooldown = 45 - (end - start)

        if cooldown > 0:
            sleep(cooldown)


def hunt_master(username, channel_id, token, config):
    sleep(45)

    while True:
        while not data[channel_id]:
            pass

        data[channel_id] = False
        start = time()
        hunt(username, channel_id, token, config)
        end = time()
        data[channel_id] = True

        if config["cooldowns"]["patron"]:
            cooldown = 15 - (end - start)
        else:
            cooldown = 45 - (end - start)

        if cooldown > 0:
            sleep(cooldown)
