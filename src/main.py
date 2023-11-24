from crawlers import csfloat
from crawlers import skinbid
import notify
import config
import threading

def main():
    notifyBot = notify.Notify()
    csfloatBot = csfloat.Csfloat(config.csfloatHighestDiscountLink, notifyBot)
    skinbidBot = skinbid.Skinbid(config.skinbidItemsLink, notifyBot)

    csfloatThread = threading.Thread(target=csfloatBot.runCrawler)
    skinbidThread = threading.Thread(target=skinbidBot.runCrawler)

    csfloatThread.daemon = True
    skinbidThread.daemon = True

    x = "1"

    while True:
        if x == "1":
            #csfloatThread.start()
            skinbidThread.start()
            x = "0"

if __name__ == "__main__":
    main()