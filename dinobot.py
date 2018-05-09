import discord
from discord.ext.commands import Bot
from discord.ext import commands
from random import randint
from time import sleep
import asyncio


bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
	print("co")
	messages = ["Grrrrrr Dinobot arrive sur le serveur !", "Dinobot arrive pour bouffer vos daronnes !", "Dinobot ici pour casser du CDAISI !"]
#	for server in bot.servers:
#		lstChannel = list(server.channels)
#		lstChannelName = [x.name for x in list(server.channels)]
#		try:
#			index = lstChannelName.index("general")
#			print(f"Join {server}")
#			message = messages[randint(0, len(messages) - 1)]
#			print(f"{message}")
#			await bot.send_message(lstChannel[index], message)
#		except:
#			print(dinosay("Pas de channel \"general\" sur {server}"))

@bot.command(pass_context=True)
async def dino(ctx):
	print(f"{ctx.message.author} : {ctx.message.content}")
	print(dinosay("grrrrrr"))
	await bot.say("grrrrrr")


@bot.command(pass_context=True)
async def translate(ctx):
	if len(ctx.message.content) > 10:
		print(f"\n{ctx.message.author} : {ctx.message.content}")
		strg = ' '.join(ctx.message.content.split(' ')[1:])
		newStrg = ""
		for x in strg:
			if x != ' ':
				newStrg += chr(randint(65, 122))
			else:
				newStrg += ' '
		print(f"Dinobot : {newStrg}")
		await bot.say(newStrg)
	else:
		error = "Il manque le message Dino !"
		print(dinosay(error))
		await bot.say(error)


def dinosay(strg):
	return f"Dinobot : {strg}"


bot.run("secret")
