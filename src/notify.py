import config
import secret
import discord

class Notify:
    def __init__(self):
        self.webhook = discord.SyncWebhook.from_url(secret.webhook)
        self.stickerWebhook = discord.SyncWebhook.from_url(secret.stickerWebhook)
        self.updateWebhook = discord.SyncWebhook.from_url(secret.updateWebhook)

    def sendMessage(self, embed, webhookNumber):
        if webhookNumber == 0:
            self.webhook.send(embed=embed)
        elif webhookNumber == 1:
            self.stickerWebhook.send(embed=embed)

    def sendMonitorUpdate(self, embed):
        self.updateWebhook.send(embed=embed)