import discord
import os
from dotenv import load_dotenv

class Notify:
    def __init__(self):
        load_dotenv()
        self.stickerWebhook = discord.SyncWebhook.from_url(os.getenv('STICKER_WH'))
        self.updateWebhook = discord.SyncWebhook.from_url(os.getenv('UPDATE_WH'))

        self.oneToTenPercentWebhook = discord.SyncWebhook.from_url(os.getenv('ONE_TO_TEN_PERCENT_WH'))
        self.elevenToFifteenPercentWebhook = discord.SyncWebhook.from_url(os.getenv('ELEVEN_TO_FIFTEEN_PERCENT_WH'))
        self.sixteenToTwentyPercentWebhook = discord.SyncWebhook.from_url(os.getenv('SIXTEEN_TO_TWENTY_PERCENT_WH'))
        self.twentyOnePlusPercentWebhook = discord.SyncWebhook.from_url(os.getenv('TWENTY_ONE_PLUS_PERCENT_WH'))

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