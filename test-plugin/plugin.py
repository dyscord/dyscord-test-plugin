from discord.ext.commands import command
from dyscord_plugin.plugin import DyscordPlugin


class Plugin(DyscordPlugin):
    def __init__(self, b):
        super().__init__(b)

    @command(pass_context=True)
    async def test_command(self, ctx):
        await ctx.channel.send("Test Command")
