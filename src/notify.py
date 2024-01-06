import secret
import discord

class Notify:
    def __init__(self):
        self.stickerWebhook = discord.SyncWebhook.from_url(secret.stickerWebhook)
        self.updateWebhook = discord.SyncWebhook.from_url(secret.updateWebhook)

        self.oneToTenPercentWebhook = discord.SyncWebhook.from_url(secret.oneToTenPercentWebhook)
        self.elevenToFifteenPercentWebhook = discord.SyncWebhook.from_url(secret.elevenToFifteenPercentWebhook)
        self.sixteenToTwentyPercentWebhook = discord.SyncWebhook.from_url(secret.sixteenToTwentyPercentWebhook)
        self.twentyOnePlusPercentWebhook = discord.SyncWebhook.from_url(secret.twentyOnePlusPercentWebhook)

    def sendMessage(self, embed, isSkin, discount):
        if isSkin:
            if discount < 11:
                self.oneToTenPercentWebhook.send(embed=embed)
            elif discount < 16:
                self.elevenToFifteenPercentWebhook.send(embed=embed)
            elif discount < 20:
                self.sixteenToTwentyPercentWebhook.send(embed=embed)
            else:
                self.twentyOnePlusPercentWebhook.send(embed=embed)

        elif not isSkin:
            self.stickerWebhook.send(embed=embed)

    def sendMonitorUpdate(self, embed):
        self.updateWebhook.send(embed=embed)