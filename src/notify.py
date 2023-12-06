import secret
import discord

class Notify:
    def __init__(self):
        self.stickerWebhook = discord.SyncWebhook.from_url(secret.stickerWebhook)
        self.updateWebhook = discord.SyncWebhook.from_url(secret.updateWebhook)

        self.onePercentWebhook = discord.SyncWebhook.from_url(secret.onePercentWebhook)
        self.tenPercentWebhook = discord.SyncWebhook.from_url(secret.tenPercentWebhook)
        self.fifteenPercentWebhook = discord.SyncWebhook.from_url(secret.fifteenPercentWebhook)
        self.twentyPercentWebhook = discord.SyncWebhook.from_url(secret.twentyPercentWebhook)
        self.twentyfivePercentWebhook = discord.SyncWebhook.from_url(secret.twentyfivePercentWebhook)

    def sendMessage(self, embed, isSkin, discount):
        if isSkin:

            self.onePercentWebhook.send(embed=embed)

            if discount >= 10:
                self.tenPercentWebhook.send(embed=embed)
            if discount >= 15:
                self.fifteenPercentWebhook.send(embed=embed)
            if discount >= 20:
                self.twentyPercentWebhook.send(embed=embed)
            if discount >= 25:
                self.twentyfivePercentWebhook.send(embed=embed)


        elif not isSkin:
            self.stickerWebhook.send(embed=embed)

    def sendMonitorUpdate(self, embed):
        self.updateWebhook.send(embed=embed)