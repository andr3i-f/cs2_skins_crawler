from crawlers import crawler
from crawlers import item
import random
import user_agents
import requests
import config
import discord
import time

class Csfloat(crawler.Crawler):
    def __init__(self, link, notifier):
        crawler.Crawler.__init__(self, link, notifier)
        self.links = [config.highestDiscountLink, config.newItemsLink]
    
    def searchItems(self):
        for link in self.links:
            headers = { "User-Agent" : random.choice(user_agents.agents)}
            items = requests.get(link, headers=headers)
            
            if items.status_code != 200:
                self.notifier.sendMonitorUpdate(self.createBannedEmbed())
                print("bonked, sleeping for 5 minutes")
                time.sleep(self.timeoutTimer)

            else:
                items = items.json()
                for i in items:
                    if i["price"] / i["reference"]["predicted_price"] > 0:

                        name = i["item"]["market_hash_name"]
                        price = round(i["price"] * 0.01, 2)
                        discount = round((1 - (i["price"] / i["reference"]["predicted_price"])) * 100, 1)
                        floatValue = "N/A"
                        image_link = f'{config.imageLink}{i["item"]["icon_url"]}'
                        id = i["id"]
                        link = f'{config.itemLink}{i["id"]}'
                        inspect_link = "N/A"
                        watchers = i["watchers"]
                        color = 0

                        if "phase" in i["item"]:
                            name = f'{name} | {i["item"]["phase"]}'
                        if "fade" in i["item"]:
                            name = f'{name} | {round(i["item"]["fade"]["percentage"], 2)}%'
                        if "float_value" in i["item"]:
                            floatValue = round(i["item"]["float_value"], 5)
                        if i["item"]["type_name"] != "Sticker" and requests.get(f'{config.betterImageLink}{i["item"]["asset_id"]}-front.png').status_code == 200:
                            image_link = f'{config.betterImageLink}{i["item"]["asset_id"]}-front.png'
                        if "inspect_link" in i["item"]:
                            inspect_link = "Inspectable (check listing)"

                        if name.find("★") != -1:
                            color = config.yellowColor
                        elif i["item"]["rarity_name"] == "Exotic" or i["item"]["rarity_name"] == "Classified":
                            color = config.pinkColor
                        elif i["item"]["rarity_name"] == "Restricted":
                            color = config.purpleColor
                        elif i["item"]["rarity_name"] == "Mil-Spec":
                            color = config.blueColor
                        elif i["item"]["rarity_name"] == "Covert" or i["item"]["rarity_name"] == "Extraordinary":
                            color = config.redColor
                        else:
                            color = config.blackColor

                        currentItem = item.Item(name, price, discount, floatValue, image_link, id, link, inspect_link, watchers, color)
                        if currentItem.id not in self.notifiedItems or (currentItem.id in self.notifiedItems and currentItem.price < self.notifiedItems[currentItem.id]):
                            self.notifiedItems[currentItem.id] = currentItem.price

                            if not self.firstPass:
                                if currentItem.float == "N/A":
                                    self.notifier.sendMessage(currentItem.createEmbed(), 1)
                                elif currentItem.float != "N/A":
                                    self.notifier.sendMessage(currentItem.createEmbed(), 0)

            if self.firstPass:
                self.firstPass = False
            time.sleep(self.delay)