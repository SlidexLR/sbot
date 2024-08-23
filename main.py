import discord
import colorama
from colorama import Fore, Style
import random
colorama.init(autoreset=True)


client = discord.Client(intents=discord.Intents.all(), self_client=True) 
print(Fore.BLUE + """
      ___                     __             __                                               
 ___/ (_)__ _______  _______/ /___ ____ _ _/_/_ _  ___  ___  ___ __ _____ ____ ____  ___ _   
/ _  / (_-</ __/ _ \/ __/ _  // _ `/ _ `//_//  ' \/ _ \/ _ \/ -_) // / _ `/ _ `/ _ \/ _ `/   
\_,_/_/___/\__/\___/_/  \_,_(_)_, /\_, /_/ /_/_/_/\___/_//_/\__/\_, /\_, /\_,_/_//_/\_, /    
       ___    __         __  /___//___/                        /___//___/          /___/     
  ___ / (_)__/ /____ __ / /___                                                               
 (_-</ / / _  / -_) \ // / __/                                                               
/___/_/_/\_,_/\__/_\_\/_/_/   
      
             """)
# Variables (token)
TOKEN = input("Enter your token: ")

# README (How to use)
# Before running the script, do pip install discord.py and pip install -r requirements.txt in the same order. The requirements txt will be inside the folder.
# Dm slidexlr on a guide how to get your token.
@client.event
async def on_ready():
      print(f'Logged in as {client.user.name}!') 
@client.event
async def on_message(message):
            
    
    if message.content.startswith('!raid'):
        for channel in message.guild.channels:
            try:
                for _ in range (100):
                    await channel.send('# FEIN')
            except:
                pass
    if message.content.startswith('!banall'):
        if message.author.guild_permissions.administrator or message.author.guild_permissions.ban_members:
            for member in message.guild.members:
                try:
                    await member.ban(reason="discord.gg/moneygang - banall")
                except:
                    pass
        else:
            await message.channel.send("You need to have `Administrator` or `Ban Members` permissions to use this command.")
    
    if message.content.startswith('!kickall'):
        if message.author.guild_permissions.administrator or message.author.guild_permissions.kick_members:
            for member in message.guild.members:
                try:
                    await member.kick(reason="discord.gg/moneygang - kickall")
                except:
                    pass
        else:
            await message.channel.send("You need to have `Administrator` or `Kick Members` permissions to use this command.")
    
    if message.content.startswith('!massdm'):
        if message.author.guild_permissions.administrator:
            try:
                args = message.content.split()
                if args[1] == 'server':
                    for member in message.guild.members:
                        try:
                            await member.send(' '.join(args[2:]))
                        except:
                            pass
                elif args[1] == 'friends':
                    for friend in client.user.friends:
                        try:
                            await friend.send(' '.join(args[2:]))
                        except:
                            pass
                else:
                    await message.channel.send("Invalid arguments. Use !massdm server or !massdm friends.")
            except:
                await message.channel.send("Something went wrong, make sure you have the right arguments!")
        
    
    if message.content.startswith('!pack'):
        try:
            user = message.mentions[0]
            insults = ["you're a faggot", "you're a retard", "you're a nigger", "you're a jew", "you're a kike", "you're a pussy", "you're a cuck", "you're a fag", "you're a homo", "you're a queer", "you're a bitch", "you're a piece of shit", "you're a waste of space", "you're a waste of oxygen", "you're a waste of life", "you're a waste of everything", "you're a waste of existence", "you're a waste","your life has no meaning","you have no money","get a life","you're a nolife"]
            for i in range(10):
                random_insult = random.choice(insults)
                await message.channel.send(f"{user.mention} {random_insult}")
        except IndexError:
            await message.channel.send("You need to mention someone to use this command.")
    if message.content.startswith('!help'):
        await message.channel.send("``` by slidexlr (script will be able to be bought in /moneygang soon) \n !banall bans every member \n !kickall kicks every member \n !raidserver <server id> <message> <amount> \n Example: !raidserver 123456789012345678 123456789012345678 10 \n !massdm server <message> sends a dm to everyone in the server \n !massdm friends <message> sends a dm to the user's friends \n !pack <user> sends an insult to the user```")
client.run(TOKEN,bot=False)
