from discord.ext.commands import command
from dyscord_plugin.plugin import DyscordPlugin


class Plugin(DyscordPlugin):
    def __init__(self, b):
        super().__init__(b)

    @command(pass_context=True)
    async def test_command(self, ctx):
        await ctx.channel.send("Test Command")

    @command(pass_context=True)
    async def store_test(self, ctx):
        s = ctx.storage
        try:
            val = s['test']
        except AttributeError:
            val = 'None'
        await ctx.channel.send("New val: " + str(val))

    @command(pass_context=True)
    async def set_store(self, ctx, val: str):
        s = ctx.storage
        s['test'] = val
        await ctx.channel.send("Set to: " + str(val))
