import os
import discord

class Notify:
    def __init__(self):
        self.stickerWebhook = discord.SyncWebhook.from_url(os.environ["STICKER_WH"])
        self.updateWebhook = discord.SyncWebhook.from_url(os.environ["UPDATE_WH"])

        self.oneToTenPercentWebhook = discord.SyncWebhook.from_url(os.environ["ONE_TO_TEN_WH"])
        self.elevenToFifteenPercentWebhook = discord.SyncWebhook.from_url(os.environ["ELEVEN_TO_FIFTEEN_WH"])
        self.sixteenToTwentyPercentWebhook = discord.SyncWebhook.from_url(os.environ["SIXTEEN_TO_TWENTY_WH"])
        self.twentyOnePlusPercentWebhook = discord.SyncWebhook.from_url(os.environ["TWENTYONE_PLUS_WH"])

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