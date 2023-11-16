from crawlers import csfloat
from tests import CSFloatTests
import unittest
import notify
import config
import DiscordBot

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

    #tests()

    while True:
        csfloatBot.runCrawler()


main()