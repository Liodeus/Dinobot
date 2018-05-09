import discord
from discord.ext.commands import Bot
from discord.ext import commands
from random import randint
import asyncio


bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
	messages = ["Grrrrrr Dinobot arrive sur le serveur !", "Dinobot arrive pour bouffer vos daronnes !"]
	for server in bot.servers:
		lstChannel = list(server.channels)
		lstChannelName = [x.name for x in list(server.channels)]
		try:
			index = lstChannelName.index("general")
			print(f"Join {server}")
			message = messages[randint(0, len(messages) - 1)]
			print(f"{message}\n")
			await bot.send_message(lstChannel[index], message)
		except:
			print(f"Pas de channel \"general\" sur {server}")


@bot.event
async def on_message(message):
	if message.content.upper() == "!DINO":
		await bot.send_message(message.channel, "grrrrrr")
	if message.content.upper().startswith("!TRANSLATE"):
		if len(message.content) > 10:
			print(f"\n{message.author} : {message.content}\n")
			strg = ' '.join(message.content.split(' ')[1:])
			newStrg = ""
			for x in strg:
				print("x= ", x)
				if x != ' ':
					newStrg += chr(randint(65, 122))
				else:
					newStrg += ' '
			await bot.send_message(message.channel, newStrg)
		else:
			error = "Il manque le message Dino !"
			print(f"{error}\n")
			await bot.send_message(message.channel, error)


bot.run("secret")

