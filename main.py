import time

from discord.ext import commands
import discord
bot = commands.Bot(command_prefix="$")
bot.reacting = True


@bot.event
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error, commands.errors.CheckFailure):
        embed = discord.Embed(title="We ran into an error", description="You are not staff", color=discord.Color.red())
        embed.set_footer(text="Issued by " + ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title="We ran into an error", description="You forgot to define a message", color=discord.Color.red())
        embed.set_footer(text="Issued by " + ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.errors.BotMissingPermissions):
        embed = discord.Embed(title="We ran into an error", description="I am missing permissions to delete my invoking command", color=discord.Color.red())
        embed.set_footer(text="Issued by " + ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.errors.CommandNotFound):
        try:
            print("Doing nothing since this command doesn't exist")
        except:
            crash = True
    else:
        embed = discord.Embed(title="We ran into an undefined error", description=error, color=discord.Color.red())
        embed.set_footer(text="Issued by " + ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)


@bot.event
async def on_ready():
    print("Bot online")


@bot.event
async def on_message(message):
    print(message.content)
    if message.author == bot.user:
        print("bot message received")
        return
    if message.channel.id == 902020018710143006:  # Channel ID
        if "$react" in message.content:
            if bot.reacting:
                print("reacting turned on")
                bot.reacting = False
                print("message reacted to")
                emojis = ['<:VoteYes:902023599123230730>']
                for emoji in emojis:
                    await message.add_reaction(emoji)
                time.sleep(5)
                await message.delete()

            else:
                print("reacting turned off")
                bot.reacting = True
                print("message reacted to")
                emojis = ['<:VoteNo:902023601056796753>']
                for emoji in emojis:
                    await message.add_reaction(emoji)
                time.sleep(5)
                await message.delete()

bot.run('TOKEN') # nearly fucking left it in
