import config
import discord

class Crawler:
    def __init__(self, link, notifier):
        self.link = link
        self.items = []
        self.notifiedItems = {} # Stores an ID : price
        self.blocked = False
        self.notifier = notifier

        self.timeoutTimer = config.timeoutTimer 
        self.delay = config.delay
        self.firstPass = True

    def searchItems(self):
        pass

    def sendAlerts(self):
        pass

    def createBannedEmbed(self) -> discord.Embed:
        embed = discord.Embed(title="BONKED")
        embed.set_image(url="https://pbs.twimg.com/media/FiGpEeVWIAAKP2Y.jpg")

        return embed