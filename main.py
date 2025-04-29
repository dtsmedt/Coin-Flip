import discord, os, asyncio, dotenv
from discord.ext import commands
from discord import app_commands

dotenv.load_dotenv()
GUILD_ID = discord.Object(id=(os.getenv("GUILD_ID")))

class Client(commands.Bot):

    async def setup_hook(self):
        for filename in os.listdir("cogs"):
            if filename.endswith(".py"):
                extension = f"cogs.{filename[:-3]}"
                try:
                    await self.load_extension(extension)
                    print(f"Loaded extension: {extension}")
                except Exception as e:
                    print(f"Failed to load extension {extension}: {e}")

    async def on_ready(self):
        try:
            synced = await self.tree.sync(guild=GUILD_ID)
            print(f"Synced {len(synced)} command(s) for guild {GUILD_ID.id}")
        except Exception as e:
            print(f"Error syncing commands: {e}")
        print(f'Logged on as {self.user}!')
    
intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="/", intents=intents)

client.run(os.getenv("DEV_TOKEN"))