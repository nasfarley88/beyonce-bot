"""

A bot that will (eventually) provide appropriate Beyonce quotes for every
occasion!

"""

import random

# TODO replace with api call or equiv
QUOTES = [
    "If you like it then you should've put a ring on it.",
    "I'm a grown woman.",
]

def send_random_quote(bot, msg):
    bot.sender.sendMessage(random.choice(QUOTES))


# Custom magic for plugin
__commands__ = {
    "/beyonce": send_random_quote
}
