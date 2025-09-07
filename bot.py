import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
async def delete_all(ctx):
    """Deletes all channels and categories in the server."""
    guild = ctx.guild
    await ctx.send("⚠️ Deleting all channels and categories...")

    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"🗑️ Deleted {channel.name}")
        except Exception as e:
            print(f"❌ Could not delete {channel.name}: {e}")

    await ctx.send("✅ All channels and categories deleted!")

bot.run("YOUR_BOT_TOKEN")
