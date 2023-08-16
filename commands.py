from main import *
from discord.utils import get
from discord_components import Select, SelectOption

# #   Cooldown
# #   На будущее
# #   @commands.cooldown(rate, per, type=<BucketType.default: 0>)

#   ON_MESSAGE
@client.event
async def on_message(message):
    if message.content.lower() == "привет":
        await message.channel.send(f'Приветствую вас, Чемпион! Чемпион людей.. Чемпион зверей')
    await client.process_commands(message)

#   Music
@client.command(pass_context = True) 
async def play(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

#   Help
@client.command(pass_context = True)
async def help(ctx):
    embed = discord.Embed( title = 'Ты просишь помощи?', colour = discord.Color.green() )
    embed.add_field(name="Помощи..", value="..не будет", inline=False)
    await ctx.send( embed = embed )


# #   Select Menu
# class Select(discord.ui.View):
#     @discord.ui.select(
#         placeholder = "Выбери игру",
#         options = [
#             discord.SelectOption(
#                 label="1",
#                 description="Первая игра"
#             ),
#             discord.SelectOption(
#                 label="2",
#                 description="Вторая игра"
#             ),
#             discord.SelectOption(
#                 label="3",
#                 description="Третья игра"
#             )
#         ]
#     )
#     async def select_callback(self, select, interaction):
#         await interaction.response.send_message(f"пипипупу")

#   Registration      
@client.command(pass_context = True, aliases = ['reg', 'register', 'рег', 'регистрация']) 
async def __register(ctx):
    embed = discord.Embed(title="Test Embed", colour=discord.Color.blue())
    await ctx.send(embed=embed, components=[
            Select(
                    placeholder="Test",
                    options=[
                            SelectOption(label=f"1", value="1"),
                            SelectOption(label=f"2", value="2") 
                    ]
            )
    ])
    interaction = await client.wait_for("select_option")
    await interaction.send(content=f"Ура!", embed = embed)


    # await ctx.send("ы", view = Select())

    # embed = discord.Embed(title="1", colour = discord.Color.green())

    # event = await self.client.wait_for("select_option")
    # label = event.component[0].label
