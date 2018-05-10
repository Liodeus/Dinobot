import discord
from discord.ext.commands import Bot
from discord.ext import commands
from random import randint
from time import sleep
import asyncio
import requests
import re
import os
import collections
import base64
from bs4 import BeautifulSoup
import binascii


bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
	messages = ["Grrrrrr Dinobot arrive sur le serveur !", "Dinobot arrive pour bouffer vos daronnes !", "Dinobot ici pour casser du CDAISI !"]
	for server in bot.servers:
		lstChannel = list(server.channels)
		lstChannelName = [x.name for x in list(server.channels)]
		try:
			index = lstChannelName.index("general")
			print(f"Join {server}")
			message = messages[randint(0, len(messages) - 1)]
			print(f"{message}")
			await bot.send_message(lstChannel[index], message)
		except:
			print(dinosay("Pas de channel \"general\" sur {server}"))


@bot.event
async def on_command_error(error, ctx):
	if isinstance(error, commands.CommandOnCooldown):
		print("Spam")


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def dino(ctx):
		await bot.say("grrrrrr")


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def trad(ctx):
	if len(ctx.message.content) > 6:
		strg = ' '.join(ctx.message.content.split(' ')[1:])
		newStrg = ''.join(chr(randint(65, 122)) if x != ' ' else ' ' for x in strg)
		await bot.say(newStrg)
	else:
		error = "Il manque le message Dino !"
		await bot.say(error)


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def rootme(ctx):
	url = "https://www.root-me.org/"
	pseudos = ["Liodeus", "THEWOLF-37439", "Moindjaro", "Ori0n__", "Sneagle-121577"]
	dic = {}

	for pseudo in pseudos:
		res = requests.get(url + pseudo)
		soup = BeautifulSoup(res.text, "html.parser")
		infos = soup.find_all("ul", {"class": "spip"})
		spans = infos[0].find_all("span")
		score = spans[1].text

		dic[pseudo] = score
	order = collections.OrderedDict(sorted(dic.items(), key=lambda x : x[1]))
	final = [x for x in order.items()][::-1]
	_pseudo = '\n'.join(f"{x[0]}" for x in final)
	_score = '\n'.join(f"{x[1]}" for x in final)

	embedScore = discord.Embed(
		title = "Score root-me",
		color = 0xe67e22,
	)
	embedScore.add_field(
		name = "Pseudo",
		value = _pseudo
	)
	embedScore.add_field(
		name = "Score",
		value = _score
	)

	await bot.say(embed=embedScore)


@bot.command(pass_context = True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def ctftime(ctx):
	url = "https://ctftime.org/stats/2018/FR"
	headers = {
		"Connection": "close",
		"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'	}

	res = requests.get(url, headers=headers)
	soup = BeautifulSoup(res.text, "html.parser")
	tab = soup.find_all("table", {"class": "table table-striped"})
	tds = tab[0].find_all("td")
	teams = tds[:125]

	mondialeFrance = ""
	nom = ""
	points = ""
	strg = ""
	for x in range(0, len(teams), 5):
		teamName = re.findall('">(.*?)<', str(teams[x+2]))
		
		mondialeFrance += f"{teams[x].text} / {teams[x+1].text}\n"
		nom += f"{teamName[0]}\n"
		points += f"{teams[x+3].text}\n"

	embed = discord.Embed(
		title = "Scoreboard ctftime",
		color = 0xe67e22,
	)
	embed.add_field(
		name = "Mondial / France",
		value = mondialeFrance
	)
	embed.add_field(
		name = "Nom",
		value = nom
	)
	embed.add_field(
		name = "Points",
		value = points
	)

	await bot.say(embed=embed)


@bot.command(pass_context = True)
@commands.cooldown(1, 1, commands.BucketType.user)
async def b64dec(ctx):
	text = ctx.message.content.split()[1:]
	for x in text:
		try:
			decode = str(base64.b64decode(x), "utf-8")
			await bot.say(decode)
		except:
			await bot.say("Erreur de decode")


@bot.command(pass_context = True)
@commands.cooldown(1, 1, commands.BucketType.user)
async def b64enc(ctx):
	text = ctx.message.content.split()[1:]
	for x in text:
		try:
			encode = str(base64.b64encode(bytes(x, "utf-8")), "utf-8")
			await bot.say(encode)
		except:
			await bot.say("Erreur d'encodage")


@bot.command(pass_context = True)
@commands.cooldown(1, 1, commands.BucketType.user)
async def bin2text(ctx):
	binas = ctx.message.content.split()[1:]
	for bina in binas:
		try:
			n = int(bina, 2)
			decode = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode("utf-8") or '\0'
			await bot.say(decode)
		except:
			await bot.say("Erreur de decode")


@bot.command(pass_context = True)
@commands.cooldown(1, 1, commands.BucketType.user)
async def text2bin(ctx):
	texts = ctx.message.content.split()[1:]
	for text in texts:
		try:
			bits = bin(int.from_bytes(text.encode("utf-8"), 'big'))[2:]
			decode = bits.zfill(8 * ((len(bits) + 7) // 8))
			await bot.say(decode)
		except:
			await bot.say("Erreur de decode")


bot.run(os.environ["BOT_TOKEN"])
