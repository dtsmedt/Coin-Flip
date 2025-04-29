import discord, os, random, asyncio
from discord import app_commands
from discord.ext import commands

GUILD_ID = discord.Object(id=(os.getenv("GUILD_ID")))

class Flip(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name="flip_coin", description="flip a coin")
    @app_commands.guilds(GUILD_ID)

    async def flip_coin(self, interaction: discord.Interaction):
        
        gif = "https://media2.giphy.com/media/MOsuJf3qp3b1fQx2Iv/200w.gif?cid=6c09b952xu3cgu7rk8axbfv6cwq39loe9n96nrwhjmfnxrlo&ep=v1_stickers_search&rid=200w.gif&ct=s"
        embed = discord.Embed()
        embed.set_image(url=gif)
        await interaction.response.send_message(embed=embed)

        await asyncio.sleep(3)

        result = random.choice(['HEADS', 'TAILS'])

        await interaction.followup.send(result)

async def setup(bot):
    await bot.add_cog(Flip(bot))