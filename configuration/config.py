from utils.yaml import load


def load_config(cwd):
    config = load(f"{cwd}/config.yml")

    options = (
        "['commands']", "['commands']['crime']", "['commands']['beg']", "['commands']['guess']", "['commands']['fish']",
        "['commands']['hunt']", "['commands']['dig']", "['commands']['search']", "['commands']['stream']",
        "['commands']['highlow']", "['commands']['postmeme']", "['cooldowns']", "['cooldowns']['patron']",
        "['cooldowns']['timeout']")

    for option in options:
        exec(f"_ = config{option}")

    return config
