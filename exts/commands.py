import discord
from discord.ext import commands

class Команды(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.shpork_vid = "https://www.youtube.com/watch?v=0xv688_SImw"

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
        
    @commands.command(aliases=("шперк", "шпірк"))
    async def шпорк(self, ctx):
        
        await ctx.send(
            self.shpork_vid
        )
        
        
    @commands.command(name="на чём")
    async def начём(self, ctx, member: discord.Member = None):
        
        """ Что сейчас использует человек? """
        
        member = member or ctx.author
        
        if member.is_on_mobile():

            return await ctx.send(
                f"Шпорк думать, что **{member.name}** сейчас использует :iphone:"
            )
        
        await ctx.send(
            f"Шпорк думать, что **{member.name}** сейчас использует :computer:"
        )

def setup(bot):
    bot.add_cog(Команды(bot))
