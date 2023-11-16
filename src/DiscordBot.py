import discord
from discord.ext import commands
import secret

TOKEN = secret.bot_token
intents = discord.Intents.default()
intents.message_content = True
#client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="$", intents=intents)

def main():
    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord')

    @bot.command()
    async def test(ctx, arg):
        print("asd")
        await ctx.send(arg)

    @bot.event
    async def on_message(message):
        print(f"message {message.author} {message.content}")
        if message.author == bot.user:
            return
        if message.content == "hello":
            await message.channel.send(f"hi {message.author}")

    bot.run(TOKEN)

if __name__ == "__main__":
    main()