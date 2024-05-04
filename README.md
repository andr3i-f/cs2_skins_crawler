# cs2_skins_crawler
Monitors CS2 skin marketplaces for good discounts and notifies via Discord webhooks.

# Discord Link to [Skin Alert](https://discord.gg/uMHSyhzMNU)
- Skin Alert is a discord community I made that uses this program! Feel free to join :)
- For Skin Alert, the program is being ran off Docker
- You can contact me if any questions you might have in the Discord or Github

# Current CS2 Marketplaces Monitored
- csfloat
- skinbid

# Future Plans
- Incorporate a default marketplace to compare discounts to (i.e. buff163)
- Incorporate more marketplaces
- Ability to interact with a Discord bot to create a private channel which will only update with wanted skins

# How to run the program
Due to issues in Python 3.12, Python 3.11 is recommended. Therefore, the app is Dockerized and public. Running the application has never been easier now that Docker is used:
1. Create `.env` file in working directory, and include the following:
   - Required
      - ONE_TO_TEN_WH="https://discord.com/api/webhooks/examplewebhook"
      - ELEVEN_TO_FIFTEEN_WH="https://discord.com/api/webhooks/examplewebhook"
      - SIXTEEN_TO_TWENTY_WH="https://discord.com/api/webhooks/examplewebhook
      - TWENTYONE_PLUS_WH="https://discord.com/api/webhooks/examplewebhook"
      - STICKER_WH="https://discord.com/api/webhooks/examplewebhook"
      - UPDATE_WH="https://discord.com/api/webhooks/examplewebhook"
   - Optional for bot support. If not using bot support, simply define the var as an empty string.
      - BOT_TOKEN="bot_token_example"
2. To run program

Running the program will automatically pull from Docker Hub as long as the image name is specified correctly as `cs2_skins_crawler`:

`docker run -d --env-file .env --name cs2_skins_crawler_container simiflorea/cs2_skins_crawler`

# Tests
To run tests, run a removable, quick container but specify pytest as the main command.

`docker run --rm simiflorea/cs2_skins_crawler pytest`
