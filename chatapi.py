from dotenv import load_dotenv
import discord
import os
from openapi import chatgpt_response
load_dotenv()

discord_token=os.getenv('TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Succesfully logged in as: ',self.user)

    async def on_message(self,message):
        print(message.content)
        if message.author==self.user:
            return
        command,user_message=None,None

        for text in ['/ai','/bot','/chatgpt']:
            if message.content.startswith(text):
                command=message.content.split(' ')[0]
                user_message=message.content.replace(text,'')
                print(command,user_message)
        
        if command == '/ai' or command =='/bot' or command =='/chatgpt':
            default=["create a hypothetical creative scene with the following: "]
            default.append(user_message.strip())
            bot_response=chatgpt_response(prompt=','.join(filter(None,default)))
            bot_response2=chatgpt_response(prompt=f"Summarize the following text to a maximum of 30 words. Remove punctuations wherever possible.Focus on keeping keywords so that the essence of the text is maintained: {bot_response}")
            await message.channel.send(f"Answer: {bot_response2}")


intents=discord.Intents.default()
intents.message_content=True

client=MyClient(intents=intents)