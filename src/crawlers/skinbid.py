from crawlers import crawler
from crawlers import item
import random
import user_agents
import requests
import config
import time

class Skinbid(crawler.Crawler):
    def __init__(self, link, notifier):
        crawler.Crawler.__init__(self, link, notifier)
    
    def runCrawler(self):
        while True:
            print("running skinbid")
            headers = {"User-Agent" : random.choice(user_agents.agents)}
            data = requests.get(self.link, headers=headers)

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
        for i in data["items"]:
            if i["items"][0]["isOnAuction"] or i["items"][0]["discount"] < 1:
                continue

            isSkin = False
            id = i["auction"]["auctionHash"]
            name = i["items"][0]["item"]["fullName"]
            price = i["nextMinimumBid"]
            discount = i["items"][0]["discount"]
            floatValue = "N/A"
            image_link = i["items"][0]["item"]["imageUrl"]
            patternID = "N/A"
            inspect_link = "N/A"
            collection = "N/A - not provided"
            link = f'{config.skinbidLink}{id}'
            rarity = i["items"][0]["item"]["rarity"]

            dopplerPhase = i["items"][0]["item"]["dopplerPhase"]
            fade = i["items"][0]["item"]["fade"]

            if dopplerPhase:
                name = f"{name} | {dopplerPhase}"
            if fade != 0:
                name = f"{name} | {fade}%"
            if i["items"][0]["item"]["inspectLink"]:
                inspect_link = "Inspectable (check listing)"
            if i["items"][0]["item"]["paintSeed"] != 0:
                patternID = i["items"][0]["item"]["paintSeed"]
            if i["items"][0]["item"]["float"]:
                floatValue = i["items"][0]["item"]["float"]
                isSkin = True

            if name.find("★") != -1:
                color = config.yellowColor
            elif rarity == 6:
                color = config.redColor
            elif rarity == 5:
                color = config.pinkColor
            elif rarity == 4:
                color = config.purpleColor
            elif rarity == 3:
                color = config.blueColor
            else:
                color = config.blackColor
            
            currentItem = item.Item(name, price, discount, floatValue, image_link, id, link, inspect_link, patternID, color, collection, isSkin)
            if currentItem.id not in self.notifiedItems or (currentItem.id in self.notifiedItems and currentItem.price < self.notifiedItems[currentItem.id]):
                self.items.append(currentItem)

        if len(self.items) > 0:
            self.sendAlerts()
        
        if self.firstPass:
            self.firstPass = False

        
    def sendAlerts(self):
        for item in self.items:
            if not self.firstPass:
                self.notifier.sendMessage(item.createEmbed("Skinbid"), item.isSkin)
            
            self.notifiedItems[item.id] = item.price
