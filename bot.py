import discord
from discord.ext import commands
from shapes_api import ask_shapes

class ChatBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ask")
    async def ask(self, ctx, *, question: str):
        """Ask the chatbot a question."""
        await ctx.trigger_typing()
        try:
            reply = ask_shapes(question, str(ctx.author.id), str(ctx.channel.id))
            await ctx.reply(reply)
        except Exception as e:
            await ctx.reply(f"Error: {str(e)}")

def setup(bot):
    bot.add_cog(ChatBot(bot))
