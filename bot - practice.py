# Imports
import discord
from discord.ext import commands
import obsws_python as obs
import time
import os

# Function to 
def reset_borders():
    cl = obs.ReqClient(host='localhost', 
                       port=4455, 
                       password='1cMYi1NmAdrIXsrh', 
                       timeout=30)
    cl.set_scene_item_enabled('C1.READYBORDER', 1, False)
    cl.set_scene_item_enabled('C2.READYBORDER', 1, False)
    cl.set_scene_item_enabled('C3.READYBORDER', 1, False)
    cl.set_scene_item_enabled('C4.READYBORDER', 1, False)
    cl.set_scene_item_enabled('C5.READYBORDER', 1, False)
    cl.set_scene_item_enabled('C6.READYBORDER', 1, False)
    cl.set_scene_item_enabled('C7.READYBORDER', 1, False)
    cl.set_scene_item_enabled('C8.READYBORDER', 1, False)

# Function to 
def reset_lock_sound():
    cl = obs.ReqClient(host='localhost', 
                       port=4455, 
                       password='1cMYi1NmAdrIXsrh', 
                       timeout=30)
    cl.set_scene_item_enabled('C1.READYBORDER', 2, False)
    cl.set_scene_item_enabled('C2.READYBORDER', 3, False)
    cl.set_scene_item_enabled('C3.READYBORDER', 3, False)
    cl.set_scene_item_enabled('C4.READYBORDER', 3, False)
    cl.set_scene_item_enabled('C5.READYBORDER', 3, False)
    cl.set_scene_item_enabled('C6.READYBORDER', 3, False)
    cl.set_scene_item_enabled('C7.READYBORDER', 3, False)
    cl.set_scene_item_enabled('C8.READYBORDER', 3, False)
    
# Function for 
def set_questions(question):
    cl = obs.ReqClient(host='localhost', 
                       port=4455, 
                       password='1cMYi1NmAdrIXsrh', 
                       timeout=30)
    question_mapping = {
        "k-1": (37, 37),
        "k-2": (36, 36),
        "k-3": (35, 35),
        "1-1": (34, 34),
        "1-2": (33, 33),
        "2-1": (32, 32),
        "2-2": (31, 31),
        "3-1": (30, 30),
        "3-2": (29, 29),
        "3-3": (28, 28),
        "4-1": (27, 27),
        "4-2": (26, 26),
        "4-3": (25, 25),
        "5-1": (24, 24),
        "5-2": (23, 23),
        "6-1": (22, 22),
        "6-2": (21, 21),
        "6-3": (20, 20),
        "ec1": (19, 19),
        "7-1": (18, 18),
        "7-2": (17, 17),
        "7-3": (16, 16),
        "8-1": (15, 15),
        "8-2": (14, 14),
        "8-3": (13, 13),
        "9-1": (12, 12),
        "9-2": (11, 11),
        "9-3": (10, 10),
        "10-1": (9, 9),
        "10-2": (8, 8),
        "10-3": (7, 7),
        "11-1": (6, 6),
        "11-2": (5, 5),
        "11-3": (4, 4),
        "12-1": (3, 3),
        "12-2": (2, 2)
    }
    if question in question_mapping:
        question_item, answer_item = question_mapping[question]
    
        for item_id in range(37, 1, -1):
            cl.set_scene_item_enabled('Questions', item_id, False)
            cl.set_scene_item_enabled('Answers', item_id, False)

        cl.set_current_program_scene('Question Board')
        cl.set_scene_item_enabled('Questions', question_item, True)
        time.sleep(1)
        cl.set_scene_item_enabled('Answers', answer_item, True)
    else:
        print("Question ID not recognized.")
    
# Function for 
def reset_questions():
    cl = obs.ReqClient(host='localhost', 
                       port=4455, 
                       password='1cMYi1NmAdrIXsrh', 
                       timeout=30)
    for item_id in range(2, 38):
        cl.set_scene_item_enabled('Questions', item_id, False)
        cl.set_scene_item_enabled('Answers', item_id, False)

# Main function for
#
def main():
    
    #################################### MAKE EDITS HERE ##############################################
    # What are these?
    # 
    broulf = 208429040845979648
    broulfy = 656349646742093825
    justin = 379320226451292161
    andrew = 309544834157379607
    garrett = 568527040408453121
    gage = 339126453029306369
    chris = 507619665871110144
    cob = 278342746564067339
    tylerf = 280838240670318602
    tylerb = 323976710905266176
    matt = 260479483264499712
    luke = 402191595874680833
    jonathon = 209495678446075904
    jacob = 143158388128350208
    jordan = 112348486581620736
    nick = 554832324387143683
    chase = 399329824931446796
    matt = 260479483264499712
    streamdeck = 1142109536300302377
    
    # What's going on here?
    # 
    player1 = cob
    player2 = gage
    player3 = nick
    player4 = andrew
    player5 = garrett
    player6 = chris
    player7 = matt
    player8 = justin
    
    admin = streamdeck

    # Explain this:
    #
    TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
    if TOKEN is None:
        print("Error: Discord bot token not provided.")
        return
    ####################################### STOP HERE #################################################

    # How does this work?
    #
    cl = obs.ReqClient(host='localhost', 
                       port=4455, 
                       password='1cMYi1NmAdrIXsrh', 
                       timeout=30)

    # Define intents
    # Internal Discord stuff, ignore
    intents = discord.Intents.default()
    intents.typing = True
    intents.presences = True
    intents.message_content = True

    # Explain this:
    #
    bot = commands.Bot(command_prefix='/', intents=intents)

    # What does this event actually do?
    #
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')
        
    # What does this handle?
    #
    @bot.event
    async def on_message(message):
        
        # Why is this important?
        #
        if message.author == bot.user:
            return
        
        # This is even more important, try to explain this:
        #
        if message.webhook_id:
            ctx = await bot.get_context(message)
            await bot.invoke(ctx)
        await bot.process_commands(message)

    # Command: 
    # Usage:   
    # Action:  
    player_ready_borders = {
    player1: ('C1.READYBORDER', 1, 2),
    player2: ('C2.READYBORDER', 1, 3),
    player3: ('C3.READYBORDER', 1, 3),
    player4: ('C4.READYBORDER', 1, 3),
    player5: ('C5.READYBORDER', 1, 3),
    player6: ('C6.READYBORDER', 1, 3),
    player7: ('C7.READYBORDER', 1, 3),
    player8: ('C8.READYBORDER', 1, 3)
    }

    @bot.command()
    async def ready(ctx):
        user = ctx.author
        response = f'Hey {user.mention}, you are ready!'

        if user.id in player_ready_borders:
            await ctx.send(response)
            border, *items = player_ready_borders[user.id]
            for item in items:
                cl.set_scene_item_enabled(border, item, True)
        else:
            response = f'Hey {user.mention}, you are not a player!'
            await ctx.send(response)

    # Command: 
    # Usage:   
    # Action:  
    @bot.command()
    async def unready(ctx):
        user = ctx.author
        response = f'Hey {user.mention}, you have been unreadied!'
        
        if user.id in player_ready_borders:
            await ctx.send(response)
            border, *items = player_ready_borders[user.id]
            cl.set_scene_item_enabled(border, items[0], False)
            cl.set_scene_item_enabled(border, items[1], False)
        else:
            response = f'Hey {user.mention}, you are not a player!'
            await ctx.send(response)
    
    # Command: 
    # Usage:   
    # Action:  
    @bot.command()
    async def reset(ctx):
        user = ctx.author
        # Explain:
        #
        if user.id == admin:
            # 
            reset_borders()
            reset_lock_sound()
            # 
            reset_lock_sound()
        # What does this do?
        #
        else:
            response = f'Hey {ctx.author.mention}, you are not an Admin!'
            await ctx.send(response)
    
    # Command: 
    # Usage:   
    # Action:  
    @bot.command()
    async def question(ctx, question):
        user = ctx.author
        # Explain:
        #
        if user.id == admin:
            # 
            reset_borders()
            reset_lock_sound()
            # 
            set_questions(question)
        # What does this do?
        #
        else:
            response = f'Hey {ctx.author.mention}, you are not an Admin!'
            await ctx.send(response)
    @bot.command()
    async def q(ctx, question):
        user = ctx.author
        # Explain:
        #
        if user.id == admin:
            # 
            reset_borders()
            reset_lock_sound()
            # 
            set_questions(question)
        # What does this do?
        #
        else:
            response = f'Hey {ctx.author.mention}, you are not an Admin!'
            await ctx.send(response)
    
    # Command: 
    # Usage:   
    # Action:  
    @bot.command()
    async def clear(ctx):
        user = ctx.author
        # Explain:
        #
        if user.id == admin:
            # 
            reset_questions()
        # What does this do?
        #
        else:
            response = f'Hey {ctx.author.mention}, you are not an Admin!'
            await ctx.send(response)
    
    # Interesting, might be worth explaining:
    #
    bot.run(TOKEN)

main()
