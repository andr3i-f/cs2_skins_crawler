from crawlers import csfloat
import notify
import config

'''
If there are multiple bots (i.e. skinfloat, csfloat) implement multithreading
andrei

'''

def main():
    notifyBot = notify.Notify()
    csfloatBot = csfloat.Csfloat(config.highestDiscountLink, notifyBot)

    while True:
        csfloatBot.searchItems()

main()