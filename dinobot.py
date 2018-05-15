from discord.ext import commands
from bs4 import BeautifulSoup
from datetime import datetime
from random import randint
import collections
import requests
import discord
import base64
import re
import os


bot = commands.Bot(command_prefix="!")
bot.remove_command("help")


@bot.event
async def on_ready():
    """
        Display one of the messages when joining a server
    """
    messages = ["Grrrrrr Dinobot arrive sur le serveur !",
                "Dinobot arrive pour bouffer vos daronnes !",
                "Dinobot ici pour casser du CDAISI !",
                "Gogo dinoranger ! tutututututu"]
    for server in bot.servers:
        lstChannel = list(server.channels)
        lstChannelName = [x.name for x in list(server.channels)]
        try:
            index = lstChannelName.index("general")
            message = messages[randint(0, len(messages) - 1)]
            await bot.send_message(lstChannel[index], message)
        except:
            pass


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def info(ctx):
    """
        Command giving some infos about the bot
    """
    embedInfo = discord.Embed(
        title="Dinobot",
        description="0,+L$CK+t{K%,Lz+t+%htz#%,+L52+X2hAQrKDO/CK",
        color=0xe67e22
    )
    embedInfo.add_field(
        name="Author",
        value="Liodeus"
    )
    embedInfo.add_field(
        name="Invite",
        value="https://discordapp.com/api/oauth2/authorize?client_id=443818702677475338&permissions=0&scope=bot"
    )
    await bot.say(embed=embedInfo)


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def help(ctx):
    """
        This is the help command
    """
    embedHelp = discord.Embed(
        title="Dinobot",
        description="Liste des commandes :",
        color=0xe67e22
    )
    embedHelp.add_field(
        name="!help",
        value="Montre ce menu.",
        inline=False
    )
    embedHelp.add_field(
        name="!info",
        value="Montre les infos concernant le bot.",
        inline=False
    )
    embedHelp.add_field(
        name="!dino",
        value="Traduit du langage humain au dinosaure.",
        inline=False
    )
    embedHelp.add_field(
        name="!trad",
        value="Traduit du langage dinosaure à l'humain.",
        inline=False
    )
    embedHelp.add_field(
        name="!deadline",
        value="Affiche le nombre de jours restant avant de rendre de mémoire.",
        inline=False
    )
    embedHelp.add_field(
        name="!ask",
        value="Pose une question à Dinobot, peut-être qu'il te répondra !",
        inline=False
    )
    embedHelp.add_field(
        name="!rootme",
        value="Affiche le nombre de points de rootme.",
        inline=False
    )
    embedHelp.add_field(
        name="!ctftime",
        value="Affiche le scoreboard des 25 premières équipes françaises.",
        inline=False
    )
    embedHelp.add_field(
        name="!b64enc",
        value="Passe en base64 une/plusieurs phrases.",
        inline=False
    )
    embedHelp.add_field(
        name="!b64dec",
        value="Decode de la base64 une/plusieurs phrases.",
        inline=False
    )
    embedHelp.add_field(
        name="!bin2text",
        value="Passe du binaire à string.",
        inline=False
    )
    embedHelp.add_field(
        name="!bin2hex",
        value="Passe du binaire à l'hexadécimal.",
        inline=False
    )
    embedHelp.add_field(
        name="!bin2dec",
        value="Passe du binaire à décimal.",
        inline=False
    )
    embedHelp.add_field(
        name="!bin2oct",
        value="Passe du binaire  à l'octal.",
        inline=False
    )
    embedHelp.add_field(
        name="!text2bin",
        value="Passe de text à binaire.",
        inline=False
    )
    embedHelp.add_field(
        name="!text2hex",
        value="Passe de text à hexadécimal.",
        inline=False
    )
    embedHelp.add_field(
        name="!hex2int",
        value="Passe de l'hexadécimal à décimal.",
        inline=False
    )
    embedHelp.add_field(
        name="!hex2text",
        value="Passe de l'hexadécimal à string.",
        inline=False
    )
    await bot.say(embed=embedHelp)


@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        print("Spam")


#################################################################################
#                                 Misc Commands                                 #
#################################################################################


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def dino(ctx):
    """
        Command to translate from human to dinolanguage !
    """
    transTab = str.maketrans('!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}', '"HmT!bN.>(U#EBks3;_|oea:PQ7`4@Yn}0cS<rd&fx1wG\\RqMIvF\'j9^/*l[=J8yh)Dz+XAi,$O26LC{gt5%Kp]u-?WVZ')
    texts = ctx.message.content.split()[1:]
    strg = ""
    for text in texts:
        strg += f"{text.translate(transTab)} "
    await bot.say(strg)


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def trad(ctx):
    """
        Command to translate from dinolanguage to human !
    """
    transTab = str.maketrans('"HmT!bN.>(U#EBks3;_|oea:PQ7`4@Yn}0cS<rd&fx1wG\\RqMIvF\'j9^/*l[=J8yh)Dz+XAi,$O26LC{gt5%Kp]u-?WVZ', '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}')
    texts = ctx.message.content.split()[1:]
    strg = ""
    for text in texts:
        strg += f"{text.translate(transTab)} "
    await bot.say(strg)


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def deadline(ctx):
    """
        Display days of the deadline
    """
    deadline = datetime(2018, 6, 16) - datetime.now()
    await bot.say(f"Il ne reste plus que {deadline.days} jours ! Fais vite, la DinoDeadline arrive !\nElle se rapproche à grand pas...")


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def ask(ctx):
    """
        Command to translate from human to dinolanguage !
    """
    messages = ["Déso pas déso, je parle pas au triso !",
                "M'en bat les couilles frère", "Oui", "Non"]
    texts = ctx.message.content.split()[1:]
    if texts:
        await bot.say(messages[randint(0, len(messages) - 1)])
    else:
        await bot.say("Mais t'es débile ma parole ! Elle est ou la question ?")


#################################################################################
#                                  Scoreboards                                  #
#################################################################################


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def rootme(ctx):
    """
        Go fetch the score of each pseudos and display them
    """
    url = "https://www.root-me.org/"
    pseudos = ["Liodeus", "THEWOLF-37439",
               "Moindjaro", "Ori0n__",
               "Sneagle-121577", "CaptainKraken",
               "etraque"]
    dic = {}

    for pseudo in pseudos:
        res = requests.get(url + pseudo)
        soup = BeautifulSoup(res.text, "html.parser")
        infos = soup.find_all("ul", {"class": "spip"})
        spans = infos[0].find_all("span")
        score = spans[1].text
        dic[pseudo] = score

    order = collections.OrderedDict(sorted(dic.items(), key=lambda x: x[1]))
    final = [x for x in order.items()][::-1]
    _pseudo = '\n'.join(f"{x[0]}" for x in final)
    _score = '\n'.join(f"{x[1]}" for x in final)

    embedScore = discord.Embed(
        title="Score root-me",
        color=0xe67e22,
    )
    embedScore.add_field(
        name="Pseudo",
        value=_pseudo
    )
    embedScore.add_field(
        name="Score",
        value=_score
    )

    await bot.say(embed=embedScore)


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def ctftime(ctx):
    """
        Display the 25 first team from the french scoreboard
    """
    url = "https://ctftime.org/stats/2018/FR"
    headers = {
        "Connection": "close",
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) \
        Gecko/20100101 Firefox/40.1'}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    tab = soup.find_all("table", {"class": "table table-striped"})
    tds = tab[0].find_all("td")
    teams = tds[:125]

    mondialeFrance = ""
    nom = ""
    points = ""
    for x in range(0, len(teams), 5):
        teamName = re.findall('">(.*?)<', str(teams[x + 2]))

        mondialeFrance += f"{teams[x].text} / {teams[x+1].text}\n"
        nom += f"{teamName[0]}\n"
        points += f"{teams[x+3].text}\n"

    embed = discord.Embed(
        title="Scoreboard ctftime",
        color=0xe67e22,
    )
    embed.add_field(
        name="Mondial / France",
        value=mondialeFrance
    )
    embed.add_field(
        name="Nom",
        value=nom
    )
    embed.add_field(
        name="Points",
        value=points
    )

    await bot.say(embed=embed)


#################################################################################
#                                  CTF Commands                                 #
#################################################################################


@bot.command(pass_context=True)
@commands.cooldown(1, 1, commands.BucketType.user)
async def b64dec(ctx):
    """
        Decode one/multiples base64 to string
    """
    text = ctx.message.content.split()[1:]
    decode = ""
    for x in text:
        try:
            decode += f"{base64.b64decode(x)} "
        except base64.binascii.Error:
            decode += "`Erreur` "
    await bot.say(decode)


@bot.command(pass_context=True)
@commands.cooldown(1, 1, commands.BucketType.user)
async def b64enc(ctx):
    """
        Encode one/multiples string to base64
    """
    text = ctx.message.content.split()[1:]
    encode = ""
    for x in text:
        encode += str(base64.b64encode(bytes(x, "utf-8")), "utf-8")
    await bot.say(encode)


"""faire"""


@bot.command(pass_context=True)
@commands.cooldown(1, 1, commands.BucketType.user)
async def bin2text(ctx):
    """
        Decode one/multiples binary to text
    """
    binas = ctx.message.content.split()[1:]
    for bina in binas:
        try:
            n = int(bina, 2)
            decode = n.to_bytes((n.bit_length() + 7) // 8,
                                'big').decode("utf-8") or '\0'
            await bot.say(decode)
        except:
            await bot.say("Erreur de decode")


@bot.command(pass_context=True)
@commands.cooldown(1, 1, commands.BucketType.user)
async def bin2hex(ctx):
    """
        Decode one/multiples binary to hexadecimal
    """
    binas = ctx.message.content.split()[1:]
    decode = ""
    for bina in binas:
        try:
            decode += f"{int(bina, 2):x} "
        except ValueError:
            decode += "`Erreur` "
    await bot.say(decode)


@bot.command(pass_context=True)
@commands.cooldown(1, 1, commands.BucketType.user)
async def bin2dec(ctx):
    """
        Decode one/multiples binary to decimal
    """
    binas = ctx.message.content.split()[1:]
    decode = ""
    for bina in binas:
        try:
            decode += f"{int(bina, 2)} "
        except ValueError:
            decode += "`Erreur` "
    await bot.say(decode)


@bot.command(pass_context=True)
@commands.cooldown(1, 1, commands.BucketType.user)
async def bin2oct(ctx):
    """
        Decode one/multiples binary to octal
    """
    binas = ctx.message.content.split()[1:]
    decode = ""
    for bina in binas:
        try:
            decode += f"{int(bina, 2):o} "
        except ValueError:
            decode += "`Erreur` "
    await bot.say(decode)


@bot.command(pass_context=True)
@commands.cooldown(1, 1, commands.BucketType.user)
async def text2bin(ctx):
    """
        Encode one/multiples string to binary
    """
    texts = ctx.message.content.split()[1:]
    decode = ""
    for text in texts:
        bits = bin(int.from_bytes(text.encode("utf-8"), 'big'))[2:]
        decode += f"{bits.zfill(8 * ((len(bits) + 7) // 8))} "
    await bot.say(decode)


@bot.command(pass_context=True)
@commands.cooldown(1, 1, commands.BucketType.user)
async def text2hex(ctx):
    """
        Encode one/multiples string to hexadecimal
    """
    texts = ctx.message.content.split()[1:]
    decode = ""
    for text in texts:
        strg = ""
        for char in text:
            strg += f"0x{hex(ord(char))[2:]} "
        decode += strg
    await bot.say(decode)


@bot.command(pass_context=True)
@commands.cooldown(1, 1, commands.BucketType.user)
async def hex2int(ctx):
    """
        Encode one/multiples hexadecimal to integer
    """
    hexas = ctx.message.content.split()[1:]
    decode = ""
    for hexa in hexas:
        try:
            decode += f"{str(int(hexa, 16))} "
        except TypeError:
            decode += "`Erreur` "
        except ValueError:
            decode += "`Erreur` "
    await bot.say(decode)


@bot.command(pass_context=True)
@commands.cooldown(1, 1, commands.BucketType.user)
async def hex2text(ctx):
    """
        Encode one/multiples hexadecimal to text
    """
    hexas = ctx.message.content.split()[1:]
    decode = ""
    for hexa in hexas:
        try:
            strg = ""
            for char in hexa.split("0x"):
                if char != "":
                    strg += chr(int(char, 16))
            decode += f"{strg} "
        except TypeError:
            decode += "`Erreur` "
        except ValueError:
            decode += "`Erreur` "
        except OverflowError:
            decode += "`Erreur` "
    await bot.say(decode)


# hex2bin
# hex2octal
# url encode
# url decode
# text to rot13
# rot13 to text
# reverse a string

#################################################################################
#                                   Bot token                                   #
#################################################################################

bot.run(os.environ["BOT_TOKEN"])
