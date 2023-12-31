from crawlers import crawler
from crawlers import item
import random
import user_agents
import requests
import config
import time

class Csfloat(crawler.Crawler):
    def __init__(self, link, notifier):
        crawler.Crawler.__init__(self, link, notifier)
        self.links = [config.csfloatHighestDiscountLink, config.csfloatNewItemsLink]
        self.monitor_name = "CSFloat"

    def runCrawler(self):
        while True:
            for link in self.links:
                headers = { "User-Agent" : random.choice(user_agents.agents)}
                data = requests.get(link, headers=headers)
                
                if data.status_code != 200:
                    self.notifier.sendMonitorUpdate(self.createBannedEmbed())
                    time.sleep((60 * self.amountOfTimesBanned + self.timeoutTimer))
                    self.amountOfTimesBanned += 1
                
                else:
                    self.amountOfTimesBanned = 0
                    data = data.json()
                    self.searchItems(data)
            
                time.sleep(self.delay)

    def searchItems(self, data) -> list:
        self.items.clear()
        for i in data:
            if (1 - (i["price"] / i["reference"]["predicted_price"])) > 0.01:

                name = i["item"]["market_hash_name"]
                price = round(i["price"] * 0.01, 2)
                discount = round((1 - (i["price"] / i["reference"]["predicted_price"])) * 100, 1)
                floatValue = "N/A"
                collection = "N/A"
                imageLink = f'{config.steamImageLink}{i["item"]["icon_url"]}'
                id = i["id"]
                link = f'{config.csfloatItemLink}{i["id"]}'
                inspectLink = "N/A"
                patternID = "N/A"
                color = 0
                isSkin = False
                rarityName = i["item"]["rarity_name"]

                if "phase" in i["item"]:
                    name = f'{name} | {i["item"]["phase"]}'
                if "fade" in i["item"]:
                    name = f'{name} | {round(i["item"]["fade"]["percentage"], 2)}%'
                if "float_value" in i["item"]:
                    floatValue = round(i["item"]["float_value"], 5)
                    isSkin = True
                if i["item"]["has_screenshot"]:
                    imageLink = f'{config.csfloatBetterImageLink}{i["item"]["asset_id"]}-front.png'
                if "inspect_link" in i["item"]:
                    inspectLink = "Inspectable (check listing)"
                if "collection" in i["item"]:
                    collection = f'[{i["item"]["collection"]}]({config.collectionLink}{i["item"]["collection"].lower().replace(".", "").replace("& ","").replace(" ", "-")})'
                if "paint_seed" in i["item"]:
                    patternID = i["item"]["paint_seed"]

                if name.find("★") != -1:
                    color = config.yellowColor
                elif rarityName == "Exotic" or rarityName == "Classified":
                    color = config.pinkColor
                elif rarityName == "Restricted":
                    color = config.purpleColor
                elif rarityName == "Mil-Spec Grade":
                    color = config.blueColor
                elif rarityName == "Covert" or rarityName == "Extraordinary":
                    color = config.redColor
                else:
                    color = config.blackColor

                currentItem = item.Item(name, price, discount, floatValue, imageLink, id, link, inspectLink, patternID, color, collection, isSkin)
                if currentItem.id not in self.notifiedItems or (currentItem.id in self.notifiedItems and currentItem.price < self.notifiedItems[currentItem.id]):
                    self.items.append(currentItem)

        if len(self.items) > 0:
            self.sendAlerts()

        if self.firstPass:
            self.firstPass = False

        return self.items

    def sendAlerts(self):
        for item in self.items:
            if not self.firstPass:
                self.notifier.sendMessage(item.createEmbed("CSFloat"), item.isSkin, item.discount)

            self.notifiedItems[item.id] = item.price