from discord.ext import commands

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print("Bot online")

@bot.event
async def on_message(message):
    print("message received")
    if message.author == bot.user:
        print("bot message received")
        return
    if message.channel.id == 902020018710143006:  # Channel ID
        print("message reacted to")
        emojis = ['<:VoteYes:902023599123230730>', '<:VoteNo:902023601056796753>']
        for emoji in emojis:
            await message.add_reaction(emoji)
bot.run('TOKEN')
