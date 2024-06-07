
from email import message
import discord
from discord.ui import Modal, InputText, View, button
from discord.ext.pages import Page, Paginator, PageGroup
import os


from dotenv import load_dotenv
load_dotenv()




bot = discord.Bot(debug_guilds=[int(os.getenv("GUILD_ID"))])




pages = [
    PageGroup(
        pages=[
            Page(content="1"),
            Page(content="2"),
        ],
        label="Group 1"
    ),
    PageGroup(
        pages=[
            Page(content="3"),
            Page(content="4"),
            Page(content="5"),
        ],
        label="Group 2"
    )
]   

class SurveyModal(Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, title="Подать заявку в семью Ant")

        self.add_item(InputText(
            label="Ник|Статик на Los Angeles|Имя и Возраст",
            placeholder="Пример: Sizzy Ant | 300 | Алексей 19 лет",
            min_length=1,
            max_length=30
        ))

        self.add_item(InputText(
            label="Опыт RP серверов | Ежедневный Онлайн",
            placeholder="Как узнали о нас?",
            min_length=1,
            max_length=100
        ))

        self.add_item(InputText(
            label="В каких семьях состояли?",
            placeholder="По какой причине покинули?",
            min_length=1,
            max_length=100
        ))

        self.add_item(InputText(
            label="Почему выбрали именно нашу фаму?",
            placeholder="Какую пользу сможете принести нашей семье?",
            min_length=1,
            max_length=400
        ))

        self.add_item(InputText(
            style=discord.InputTextStyle.multiline,
            label="Как бы вы оценили свой навык стрельбы?",
            placeholder="Видео(откат с любого мероприятия, файта, крайний случай - ГГ)Без отката заявка будет отклонена!",
            min_length=1,
            max_length=400
        ))

    async def callback(self, intercation: discord.Interaction):
            # name = self.children[0].value
            # exp = self.children[1].value
            # fams = self.children[2].value
            # benefit = self.children[3].value
            # fight = self.children[4].value

            name, exp, fams, benefit, fight = map(lambda x: x.value, self.children)
            
            await intercation.response.send_message(f"**Ваш ник | Статик | Имя:** ```{name}``` **Ваш опыт и онлайн:** ```{exp}``` **В каких семьях вы были:** ```{fams}``` **Почему именно наша семья:** ```{benefit}``` **Ваши навыки стрельбы:** ```{fight}```")
  

        

# @bot.command()
# async def showcase(ctx: discord.ApplicationContext):
#      pagesManager = Paginator(
#           pages=pages,
#           show_disabled=False,
#           show_menu=True,

#      )
#      await pagesManager.respond(
#           ctx.interaction,
#           target=bot.get_channel(1248728288470368418)
#    )

class MyView(View):
            
        @button(label="Подать заявку в семью", style=discord.ButtonStyle.green, emoji="📋")
        async def callback(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.send_modal(SurveyModal())
        
@bot.command()
async def application(ctx: discord.ApplicationContext):
     await ctx.respond("https://tenor.com/view/%D1%81-%D0%B4%D0%BD%D0%B5%D0%BC-%D1%80%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F-gif-1024174821354942547", view=MyView())
async def showcase(ctx: discord.ApplicationContext):
            pagesManager = Paginator(
                pages=pages,
                show_disabled=False,
                show_menu=True,
            )

            await pagesManager.respond(
            ctx.interaction,
            target=bot.get_channel(1248728288470368418)
        )         

     
       
# @bot.command()
# async def survey(ctx: discord.ApplicationContext):
#     await ctx.send_modal(SurveyModal())

if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))
