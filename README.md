# cs2_skins_crawler
Monitors CS2 skin marketplaces for good discounts and notifies via Discord webhooks.

# Discord Link to [Skin Alert](https://discord.gg/uMHSyhzMNU)
- Skin Alert is a discord community I made that uses this program! Feel free to join :)
- For Skin Alert, the program is being ran off my Raspberry Pi - hopefully switching to a VPS
- You can contact me if any questions you might have in the Discord or Github

# Current CS2 Marketplaces Monitored
- csfloat
- skinbid

# Future Plans
- ~~Utilize docker~~
- Incorporate a default marketplace to compare discounts to (i.e. buff163)
- Incorporate more marketplaces
- Ability to interact with a Discord bot to create a private channel which will only update with wanted skins

# How to run the program
1. Copy the repo
2. Install the discord.py, requests and pytest module
   - pip install discord
   - pip install requests
   - pip install pytest
3. Create a .env file in root directory of project and implement the following inside:
   - ONE_TO_TEN_PERCENT_WH = "https://discord.com/api/webhooks/examplewebhook"
   - ELEVEN_TO_FIFTEEN_PERCENT_WH = "https://discord.com/api/webhooks/examplewebhook"
   - SIXTEEN_TO_TWENTY_PERCENT_WH = "https://discord.com/api/webhooks/examplewebhook
   - TWENTY_ONE_PLUS_PERCENT_WH = "https://discord.com/api/webhooks/examplewebhook"
   - STICKER_WH = "https://discord.com/api/webhooks/examplewebhook"
   - UPDATE_WH = "https://discord.com/api/webhooks/examplewebhook"
   - BOT_TOKEN = "BotTokenExample"
5. Make sure you're not on Python 3.12 as there's an issue with the requests package, I am currently on Python 3.11.1
6. run "python3 src/main.py" for main program
   - optional - if you have a bot you can  run "python3 src/DiscordBot.py" - useful for my case as the program is run off a Raspberry Pi, letting me know if program is running (if bot is online)
7. to run tests run "pytest"
