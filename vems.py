import discord
from discord.ext import commands


client = commands.Bot(command_prefix = "vems ", description = "Manager of VEMS eSports")


#Bot Online Status
@client.event
async def on_ready():
    activity = discord.Activity(type = discord.ActivityType.watching,
                                name = f"VEMS eSports community")
    await client.change_presence(status = discord.Status.dnd, activity = activity)
    print("Bot is online! \n")

client.run("NzMzNTA5OTgxNzcyNTc4OTE2.XxEMZw.sP59JUtJPB8h2MzZQB9dcrVtFB4")