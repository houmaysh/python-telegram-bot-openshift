
Skip to content
This repository

    Pull requests
    Issues
    Gist

    @AliYazdani67

2
4

    1

lufte/python-telegram-bot-openshift
Code
Issues 0
Pull requests 0
Projects 0
Wiki
Pulse
Graphs
python-telegram-bot-openshift/bot.py
d8ea31b 29 days ago
@lufte lufte Resolve #1.
63 lines (53 sloc) 1.9 KB
# Copyright (C) 2016 Javier Ayres
#
# This file is part of python-telegram-bot-openshift.
#
# python-telegram-bot-openshift is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# python-telegram-bot-openshift is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-telegram-bot-openshift.  If not, see <http://www.gnu.org/licenses/>.

import logging
from queue import Queue
from threading import Thread
from telegram import Bot
from telegram.ext import Dispatcher, MessageHandler, Updater

TOKEN = '295094626:AAEuQ85OoDlKPHzCzJ0ZyBLxjZG7fKyplUI'


def example_handler(bot, update):
    # Remove this handler
    bot.send_message(
        update.message.chat_id,
        text='Hello from openshift'
    )

# Write your handlers here


def setup(webhook_url=None):
    """If webhook_url is not passed, run with long-polling."""
    logging.basicConfig(level=logging.WARNING)
    if webhook_url:
        bot = Bot(TOKEN)
        update_queue = Queue()
        dp = Dispatcher(bot, update_queue)
    else:
        updater = Updater(TOKEN)
        bot = updater.bot
        dp = updater.dispatcher
    dp.add_handler(MessageHandler([], example_handler))  # Remove this line
    # Add your handlers here
    if webhook_url:
        bot.set_webhook(webhook_url=webhook_url)
        thread = Thread(target=dp.start, name='dispatcher')
        thread.start()
        return update_queue, bot
    else:
        bot.set_webhook()  # Delete webhook
        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    setup()

    Contact GitHub API Training Shop Blog About 

    © 2016 GitHub, Inc. Terms Privacy Security Status Help 

