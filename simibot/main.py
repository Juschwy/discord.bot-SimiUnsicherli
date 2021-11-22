import sys
import traceback
from os import listdir
from os.path import isfile, join
import csv
import pandas
import discord
from discord.ext import commands
import pytz
from datetime import datetime

class PythonBot(commands.Bot):

    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)

async def on_ready(self):
    print(f'BotId: {bot.user.id} - Name: {bot.user.name}')

async def on_raw_reaction_add(self, payload):
    if payload.member.bot:
        return
    if payload.channel_id == 911690965226520616:
        if payload.message_id == 911691005399547915:
            if payload.emoji.name == '🦷':
                guild: discord.Guild = bot.get_guild(911556407084609556)
                channel: discord.TextChannel = guild.get_channel(911690965226520616)

                role: discord.Role = guild.get_role(911917793224560700)
                await payload.member.add_roles(role, reason='Zuweisung')

                message = await channel.send('Du hast den Zahn gezogen.')
                await message.add_reaction('🦷')


bot = PythonBot(intents=discord.Intents.all(), command_prefix='!')

@bot.command(name='hilfe')
async def test(ctx):
    await ctx.send('Liste aller Befehle:'
                   '````!userinfo @person``` zeigt Infos zu bestimmten Personen an.'
                   '```!run:server``` startet den Minecraft-Server (noch nicht verfügbar)'
                   '```!julian``` Jules ist cooler')

@bot.command(name='julian')
async def test(ctx):
    await ctx.send('Jules ist cooler')
    await ctx.send('Jules ist cooler')
    await ctx.send('Jules ist cooler')
    await ctx.send('Jules ist cooler')
    await ctx.send('Jules ist cooler')
    await ctx.send('Jules ist cooler')
    await ctx.send('Jules ist cooler')
    await ctx.send('Jules ist cooler')
    await ctx.send('Jules ist cooler')
    await ctx.send('Jules ist cooler')
    await ctx.send('Jules ist cooler')
    await ctx.send('Jules ist cooler')
    await ctx.send('Jules ist cooler')

@bot.command(name='run:server')
async def test(ctx):
    await ctx.send('Diese Funktion ```!run:server``` ist leider noch nicht verfügbar.')
    print(f'run:server wurde versucht auszuführen')

@bot.command(name='test')
async def test(ctx, *args):
    await ctx.send(f'Eingabe: {" ".join(args)}')

@bot.command(name='userinfo')
async def userinfo(ctx, member: discord.Member):
    hi = pandas.read_csv('daten.csv')
    print(hi)
    de = pytz.timezone('Europe/Berlin')
    embed = discord.Embed(title=f'> Userinfo für {member.display_name}',
                          description='', color=0x4cd137, timestamp=datetime.now().astimezone(tz=de))

    embed.add_field(name='Name', value=f'```{member.name}#{member.discriminator}```', inline=True)
    embed.add_field(name='Bot', value=f'```{("Ja" if member.bot else "Nein")}```', inline=True)
    embed.add_field(name='Nickname', value=f'```{(member.nick if member.nick else "Nicht gesetzt")}```', inline=True)
    embed.add_field(name='Server beigetreten', value=f'```{member.joined_at}```', inline=True)
    embed.add_field(name='Discord beigetreten', value=f'```{member.created_at}```', inline=True)
    embed.add_field(name='Rollen', value=f'```{len(member.roles)}```', inline=True)
    embed.add_field(name='Höchste Rolle', value=f'```{member.top_role.name}```', inline=True)
    embed.add_field(name='Farbe', value=f'```{member.color}```', inline=True)
    embed.add_field(name='Booster', value=f'```{("Ja" if member.premium_since else "Nein")}```', inline=True)
    embed.add_field(name='Minecraft-Name', value=f'```{"Noch nicht vorhanden"}```', inline=True)
    embed.add_field(name='Team', value=f'```{"Noch nicht vorhanden"}```', inline=True)
    embed.add_field(name='Base-Coords', value=f'```{"Noch nicht vorhanden"}```', inline=True)
    embed.set_footer(text=f'Angefordert von {ctx.author.name} • {ctx.author.id}', icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

bot.run('OTExMjY5MzUxODEyOTE5MzA2.YZe7uA.I8pkrVw1h2oeSft2MNWmz_4_Zp4')