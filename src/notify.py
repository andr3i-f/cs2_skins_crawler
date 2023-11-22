import config
import secret
import discord

class Notify:
    def __init__(self):
        self.webhook = discord.SyncWebhook.from_url(secret.webhook)
        self.stickerWebhook = discord.SyncWebhook.from_url(secret.stickerWebhook)
        self.updateWebhook = discord.SyncWebhook.from_url(secret.updateWebhook)

    def sendMessage(self, embed, isSkin):
        if isSkin == True:
            self.webhook.send(embed=embed)
        elif isSkin == False:
            self.stickerWebhook.send(embed=embed)

    def sendMonitorUpdate(self, embed):
        self.updateWebhook.send(embed=embed)