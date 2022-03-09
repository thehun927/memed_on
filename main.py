# main.py

import sys
import os
from threading import Thread
from discord import send_message, retrieve_message
from os.path import dirname
from configuration.config import load_config
from configuration.credentials import load_credentials
from utils.shared import data
from memes.search import search_master
from memes.crime import crime_master
from memes.postmeme import postmeme_master
from memes.basic import beg_master, dig_master, fish_master, hunt_master
from games.highlow import highlow_master
from games.guess import guess_master

print(f"""

███╗   ███╗███████╗███╗   ███╗███████╗██████╗          ██████╗ ███╗   ██╗
████╗ ████║██╔════╝████╗ ████║██╔════╝██╔══██╗        ██╔═══██╗████╗  ██║
██╔████╔██║█████╗  ██╔████╔██║█████╗  ██║  ██║        ██║   ██║██╔██╗ ██║
██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██╔══╝  ██║  ██║        ██║   ██║██║╚██╗██║
██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║███████╗██████╔╝███████╗╚██████╔╝██║ ╚████║
╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝

""")

if getattr(sys, "frozen", False):
    cwd = dirname(sys.executable)
elif __file__:
    cwd = dirname(__file__)

config = load_config(cwd)
credentials = load_credentials(cwd)

for index in range(len(credentials)):
    user_id = credentials[index][0]
    username = credentials[index][1]
    session_id = credentials[index][2]
    channel_id = credentials[index][3]
    token = credentials[index][4]
    data[channel_id] = True

    send_message(channel_id, token, config, username, "p beg")
    print("we're in")

    while True:
        latest_message = retrieve_message(channel_id, token, config, username, "p beg", user_id, session_id)

        if latest_message is not None:
            break

    if config["commands"]["beg"]:
        Thread(target=beg_master, args=(username, channel_id, token, config)).start()

    if config["commands"]["crime"]:
        Thread(target=crime_master, args=(username, channel_id, token, config, user_id, session_id)).start()

    if config["commands"]["dig"]:
        Thread(target=dig_master, args=(username, channel_id, token, config)).start()

    if config["commands"]["fish"]:
        Thread(target=fish_master, args=(username, channel_id, token, config)).start()

    if config["commands"]["hunt"]:
        Thread(target=hunt_master, args=(username, channel_id, token, config)).start()

    if config["commands"]["search"]:
        Thread(target=search_master, args=(username, channel_id, token, config, user_id, session_id)).start()

    if config["commands"]["postmeme"]:
        Thread(target=postmeme_master, args=(username, channel_id, token, config, user_id, session_id)).start()

    if config["commands"]["highlow"]:
        Thread(target=highlow_master, args=(username, channel_id, token, config, user_id, session_id)).start()

    if config["commands"]["guess"]:
        Thread(target=guess_master, args=(username, channel_id, token, config, user_id, session_id)).start()




