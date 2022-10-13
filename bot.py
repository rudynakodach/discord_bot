import praw
from praw import Reddit
import discord
from discord import *
import asyncio
import random
import os
import time
import datetime
import json
from colorama import Fore
import colorama

colorama.init(autoreset=True)

os.system("cls")

print(f"{Fore.RED}IMPORTANT!{Fore.WHITE} If you haven't already, set the reddit client ID and secret with your own application as you can, and will encounter errors! Go to 'https://www.reddit.com/prefs/apps' to create your app.")
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="discordBOT",
    check_for_async=False
)

#you can add your own subs if you want I dont care lol
meme_subs = ["bossfight","memes","dankmemes","shitposting","rareinsults","cursedcomments","blursedimages"]

TOKEN = "ENTER YOUR KEY HERE"

if(TOKEN == "ENTER YOUR KEY HERE"):
    print(f"{Fore.YELLOW}[Warning] Edit the 31th line of code to 'TOKEN = '<your api key>''! You can get your token from 'General Information' tab.")
    os.system("pause")
    quit()

bot = discord.Client()

print(f"Startup: {datetime.datetime.now()}")

@bot.event
async def on_ready():
    print(f"Ready.")
    print(f"Currently in {bot.guilds}")
    print(f"{len(bot.guilds)} servers.")
    servNum = len(bot.guilds)
    servNum = int(servNum)
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{servNum} servers"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == ("-meme"):
        if message.author != bot.user:
            print(f"{message.author} used -meme")
            selected_sub = random.choice(meme_subs)
            meme = reddit.subreddit(selected_sub).random()
            await message.channel.send(f"**Title: **{meme.title}\n**Author: ** {meme.author}\n**Subreddit: **r/{selected_sub}\n{meme.url}")
            await message.channel.send(f"**Comments: **")
            for top_level_comment in meme.comments[:5]:
                    await message.channel.send(f"> {top_level_comment.body}")


    if message.content == ("-info"):
        await message.channel.send("**Bot by:** <@795241041753014272>\n**Bot version:** 1.0\n**Bot created:** 12-06-2022\n**Bot updated:** 14-06-2022")
        await asyncio.sleep(2)

    if message.content == ("-help"):
        await message.channel.send("**-meme** - Picks a random meme from Reddit\n**-reddit [subreddit]** - Picks a random post from the provided subreddit\n**-info** - Displays bot information\n**-help** - Displays this message")
        await asyncio.sleep(3)
    if message.content == ("-ping"):
        #get the latency of the bot and send it in a message
        latency = bot.latency
        await message.channel.send(f"Running on **{latency*1000}ms**")
        await asyncio.sleep(2)
        

    if message.content == ("-random"):
        #generate a random number between 1 and 100
        random_number = random.randrange(1, 100)
        await message.channel.send(f"**Your number:** {random_number}")
    elif message.content.startswith("-random"):
        print(f"{message.author} used -random")
        #make the users messge a string and make it into 3 parts
        message_string = str(message.content)
        message_string = message_string.split(" ")
        #get the number of words in the message
        message_length = len(message_string)
        print(len(message_string))
        #if the number of words is 3, get the second and third word and check if its a number
        if message_length == 3:
            try:
                number1 = int(message_string[1])
                number2 = int(message_string[2])
                #if number 1 is smalled than number 2, generate a random number between them
                if number1 < number2:
                    random_number = random.randrange(number1, number2)
                    await message.channel.send(f"**Your number:** {random_number}")
                    await asyncio.sleep(2)
            except:
                await message.channel.send(f"**KeyError**\n**Enter corrent numbers**")
                await asyncio.sleep(2)




    if message.content.startswith("-reddit"):
        if message.author != bot.user:
            try:
                subreddit = message.content[8::]
                print(subreddit)
                meme = reddit.subreddit(subreddit).random()
                await message.channel.send(f"**Title: **{meme.title}\n**Author: ** u/{meme.author}\n**Subreddit: **r/{subreddit}\n{meme.url}")
            except:
                await message.channel.send("This subreddit doesnt exist!")
            await asyncio.sleep(5)

#uncomment when 
#nvm 
    """
    if message.content == ('-invite'):
        await message.channel.send(f"**You can invite this bot by using this link!**\nhttps://discord.com/api/oauth2/authorize?client_id=985155516747636766&permissions=8&scope=bot")
        await asyncio.sleep(5)
    """
    
#uncomment when functional
"""
    if message.content.startswith("-timeout"):
        if message.author != bot.user:
            if message.author.guild_permissions.administrator:
                print(f"{message.author} used -timeout | perms")
                message_string = str(message.content)
                message_string = message_string.split(" ")
                message_length = len(message_string)
            else:
                print(f"{message.author} tried to use -timeout | no perms")
                await message.channel.send("Nie masz uprawnień do wykonania tej komendy")
                await asyncio.sleep(2)

            if message_length == 3:
                if message_string[1].startswith("<@"):
                    user = message_string[1]
                
                if message_string[1].isdigit():
                    user_id = message_string[1]
                    user = message.guild.get_member(user_id)
                else:
                    await message.channel.send(f"**KeyError**\n**Wpisz poprawne ID**")

                print(f"{message.content}\n{message_string}\n{message_string[1]}\n{message_string[2]}")

                try:
                    number = int(message_string[2])
                    print(f"{user.author} | timeout | number converted into an int")
                    if number < 1:
                        print(f"{message.author} tried to use -timeout with a number less than 1")
                        await message.channel.send("**Nie możesz wywołać timeouta krótszego niż 1 minuta!**")
                        await asyncio.sleep(2)
                    else:
                        await user.edit(mute=True, reason=f"Timeout na {number} minut")
                        await asyncio.sleep(2)
                        await message.channel.send(f"**{user.name}** został timeoutowany na **{number}** minut")
                        await asyncio.sleep(2)
                except:
                    await message.channel.send(f"**Niepoprawne użycie komendy!**\n*-timeout <user> <minuty>*")
                    await asyncio.sleep(2)
                




#    if message.content == ("-acc22135"):
#        print(f"{message.author} | -acc")
#        os.system("cls")
#        await message.delete()
#        #print all the avaible text channels from all servers
#        for guild in bot.guilds:
#            for channel in guild.text_channels:
#                print(f"{channel.name} | {channel.id} | {channel.guild.name} | {channel.guild.id}")
#        commandType = input("Action: ")
#        if commandType == "message":
#            channel = input("Channel: ")
#            message = input("Message: ")
#            await bot.get_channel(channel).send(message)
#        #if commandType = "kick" then kick the user from server id from input
#        elif commandType == "kick":
#            server = input("Server: ")
#            user = input("User: ")
#            await bot.guild(server).kick(user)
#        elif commandType == "ban":
#            user = input("User: ")
#            await bot.get_user(user).ban()
#        elif commandType == "unban":
#            user = input("User: ")
#            await bot.get_user(user).unban()
#        elif commandType == "createRole":
#            #create a role with a name from input with admin permissions
#            roleName = input("Role name: ")
#            server = input("Server: ")
#            await bot.guild(server).create_role(name=roleName, permissions=discord.Permissions.all())
#        elif commandType == "createChannel":
#            #create a channel in a server from input with a name from input
#            server = input("Server: ")
#            channelName = input("Channel name: ")
#            await bot.get_server(server).create_text_channel(channelName)

    if message.content == ("-cfg ~welcomeChannel --set-ID"):
        await message.channel.send(f"**Wpisz ID kanału tekstowego**")
        #wait for message author to send a message and define it as "msg"
        msg = await bot.wait_for('message', check=lambda message: message.author == message.author)
        if msg.content == ("cancel"):
            await message.channel.send("**Anulowano**")
            return
        else:
            with open("cfg.txt", "w") as file:
                file.write(f"{bot.guild} {msg.content}")
            await message.channel.send("**Zapisano**")
            asyncio.sleep(3)
#make a welcome message in a text channel
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(986294405545721866)
    await channel.send(f"{member.mention} Witamy na serwerze!")
    await asyncio.sleep(1)

"""
bot.run(TOKEN)