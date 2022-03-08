from json import load, loads
from requests import get
from discord import gateway


def load_credentials(cwd):
    credentials = load(open(f"{cwd}/credentials.json", "r"))
    data = []

    for index in range(len(credentials["tokens"])):
        request = get("https://discord.com/api/v10/users/@me", headers={"authorization": credentials["tokens"][index]})

        request = loads(request.text)

        data.append(
            [request["id"], f"{request['username']}#{request['discriminator']}", gateway(credentials["tokens"][index]),
             credentials["channel_ids"][index], credentials["tokens"][index]])

    print("")

    return data
