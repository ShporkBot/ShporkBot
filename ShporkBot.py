import discord
from discord.ext import commands

class ShporkBot(commands.Bot):
    def __init__(self):

        self.color = 0x26b73e
        self.token = open("token.ini", "r").read()

        super().__init__(command_prefix="!", case_insensitive=True)

    def run(self):

        for ext in ("exts.music", "exts.commands", "jishaku"):

            try:

                self.load_extension(ext)

            except Exception as exc:

                print(f"Произошла ошибка при загрузке модуля {ext}: {exc}")

            else:

                print(f"Модуль {ext} успешно загружен!")

        super().run(self.token)

    async def on_ready(self):

        print("Готов!")  

        await self.change_presence(
            status=discord.Status.dnd,
            activity=discord.Activity(
                type=discord.ActivityType.listening, 
                name="и поёт песенки"
            )
        )

if __name__ == "__main__":
    ShporkBot().run()
