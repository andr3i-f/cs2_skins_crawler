import discord

class Item:
    def __init__(self, name, price, discount, floatValue, imageLink, id, link, inspectLink, patternID, color, collection, isSkin):
        self.name = name
        self.collection = collection
        self.float = floatValue
        self.price = price
        self.discount = discount
        self.imageLink = imageLink
        self.inspectLink = inspectLink
        self.color = color
        self.patternID = patternID
        self.link = link
        self.id = id
        self.isSkin = isSkin

    def createEmbed(self, website) -> discord.Embed:
        embed = discord.Embed(title=self.name, url=self.link, color=self.color)

        embed.set_image(url=self.imageLink)
        embed.add_field(name="Price", value=f'${self.price}', inline=True)
        embed.add_field(name="Float", value=self.float, inline=True)
        embed.add_field(name="Collection", value=f'{self.collection}', inline=True)
        embed.add_field(name="Discount", value=f'{self.discount}%', inline=True)
        embed.add_field(name="Pattern", value=self.patternID, inline=True)
        embed.add_field(name="Inspect", value=self.inspectLink, inline=True)

        embed.set_footer(text=f"{website} Crawler")

        return embed