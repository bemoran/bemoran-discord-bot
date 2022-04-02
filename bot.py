# bot.py
import os
import random
import time
import discord
from discord.ext import commands
import urllib
import string

#import youtube_dl

# to get member monitoring to work
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents, help_command = None)


# ready message
@client.event
async def on_ready():
    print('Chonki is ready!')

# check ping
# sends current ping in ms as a message
@client.command()
async def ping(ctx):
    await ctx.send(f'pong ({round(client.latency * 1000)}ms)')

# coin
# flips a coin
@client.command(aliases = ['c'])
async def coin(ctx):
    num = random.random()
    if num >= 0.995:
        await ctx.send('Heads :star_struck::open_hands:')
        time.sleep(2)
        await ctx.send(':exploding_head: YOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!! :exploding_head:\nThis roll has consumed all of your luck for the day. Flip again.')

    if num < 0.5:    
        await ctx.send('Heads :star_struck::open_hands:')
    
    if num >= 0.5:
        await ctx.send('Tails :flushed::eggplant:')

    
    
# 8ball
# creates a list from a .txt file with responses then sends a message with the response
@client.command(aliases = ['8ball'])
async def _8ball(ctx):
    with open('8ball.txt', "r") as file:
        responses = file.readlines()
        await ctx.reply(f'{random.choice(responses)}')


# chonk
# creates a list from a .txt file of imgur links then embeds one and sends a message with the link
@client.command(aliases = ['chonki'])
async def chonk(ctx):
    with open('pictures.txt', "r") as file:
        pictures = file.readlines() 
        embedObj = discord.Embed(colour = discord.Colour.random())
        embedObj.set_image(url = random.choice(pictures))
        await ctx.send(embed=embedObj)
    

# based
# bot user id: @823308626642206740
# add one to a number saved in a .txt file then sends a message with that number
@client.command(aliases = ['b'])
async def based(ctx):
    with open('basedcounter.txt', "r+") as file:
        line = file.readlines() # cannot read just the first character. must take the whole string in as a list
        num = int(line[0]) + 1  # typecast string of number to int, add one
        line = str(num)         # typecast incremented number back to string 

        file.truncate(0)        # clear file
        file.seek(0)            # must move cursor back to beginning
        file.write(line)        # write new string

        embedObj = discord.Embed(title = 'Based', description = f'{line} (+1)', colour = discord.Colour.red())
        embedObj.set_image(url = 'https://i.kym-cdn.com/entries/icons/facebook/000/026/799/basedcover.jpg')
        await ctx.send(embed=embedObj)


# bluepilled
# subtracts one from a number saved in a .txt file then sends a message with that number
@client.command(aliases = ['bp'])
async def bluepilled(ctx):
    with open('basedcounter.txt', "r+") as file:
        line = file.readlines() # cannot read just the first character. must take the whole string in as a list
        num = int(line[0]) - 1  # typecast string of number to int, subtract one
        line = str(num)         # typecast decremented number back to string 

        file.truncate(0)        # clear file
        file.seek(0)            # must move cursor back to beginning
        file.write(line)        # write new string

        embedObj = discord.Embed(title = 'Cringe and bluepilled', description = f'{line} (-1)', colour = discord.Colour.blue())
        embedObj.set_image(url = 'https://i1.sndcdn.com/artworks-000590443583-exzk78-t500x500.jpg')
        await ctx.send(embed=embedObj)


# whatdo
# splits given user id's into a list then spits a random one out
@client.command(aliases = ['wd'])
async def whatdo(ctx, *, mentions):
    mention_list = mentions.split(" ")
    if len(mention_list) < 2:
        await ctx.reply('You must list at least **2** things!')
    else:
        await ctx.send(f"<@823308626642206740> picked {random.choice(mention_list)}!")




#pswd
# generate random password and send to user in DM
@client.command(aliases = ['password', 'passwords', 'p'])
async def pswd(ctx, difficulty=None):
    word_website = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = urllib.request.urlopen(word_website) # returns bytes not string
    txt = str(response.read(), 'utf-8') # decode bytes
    WORDS = txt.splitlines()
    word1 = random.choice(WORDS).capitalize()
    word2 = random.choice(WORDS).capitalize()
    num1 = round(random.random() * 100)
    num2 = round(random.random() * 100)
    num3 = round(random.random() * 100)
    special = random.choice(string.punctuation)
    special2 = random.choice(string.punctuation)



    if difficulty == 'easy':
        password = word1 + str(num1)
        await ctx.author.send(f'Your password is:  **{password}**')
        await ctx.send("DM sent.")
    elif difficulty == 'medium':
        password = word1 + str(num1) + str(num2) + special + special2
        await ctx.author.send(f'Your password is:  **{password}**')
        await ctx.send("DM sent.")
    elif difficulty is None or difficulty == 'hard':
        password = special2 + str(num1) + word1 + str(num2) + word2 + str(num3) + special
        await ctx.author.send(f'Your password is:  **{password}**')
        await ctx.send("DM sent.")
    else:
        await ctx.send("Incorrect syntax.")





# clear given text channel with correct permissions and given message amount. default 10
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)



# music

# join channel
# @client.command()
# async def join(ctx):
#     channel = ctx.message.author.voice.channel
#     if not channel:
#         await ctx.send("You are not connected to a voice channel")
#         return
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice and voice.is_connected():
#         await voice.move_to(channel)
#     else:
#         voice = await channel.connect()

# play

# @client.command(pass_context = True)
# async def play(ctx, url):


# # leave channel
# @client.command()
# async def leave(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_connected():
#         await voice.disconnect()
#     else:
#         await ctx.send("Not connect to a channel.")

# # pause
# @client.command()
# async def pause(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_playing():
#         voice.pause()
#     else:
#         ctx.send("There is no audio playing.")


# # resume
# @client.command()
# async def resume(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_paused():
#         voice.resume()
#     else:
#         ctx.send("The audio is not paused.")


# # stop
# @client.command()
# async def stop(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     voice.stop()






# help
# custom help command
@client.command()
async def help(ctx):
    await ctx.reply('\
:small_blue_diamond: **.ping** - displays ping to bot\n\
:small_blue_diamond: **.coin** - flips heads or tails\n\
:small_blue_diamond: **.8ball <question>** - ask a question\n\
:small_blue_diamond: **.chonk** - see random chonki\n\
:small_blue_diamond: **.based, .b** - add one to based and pog pilled counter\n\
:small_blue_diamond: **.bluepilled, .bp** - subtract one from based and pog pilled counter\n\
:small_blue_diamond: **.whatdo <option1> <option2> ...** - pick something to do - must be one word per option\n\
:small_blue_diamond: **.pswd** - password generator\n')






# error handling

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply('Command not found! Please see **.help** or check your syntax')

@whatdo.error
async def whatdo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('You must **@** at least **2** people!')

@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('You must ask a question!')







