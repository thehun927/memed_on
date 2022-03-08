# main.py

import sys
from time import sleep
from discord import send_message
from os.path import dirname
from configuration.config import load_config
from configuration.credentials import load_credentials
from utils.shared import data
from memes.search import search_master

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
    sleep(3)
    send_message(channel_id, token, config, username, "p dig")
    sleep(3)
    send_message(channel_id, token, config, username, "p fish")
    sleep(3)
    send_message(channel_id, token, config, username, "p hunt")
    sleep(3)
    search_master(username, channel_id, token, config, user_id, session_id)

