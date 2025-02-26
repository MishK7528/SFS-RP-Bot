import discord
from discord.ext import commands
from discord import Option



class CogHelp(commands.Cog): 

    
    def __init__(self, bot):
        self.bot = bot
       

    

    @discord.slash_command(
        name="help",
        description="Affichage des commandes"
    )
    async def help(self,ctx):
       
        embed = discord.Embed(color=0x00ff00, title="Page d'aide sur les commandes")
        embed.set_thumbnail(url="https://www.crushpixel.com/big-static14/preview4/planet-space-with-stars-shiny-1674010.jpg")
        embed.add_field(name="**`/mission <planete ou satellite>`**", value="Permets de calculer vos couts de mission vers une planete ou un satellite ainsi que vos bénefices facilement via un questionnaire.",inline = False)
        embed.add_field(name="**`/satellite <planete>`**", value="Affiche les satellite de la planete spécifié ainsi que leur couts de mission.",inline = False)
        embed.add_field(name="**`/prix <planete>`**",value="Donne la table des couts pour le type et les objectif de mission pour la planete spécifié.",inline = False)
        await ctx.respond(embed=embed)


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(CogHelp(bot))
