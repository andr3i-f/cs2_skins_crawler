from crawlers import crawler
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
                #print(items.status_code)
                items = items.json()
                for item in items:
                    currentItem = {}

                    if "StatTrak" in item["item"]["market_hash_name"]:
                        currentItem["name"] = f'StatTrak™ {item["item"]["item_name"]}'
                    else:
                        currentItem["name"] = item["item"]["item_name"]

                    if "phase" in item["item"]:
                        currentItem["name"] = f'{currentItem["name"]} | {item["item"]["phase"]}' 

                    if "fade" in item["item"]:
                        currentItem["name"] = f'{currentItem["name"]} | {round(item["item"]["fade"]["percentage"], 2)}%' 

                    if "wear_name" in item["item"]: 
                        currentItem["wear_name"] = item["item"]["wear_name"]
                    else:
                        currentItem["wear_name"] = "N/A"

                    if "float_value" in item["item"]:
                        currentItem["float"] = round(item["item"]["float_value"], 5)
                    else:
                        currentItem["float"] = "N/A"

                    currentItem["price"] = round(item["price"] * 0.01, 2)
                    currentItem["discount"] = round((1 - (item["price"] / item["reference"]["predicted_price"])) * 100, 1)

                    if item["item"]["type_name"] != "Sticker" and requests.get(f'{config.betterImageLink}{item["item"]["asset_id"]}-front.png').status_code == 200:
                        currentItem["image"] = f'{config.betterImageLink}{item["item"]["asset_id"]}-front.png'
                    else:
                        currentItem["image"] = f'{config.imageLink}{item["item"]["icon_url"]}'

                    currentItem["id"] = item["id"]
                    currentItem["link"] = f'{config.itemLink}{item["id"]}'

                    if "inspect_link" in item["item"]:
                        currentItem["inspect"] = "Inspectable (check listing)"
                    else:
                        currentItem["inspect"] = "N/A"
                    
                    currentItem["rarity_name"] = item["item"]["rarity_name"]

                    if currentItem["name"].find("★") != -1:
                        currentItem["color"] = config.yellowColor
                    elif item["item"]["rarity_name"] == "Exotic" or item["item"]["rarity_name"] == "Classified":
                        currentItem["color"] = config.pinkColor
                    elif item["item"]["rarity_name"] == "Restricted":
                        currentItem["color"] = config.purpleColor
                    elif item["item"]["rarity_name"] == "Mil-Spec":
                        currentItem["color"] = config.blueColor
                    elif item["item"]["rarity_name"] == "Covert" or item["item"]["rarity_name"] == "Extraordinary":
                        currentItem["color"] = config.redColor
                    else:
                        currentItem["color"] = config.blackColor
                    
                    currentItem["watchers"] = item["watchers"]
                    currentItem["state"] = item["state"]


                    if currentItem["discount"] > 0:
                        if currentItem["id"] not in self.notifiedItems or (currentItem["id"] in self.notifiedItems and currentItem["price"] < self.notifiedItems[currentItem["id"]]):
                            self.notifiedItems[currentItem["id"]] = currentItem["price"]
                            if not self.firstPass:
                                self.notifier.sendMessage(self.createItemEmbed(currentItem))

            if self.firstPass:
                self.firstPass = False
            time.sleep(self.delay)


    def createItemEmbed(self, item) -> discord.Embed:
        embed = discord.Embed(title=item["name"], url=item["link"], color=item["color"])

        embed.set_image(url=item["image"])
        embed.add_field(name="Price", value=f'${item["price"]}', inline=True)
        embed.add_field(name="Discount", value=f'{item["discount"]}%', inline=True)
        embed.add_field(name="Wear", value=item["wear_name"], inline=True)
        embed.add_field(name="Float", value=item["float"], inline=True)
        embed.add_field(name="Inspect", value=item["inspect"], inline=True)
        embed.add_field(name="Watchers", value=item["watchers"], inline=True)

        embed.set_footer(text="CSFloat Crawler by endrei")

        return embed
