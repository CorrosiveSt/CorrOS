import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('OTcwODk4MjcyNDg5MTc3MTc4.YnCpeg.rqqYNLWdrZSqGaJxBXI6Xq6aFa4')

// Add git commit
