import discord
import asyncio
import time

class TheaterBot(discord.Client):

    def __init__(self):
        super(TheaterBot, self).__init__()
        self._id = ""
        self._channel = None

    @asyncio.coroutine
    def on_ready(self):
        print('Logged in as:')
        print(self.user.name)
        print(self.user.id)


    @asyncio.coroutine
    def on_message(self, message):
        if self.user.mentioned_in(message): #checks to see if bot was mentioned in message
            if message.content.split()[1] == "init": #checks to see if the content of the message's first word is 'init'
                yield from self.send_message(message.channel, "Initialized")
                self._channel = message.channel
                self._id = message.content.split(' ')[2]
        elif message.content.startswith("!1235"):
            if message.content.split()[1] == self._id:
                yield from self.send_typing(self._channel)
                msg = message.content.split(maxsplit = 2)
                time.sleep(1)
                try:
                    yield from self.send_message(self._channel, msg[2])
                except Exception as e:
                    print("couldn't send message, no channel Initialized")
                yield from self.add_reaction(message, '👍')
