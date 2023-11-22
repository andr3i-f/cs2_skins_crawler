from crawlers import csfloat
from crawlers import skinbid
from tests import CSFloatTests
import unittest
import notify
import config
import DiscordBot
import threading

'''
If there are multiple bots (i.e. skinfloat, csfloat) implement multithreading
andrei

'''
def tests():
    suite = unittest.TestLoader().loadTestsFromModule(CSFloatTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

def main():
    notifyBot = notify.Notify()
    csfloatBot = csfloat.Csfloat(config.highestDiscountLink, notifyBot)
    skinbidBot = skinbid.Skinbid(config.skinbidItemsLink, notifyBot)

    csfloatThread = threading.Thread(target=csfloatBot.runCrawler)
    skinbidThread = threading.Thread(target=skinbidBot.runCrawler)

    csfloatThread.daemon = True
    skinbidThread.daemon = True

    #tests()
    #csfloatBot.runCrawler()
    csfloatThread.start()
    skinbidThread.start()

    csfloatThread.join()
    skinbidThread.join()


main()