""" Links to GIFs that the bot will choose from depending on it's intended response"""
import random

hello = [
    "https://c.tenor.com/pvFJwncehzIAAAAM/hello-there-private-from-penguins-of-madagascar.gif",
    "https://c.tenor.com/FABadXdQ65MAAAAC/hi-hello.gif",
    "https://media.giphy.com/media/3o7TKNAKmaV3z0mNkQ/giphy.gif",
    "https://media.giphy.com/media/OnnUZxcHsbBN6/giphy.gif",
    "https://media.giphy.com/media/CVNWEzubQAfIivcVEF/giphy.gif",
    "https://media.giphy.com/media/14aa5GbbHT3bHO/giphy.gif",
    "https://media.giphy.com/media/xUyrMCdgrOL3ntbTvK/giphy.gif",
    "https://cdn.substack.com/image/fetch/f_auto,q_auto:good,"
    "fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984"
    ".s3.amazonaws.com%2Fpublic%2Fimages%2F95627f4a-7c0a-4a97-b760-40ffd4d02e23_480x273.gif",
    "https://c.tenor.com/Km9AwoEjCpgAAAAC/jisoo-hello.gif",
    "https://giphy.com/gifs/80s-retro-1980s-TAqYM2x2WHoT6",
    "https://c.tenor.com/6us3et_6HDoAAAAM/hello-there-hi-there.gif",
    "https://c.tenor.com/UNTqMDwqh1gAAAAM/hello-hi.gif",
]
money = [
    "https://media.giphy.com/media/3orif7DCmoW6zG6HUQ/giphy.gif",
    "https://c.tenor.com/vpva0KfiifsAAAAC/rich-money.gif",
    "https://media.giphy.com/media/50hzYZ3IETMrK/giphy.gif",
    "https://www.gifcen.com/wp-content/uploads/2021/05/money-gif-9.gif",
]
no_money = [
    "https://media.giphy.com/media/yIxNOXEMpqkqA/giphy.gif",
    "https://c.tenor.com/o6_Suc3YJq4AAAAM/no-money-please.gif",
    "https://c.tenor.com/rdvWdzGheQYAAAAM/drama-queen-wallet.gif",
    "https://giphy.com/gifs/season-12-the-simpsons-12x4-3orifdO6eKr9YBdOBq",
]
applause = ["https://c.tenor.com/ZWopsXeO7tQAAAAd/clapping-applause.gif"]
sacrifice = [
    "https://c.tenor.com/M5QmujL5_YQAAAAC/good-evil.gif",
    "https://media.giphy.com/media/sR91D133W02D6/giphy.gif",
    "https://media.giphy.com/media/RG4IXFG1YmLOU/giphy.gif",
    "https://media.giphy.com/media/8wzDNe9unxCuY/giphy.gif",
    "https://media.giphy.com/media/Qaoh3qmKzOFVK/giphy.gif",
]


def get_hello():
    """Choose a random gif from the 'hello' list"""
    return random.choice(hello)


def get_money():
    """Choose a random gif from the 'money' list"""
    return random.choice(money)


def get_no_money():
    """Choose a random gif from the 'no_money' list"""
    return random.choice(no_money)


def get_sacrifice():
    """Choose a random gif from the 'sacrifice' list"""
    return random.choice(sacrifice)


def get_applause():
    """Choose a random gif from the 'applause' list"""
    return random.choice(applause)
