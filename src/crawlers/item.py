import discord

class Item:
    def __init__(self, name, price, discount, floatValue, image_link, id, link, inspect_link, watchers, color, wear_name):
        self.name = name
        self.wear_name = wear_name
        self.float = floatValue
        self.price = price
        self.discount = discount
        self.image_link = image_link
        self.inspect_link = inspect_link
        self.color = color
        self.watchers = watchers
        self.link = link
        self.id = id

    def createEmbed(self) -> discord.Embed:
        embed = discord.Embed(title=self.name, url=self.link, color=self.color)

        embed.set_image(url=self.image_link)
        embed.add_field(name="Price", value=f'${self.price}', inline=True)
        embed.add_field(name="Discount", value=f'{self.discount}%', inline=True)
        embed.add_field(name="Wear", value=f'{self.wear_name}', inline=True)
        embed.add_field(name="Float", value=self.float, inline=True)
        embed.add_field(name="Inspect", value=self.inspect_link, inline=True)
        embed.add_field(name="Watchers", value=self.watchers, inline=True)

        embed.set_footer(text="CSFloat Crawler by endrei")

        return embed