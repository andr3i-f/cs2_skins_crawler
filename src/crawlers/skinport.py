from crawlers import crawler
import random
import user_agents
import requests
import config
import discord
import time

class Skinport(crawler.Crawler):
    def __init__(self, link, notifier):
        crawler.Crawler.__int__(self, link, notifier)

    def searchItems(self):
        pass