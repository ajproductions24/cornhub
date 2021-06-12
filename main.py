#Importing Libraries
import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
import random
from keep_alive import keep_alive

#Bot Setup
client = commands.Bot(command_prefix='c!', help_command=None)
discord_token = 'DISCORD_TOKEN'

#Defining Images
CORN = ["https://www.thegunnysack.com/wp-content/uploads/2018/06/Boiled-Corn-On-The-Cob-Recipe-720x540.jpg","https://www.jessicagavin.com/wp-content/uploads/2019/05/how-to-cook-corn-on-the-cob-8-1200.jpg","https://www.simplyhappyfoodie.com/wp-content/uploads/2018/04/instant-pot-corn-on-the-cob-1-500x500.jpg","https://www.dudafresh.com/hubfs/images-2017/p-main-corn.png","https://www.simplyrecipes.com/thmb/SeFw2HWwLCOznSTMTsdCWuydQTo=/1777x1333/smart/filters:no_upscale()/__opt__aboutcom__coeus__resources__content_migration__simply_recipes__uploads__2019__07__Grilled-Corn-on-the-Cob-LEAD-3-2473cd41fbce489fa6d08b74a4334562.jpg"]

BIG_CORN = ["http://www.exactrix.com/Broadcast_09_08_2016/image002.jpg","https://i.pinimg.com/originals/87/4f/8b/874f8bbb6ec814b320dcd8f26e00005d.jpg","https://steamuserimages-a.akamaihd.net/ugc/949600067406158799/51D460C6FED45D2DBBA75467FE62A7D552E9012D/"]

THE_FARMER = ["https://i.ytimg.com/vi/pKl8AOvs6Ts/hqdefault.jpg","https://i.pinimg.com/originals/da/1d/8c/da1d8cf3caf538324e35d9c2ca2779b1.jpg","https://st2.depositphotos.com/3901127/6576/i/950/depositphotos_65762897-stock-photo-funny-farmer-jokes-with-his.jpg","https://www.agdaily.com/wp-content/uploads/2018/06/bg-farmer_laughing-001.jpg","https://i.ytimg.com/vi/JLZvijnwmDM/maxresdefault.jpg","https://media.istockphoto.com/photos/hillbilly-nerd-picture-id184851348?k=6&m=184851348&s=612x612&w=0&h=vGBUNRPbCgNxw3HFoIpnrIMko_C7U6-eS4hJQXoX9Ak=","https://media.istockphoto.com/photos/bored-farmer-picture-id135157996?k=6&m=135157996&s=612x612&w=0&h=zQuOxmrmqokVSGArGaJ1EsuVSAARc3u1ua-HJUgZ1gg=","https://www.cybersalt.org/images/funnypictures/h/harvestanxiety.jpg"]

BUTTER = ["https://i0.wp.com/cdn-prod.medicalnewstoday.com/content/images/articles/321/321990/close-up-of-block-of-butter-being-sliced-may-raise-cholesterol.jpg?w=1155&h=1541","https://media.istockphoto.com/photos/butter-picture-id179875636?k=6&m=179875636&s=612x612&w=0&h=U6KGIvmBwcYxCNYGMrvKvgNumIzgtUl0mVDJlduIW1k=","https://lh3.googleusercontent.com/proxy/rDuxwRjDVlxf1k5upakCLOV4jYMinuJ6klSeV2s1MZ9j2k4OnGnKFwSRehN1wypsv8pu_K3l5Vf1S2HvLZYH7oGdP92Xr71x9rWmlpQCSlACeP8yFREcQIBJruBe","https://assets.bonappetit.com/photos/5cc0d0069e22ba4d590733cf/4:3/w_2775,h_2081,c_limit/HLY-Cannabis-Butter.jpg","https://static.onecms.io/wp-content/uploads/sites/43/2020/05/14/butter-on-blue-cloth-photo-by-littleny-GettyImages-506715010-resized.jpg"]

MEGA_CORN = ["https://www.lkbaits.com/images/LK%20Baits%20MEGA%20CORN%20Hungary%20Honey%20-%20Ob%C5%99%C3%AD%20kuku%C5%99ice%20Ma%C4%8Farsk%C3%BD%20med%20220ml.png","https://www.hiki.eu/pub/media/catalog/product/cache/be723d353c623cbb299d4ddec2f2b6b4/0/1/015-1754000.jpeg","https://i.ytimg.com/vi/gNhqAl174n4/maxresdefault.jpg","http://carpshop-vuksic.com/1976-large_default/mega-corn-carptec-1-l.jpg"]

BUTTER_CORN = ["https://onepotrecipes.com/wp-content/uploads/2018/10/One-Pot-Boiled-Corn-on-The-Cob-Recipe-With-Milk-and-Butter.jpg","https://izzycooking.com/wp-content/uploads/2019/10/Sous-Vide-Corn-with-Butter.jpg","https://photos.bigoven.com/recipe/hero/milkboiledcornonthecob-bac228.jpg","https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F1036447.jpg&w=380&h=254&c=sc&poi=face&q=85","https://i.pinimg.com/originals/32/17/17/3217179439ae667cda1bf6a2a7c263f2.jpg","https://www.katiescucina.com/wp-content/uploads/2016/06/Slow-cooker-corn-on-the-cob-5.jpg"]

BIG_STOCK = ["https://static2.bigstockphoto.com/2/5/3/large1500/352458521.jpg","https://c8.alamy.com/comp/2A5370H/fresh-corn-ears-with-leaves-two-big-ripe-mature-yellow-cob-2A5370H.jpg","https://static2.bigstockphoto.com/0/9/3/large1500/390073237.jpg","https://static1.bigstockphoto.com/2/9/3/large1500/392930519.jpg","https://cdn.apartmenttherapy.info/image/upload/f_jpg,q_auto:eco,c_fill,g_auto,w_1500,ar_1:1/k%2Farchive%2Fbfe23c089acf07b6dab335d6aa1e745e2809cccd"]

MALE_CORN = ["https://cdn.ebaumsworld.com/mediaFiles/picture/252061/960137.jpg","https://www.kanojotoys.com/img/ligre/sweet-corn-cob-kernel-cock-dildo-sex-toy-3.jpg","https://previews.123rf.com/images/chaowalit/chaowalit1308/chaowalit130800012/21979887-black-corn-shape-of-a-penis.jpg",""]

#Command 1
@client.command(name = 'commands')
async def commands(ctx):
    embed=discord.Embed(title="Commands", description="The commands for the **CornHub Bot** are as follows: ``c!corn`` ``c!bigcorn`` ``c!thefarmer`` ``c!butter`` ``c!megacorn`` ``c!buttercorn`` ``c!bigstock`` ``c!malecorn``", color=0xffa100)
    await ctx.send(embed=embed, components = [Button(style=2, label="Delete")]) 
    res = await client.wait_for("button_click")
    await res.message.delete()    

#Command 2
@client.command(name = 'help')
async def help(ctx):
  ctx.message.delete
  embed=discord.Embed(title="CornHub", url="http://corn-hub.blogspot.com/", description="Looks like you need help. Use the buttons down below to navigate to the corresponding areas. If you have any questions, please DM **AJ.Productions#1815**. Thank you.", color=0xffa100)
  await ctx.send(embed=embed, 
          components = [
              [
                  Button(style=2, label="Commands"),
                  Button(style=5, label="Invite", url="https://discord.com/api/oauth2/authorize?client_id=851938911437717595&permissions=27648&scope=bot")
              ]
        ]   
)
  embed=discord.Embed(title="Commands", description="The commands for the **CornHub Bot** are as follows: ``c!corn`` ``c!bigcorn`` ``c!thefarmer`` ``c!butter`` ``c!megacorn`` ``c!buttercorn`` ``c!bigstock`` ``c!malecorn``", color=0xffa100)
  res = await client.wait_for("button_click")
  await ctx.send(embed=embed, components = [Button(style=2, label="Delete")])  
  res = await client.wait_for("button_click")
  await res.message.delete() 

#Corn Command
@client.command(name = 'corn')
async def corn(ctx):
  await ctx.send(random.choice(CORN))

#Big Corn Command
@client.command(name = 'bigcorn')
async def bigcorn(ctx):
  await ctx.send(random.choice(BIG_CORN))

#The Farmer Command
@client.command(name = 'thefarmer')
async def thefarmer(ctx):
  await ctx.send(random.choice(THE_FARMER))

#Butter Command
@client.command(name = 'butter')
async def butter(ctx):
  await ctx.send(random.choice(BUTTER))

#Mega Corn Command
@client.command(name = 'megacorn')
async def megacorn(ctx):
  await ctx.send(random.choice(MEGA_CORN))

#Butter Corn Command
@client.command(name = 'buttercorn')
async def buttercorn(ctx):
  await ctx.send(random.choice(BUTTER_CORN))

#Big Stock Command
@client.command(name = 'bigstock')
async def bigstock(ctx):
  await ctx.send(random.choice(BIG_STOCK))

#Male Corn Command
@client.command(name = 'malecorn')
async def malecorn(ctx):
  await ctx.send(random.choice(MALE_CORN))  

#Bot Startup
@client.event
async def on_ready():
   DiscordComponents(client)
   print("The bot is ready!")
   await client.change_presence(activity=discord.Game(name="c!help"))

#On Guild Join
@client.event
async def on_guild_join(guild):
  print("The bot has been added to a server!")
  channels = guild.text_channels
  channel = channels[0]
  embed=discord.Embed(title="CornHub", url="http://corn-hub.blogspot.com/", description="**Thank you** for adding the **CornHub Bot** to your server. Use the buttons down below to navigate to the corresponding areas. If you have any questions or concerns, please DM **AJ.Productions#1815**.", color=0xffa100)
  await channel.send(embed=embed, 
        components = [
            [       
                Button(style=2, label="Commands"),
                Button(style=5, label="Invite", url="https://discord.com/api/oauth2/authorize?client_id=851938911437717595&permissions=27648&scope=bot")
            ]
      ]      
)
  embed=discord.Embed(title="Commands", description="The commands for the **CornHub Bot** are as follows: ``c!corn`` ``c!bigcorn`` ``c!thefarmer`` ``c!butter`` ``c!megacorn`` ``c!buttercorn`` ``c!bigstock`` ``c!malecorn``", color=0xffa100)
  res = await client.wait_for("button_click")
  await channel.send(embed=embed, components = [Button(style=2, label="Delete")])  
  res = await client.wait_for("button_click")
  await res.message.delete() 

@client.event
async def on_button_click(interaction):
    if interaction.responded:
        return
    await interaction.respond(type = 6)
  

#Start
keep_alive()
client.run(discord_token)

