import discord
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with your bot's token
BOT_TOKEN = '#Put_your_token_here'

intents = discord.Intents().all()

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('Guilds the bot is in:')
    for guild in bot.guilds:
        print(f'{guild.name} (ID: {guild.id})')

@bot.command()
async def list_guilds(ctx):
    if ctx.author.guild_permissions.administrator:
        guild_list = [(guild.name, guild.id) for guild in bot.guilds]
        guild_info = "\n".join([f'**{name}** : ``{id}``' for name, id in guild_list])
        await ctx.send(f"```Guilds I'm in:```\n{guild_info}")
    else:
        await ctx.send('You do not have permission to use this command.')

@bot.command()
@commands.is_owner()
async def leave_guild(ctx, guild_id: int):
    guild = bot.get_guild(guild_id)
    if guild:
        await guild.leave()
        await ctx.send(f'Bot has left the server: {guild.name} (ID: {guild.id})')
    else:
        await ctx.send('Guild not found or bot is not in the guild.')

bot.run(BOT_TOKEN)
