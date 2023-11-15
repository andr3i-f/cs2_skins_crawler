import config
import discord

class Crawler:
    def __init__(self, link, notifier):
        self.link = link
        self.items = []
        self.notifiedItems = {} # Stores an ID : price
        self.blocked = False
        self.notifier = notifier
        self.monitor_name = "default"

        self.amountOfTimesBanned = 0
        self.timeoutTimer = config.timeoutTimer 
        self.delay = config.delay
        self.firstPass = True

    def searchItems(self):
        pass

    def sendAlerts(self):
        pass

    def createBannedEmbed(self) -> discord.Embed:
        embed = discord.Embed(title=f"Banned from: {self.monitor_name}")
        embed.add_field(name="Waiting until next try (seconds)", value=(self.amountOfTimesBanned * 60 + self.timeoutTimer))
        return embed