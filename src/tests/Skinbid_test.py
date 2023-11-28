import json
from crawlers import skinbid, item

"""
SkinbidTestData consists of checking for:
    - If item is not a skin (sticker or container)
    - If item is a regular skin (doesn't have stattrack, doppler, etc)
    - If item has a doppler phase
    - If item has fade percentage
    - If item is stattrack
"""

with open("src/tests/SkinbidTestData.json", encoding="utf-8") as f:
    data = json.load(f)

correctItemsList = [
    item.Item("Sticker | cadiaN (Foil) | London 2018",
              19.14,
              32.19,
              "N/A",
              "https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9QVcJY8gulRRQ0LUSOr_h56LHE59IjtUt76sKglf1fzBfQJO7c6xkc6PkfKiY-OGkm0J6sAl3eiRp9-h2VC3rkdlZzjyI4aTe1c5NA7Q_1O3366x0jsUnahW",
              "60676515-cb15-4248-b0f6-538e601b80fc",
              "https://skinbid.com/market/60676515-cb15-4248-b0f6-538e601b80fc",
              "Inspectable (check listing)",
              "N/A",
              0x000000,
              "N/A - not provided",
              False),
    item.Item("SSG 08 | Threat Detected (Minimal Wear)",
              12.53,
              18.93,
              0.10018,
              "https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpopamie19f0v73eDNW6dC6nYeOmfTxDLTDl2VW7fp9g-7J4bP5iUazrl1rMmiicoGUdFQ3aA3RrwW7wOm-0cDouZ6cnSYw7CkityvZmxSwhxtOcKUx0kxNmVKx",
              "0f687e22-5281-470b-99bd-f9f118c8414b",
              "https://skinbid.com/market/0f687e22-5281-470b-99bd-f9f118c8414b",
              "Inspectable (check listing)",
              479,
              0x0026ff,
              "N/A - not provided",
              True),
    item.Item("★ Ursus Knife | Doppler (Factory New) | Sapphire",
              2181.03,
              17.91,
              0.02470,
              "https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpovbSsLQJfxuHbZC597dGJh4Gbh__9Ib7um2pD6sl0g_PE8bP5gVO8vywwMiukcZiUdVI_ZwmC-Fa-xb_ujZW7ucycyXZg6Ckn4HaIzUGz1BtPauNu1vOZVxzAUD4jS_xv",
              "39963fe4-7b3b-4a97-897a-1a681c04c6de",
              "https://skinbid.com/market/39963fe4-7b3b-4a97-897a-1a681c04c6de",
              "Inspectable (check listing)",
              619,
              0xffe100,
              "N/A - not provided",
              True),
    item.Item("★ Butterfly Knife | Fade (Factory New) | 80.6%",
              2812.8,
              10.37,
              0.01650,
              "https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpovbSsLQJf0ebcZThQ6tCvq4GKqPH1N77ummJW4NFOhujT8om7igW1qUY6MWqmcIadcw47MFrW_FK9xbzpgZ607Z7PzSAxuXYg53-Llwv330-D9XTwcQ",
              "ddfed68b-0259-4988-a1c4-d814d22f9147",
              "https://skinbid.com/market/ddfed68b-0259-4988-a1c4-d814d22f9147",
              "Inspectable (check listing)",
              787,
              0xffe100,
              "N/A - not provided",
              True),
    item.Item("StatTrak™ M4A1-S | Mecha Industries (Field-Tested)",
              52.56,
              9.6,
              0.28754,
              "https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpou-6kejhz2v_Nfz5H_uOxh7-Gw_alDLbUlWNQ18x_jvzS4Z78jUeLphY4OiyuS9rEMFFrf16DqALvl-_u05-6753JzCc3uSAntHjVnxCziEsZPLZo0KPNHQ2aAKBXXP7V3wxvJ98",
              "026e09a4-693f-47eb-bad3-3b72450fef1f",
              "https://skinbid.com/market/026e09a4-693f-47eb-bad3-3b72450fef1f",
              "Inspectable (check listing)",
              865,
              0xff0000,
              "N/A - not provided",
              True)
]

def test_Skinbid():
    skinbidCrawler = skinbid.Skinbid("N/A", "N/A")
    listToCheck = skinbidCrawler.searchItems(data)

    x = 0
    for i in listToCheck:
        assert i.name == correctItemsList[x].name
        assert i.collection == correctItemsList[x].collection
        assert i.float == correctItemsList[x].float
        assert i.price == correctItemsList[x].price
        assert i.discount == correctItemsList[x].discount
        assert i.imageLink == correctItemsList[x].imageLink
        assert i.inspectLink == correctItemsList[x].inspectLink
        assert i.color == correctItemsList[x].color
        assert i.patternID == correctItemsList[x].patternID
        assert i.link == correctItemsList[x].link
        assert i.id == correctItemsList[x].id
        assert i.isSkin == correctItemsList[x].isSkin
        x += 1
    # iterate