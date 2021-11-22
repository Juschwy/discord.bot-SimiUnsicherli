from discord.ext import commands

@commands.command(name='run_server')
async def test(ctx):
    await ctx.send('Diese Funktion ist leider noch nicht verfügbar.')

def setup(bot):
    bot.add_commands(run_server)