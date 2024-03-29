﻿import discord
import requests

class TikTokBot(discord.Client):

    def __init__(self):
        super().__init__()

        self.api_key = MTE5NTM3ODY5NjI0NTIzMTc3Ng.Gw2Jea.oY5C1_oAZ6xrmboawFUz9qnpvTC4IAToyiFpGg
        self.users = []

    async def on_ready(self):
        print("Bot ready!")

    async def on_message(self, message):
        if message.content.startswith("!give_followers"):
            username = message.content.split(" ")[1]
            count = int(message.content.split(" ")[2])

            if username not in self.users:
                self.users.append(username)

            for i in range(count):
                user = random.choice(self.users)

                url = f"https://api.tiktok.com/v1/users/{user}/follow"
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                }

                response = requests.post(url, headers=headers)

                if response.status_code == 200:
                    print(f"Gave {count} followers to {username}")
                else:
                    print(f"Error giving {count} followers to {username}")


bot = TikTokBot()
bot.run()
