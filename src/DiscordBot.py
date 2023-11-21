import discord
from discord import app_commands, member
from discord.ext import commands
import secret

TOKEN = secret.bot_token
intents = discord.Intents.default()
intents.message_content = True
#client = discord.Client(intents=intents)
guild_id = 1168967314419486871
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

def main():
    @bot.event
    async def on_ready():
        await tree.sync(guild=discord.Object(id=guild_id))
        print(f'{bot.user} has connected to Discord')

    @tree.command(name="add_role", description="Gives you a role", guild=discord.Object(id=guild_id))
    async def add_role(interaction):
        await interaction.response.send_message("Added role")

    bot.run(TOKEN)

if __name__ == "__main__":
    main()