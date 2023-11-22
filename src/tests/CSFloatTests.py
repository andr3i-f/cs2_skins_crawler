import unittest
import json
from crawlers import csfloat, item

"""
CSFloatTestData consists of checking for:
    - If item has fade percentage
    - If item is a sticker (should apply for containers as well)
    - If item is stattrack
    - If item doesn't "better" screenshot and no inspect link
    - If item has "better" screenshot and inspect link
    - If item is a container

Prices of items have been adjusted so it has a discount %
"""

with open("src/tests/CSFloatTestData.json", encoding="utf-8") as f:
    data = json.load(f)

correctItemsList = [
    item.Item("★ StatTrak™ M9 Bayonet | Fade (Factory New) | 84.39%",
              1639,
              11.9,
              0.01104,
              "https://s.csgofloat.com/34269345930-front.png",
              "641299126818049306",
              "https://csfloat.com/item/641299126818049306",
              "Inspectable (check listing)",
              630,
              0xffe100,
              "N/A",
              True),
    item.Item("Sticker | bodyy (Foil) | Krakow 2017",
              20.35,
              10.8,
              "N/A",
              "https://community.cloudflare.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9QVcJY8gulRWXk3bSPP_h56EHE59IjtVub68Mjhm3PrETjFD_tuz2tWJwfOmYL3Uzm4FucAj2brDotT021KxrRFqYj-mcYfHdwM7ZliB81aggbC4GRo6qeU",
              "641685061690853901",
              "https://csfloat.com/item/641685061690853901",
              "N/A",
              "N/A",
              0x000000,
              "N/A",
              False),
    item.Item("★ StatTrak™ Butterfly Knife | Gamma Doppler (Factory New) | Phase 1",
              1870,
              6.7,
              0.04815,
              "https://community.cloudflare.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpovbSsLQJf0ebcZThQ6tCvq4GGqPD1PrbQqW9e-NV9j_v-5YT0m1HllB81NDG3S9rEMFFrf1iC_QXqw7u9h5PqupTKyiNh6ClxtCvczUPmgUtPPbE-1qDISFicAqVXXP7V9p_o84A",
              "643006786961540796",
              "https://csfloat.com/item/643006786961540796",
              "Inspectable (check listing)",
              453,
              0xffe100,
              "N/A",
              True),
    item.Item("Tec-9 | Cracked Opal (Minimal Wear)",
              0.06,
              25,
              0.09334,
              "https://community.cloudflare.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpoor-mcjhjxszcdD4b09-klYOAkvPLPKvQmlRd4cJ5ntbN9J7yjRqw_RZlMDryd4WUdwM-NwmFqwK3kuvqhpK97sjIznIy6HYi4n3Zmkewn1gSOdsvfAHj",
              "643221582671644613",
              "https://csfloat.com/item/643221582671644613",
              "N/A",
              931,
              0x0026ff,
              "[The Spectrum 2 Collection](https://csgoskins.gg/collections/the-spectrum-2-collection)",
              True),
    item.Item("AK-47 | Nightwish (Factory New)",
              90,
              15.5,
              0.00076,
              "https://s.csgofloat.com/34444149914-front.png",
              "643221024900515491",
              "https://csfloat.com/item/643221024900515491",
              "Inspectable (check listing)",
              534,
              0xff0000,
              "[The Dreams & Nightmares Collection](https://csgoskins.gg/collections/the-dreams-nightmares-collection)",
              True),
    item.Item("Clutch Case",
              0.39,
              20.4,
              "N/A",
              "https://community.cloudflare.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQNqhpOSV-fRPasw8rsUFJ5KBFZv668FFY5naqQIz4R7Yjix9bZkvKiZrmAzzlTu5AoibiT8d_x21Wy8hY_MWz1doSLMlhpM3FKbNs",
              "643221862180063381",
              "https://csfloat.com/item/643221862180063381",
              "N/A",
              "N/A",
              0x000000,
              "N/A",
              False)
    ]


class TestCSFloatMethods(unittest.TestCase):
    def test_searchItems(self):
        csfloatCrawler = csfloat.Csfloat("N/A", "N/A")
        listToCheck = csfloatCrawler.searchItems(data)

        x = 0
        for i in listToCheck:
            self.assertEqual(i.name, correctItemsList[x].name, f"Names not equal - index {x}")
            self.assertEqual(i.collection, correctItemsList[x].collection, f"Wear names not equal - index {x}")
            self.assertEqual(i.float, correctItemsList[x].float, f"Float values not equal - index {x}")
            self.assertEqual(i.price, correctItemsList[x].price, f"Price values not equal - index {x}")
            self.assertEqual(i.discount, correctItemsList[x].discount, f"Discount values not equal - index {x}")
            self.assertEqual(i.image_link, correctItemsList[x].image_link, f"Image links not equal - index {x}")
            self.assertEqual(i.inspect_link, correctItemsList[x].inspect_link, f"Inspect links not equal - index {x}")
            self.assertEqual(i.color, correctItemsList[x].color, f"Color values not equal - index {x}")
            self.assertEqual(i.patternID, correctItemsList[x].patternID, f"Watchers value not equal - index {x}")
            self.assertEqual(i.link, correctItemsList[x].link, f"Link not equal - index {x}")
            self.assertEqual(i.id, correctItemsList[x].id, f"ID not equal - index {x}")
            x += 1