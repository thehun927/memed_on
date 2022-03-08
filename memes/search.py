from discord import send_message, retrieve_message, interact_button
from random import choice
from time import time, sleep
from utils.shared import data


def search(username, channel_id, token, config, user_id, session_id):
	send_message(channel_id, token, config, username, "p deposit all")
	sleep(3)
	send_message(channel_id, token, config, username, "p search")
	latest_message = retrieve_message(channel_id, token, config, username, "p search", user_id)

	if latest_message is None:
		return
	
	interact_button(channel_id, token, config, username, "p search", choice(latest_message["components"][0]["components"])["custom_id"], latest_message, session_id)


def search_master(username, channel_id, token, config, user_id, session_id):
	while True:
		while not data[channel_id]:
			pass

		data[channel_id] = False
		start = time()
		search(username, channel_id, token, config, user_id, session_id)
		end = time()
		data[channel_id] = True
		
		if config["cooldowns"]["patron"]:
			cooldown = 15 - (end - start)
		else:
			cooldown = 45 - (end - start)

		if cooldown > 0:
			sleep(cooldown)