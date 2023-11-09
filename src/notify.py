import config
import secret
import discord

class Notify:
    def __init__(self):
        self.webhook = discord.SyncWebhook.from_url(secret.webhook)
        self.updateWebhook = discord.SyncWebhook.from_url(secret.updateWebhook)

    def sendMessage(self, embed):
        self.webhook.send(embed=embed)

    def sendMonitorUpdate(self, embed):
        self.updateWebhook.send(embed=embed)