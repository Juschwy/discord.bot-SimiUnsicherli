from discord.ext import commands


@commands.command(name='test')
async def test(ctx, *args):
    await ctx.send(f'Eingabe: {" ".join(args)}')

def setup(bot):
    bot.add_command(test)