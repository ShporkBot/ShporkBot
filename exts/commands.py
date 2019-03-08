import discord
from discord.ext import commands

class Команды(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    def __repr__(self):
        return "Команды"

    @commands.command()
    async def привет(self, ctx):
        await ctx.send(f"Привет, **{ctx.author.mention}**, я - **ShporkBot**")

    @commands.command(aliases=("ава", "аватарка"))
    async def аватар(self, ctx, target: discord.Member = None):

        target = target or ctx.author
    
        embed = discord.Embed(color=self.bot.color)
        embed.set_image(url=target.avatar_url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Команды(bot))
