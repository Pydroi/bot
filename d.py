import discord
import random
from pyautogui import *
import pyautogui
import time



TOKEN =""

client = discord.Client()




@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = message.content
  
    channel =str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")
    
    
    if message.author == client.user:
        return
    
        
    #await message.channel.send(user_message)
    
    
    if message.content == 'ping':
            await message.channel.send('pong')
    
    
    
    if message.content.lower()=='hello':
        await message.channel.send(f"hello  {username}")
        return

    elif user_message.lower() == "bye":
        await message.channel.send(f"see you later {username}!")
        return
    
    elif user_message.lower() =="random":
        response =f"This is your random number: {random.randrange(1000000)}"
        await message.channel.send(response)
        return
    if user_message.lower() =="anywhere":
        await message.channel.send("This can be used anywhere!")
        return 

    if user_message.lower() =="spam":
        for i in range(1,(10)):
                await message.channel.send("hii")
    
    if (user_message.lower()=="kick") :
        print(message.channel.name)
         #   await message.slayer_ts.send("it works")







client.run(TOKEN)
