# Imports
import discord
from discord.ext import commands
import obsws_python as obs
import time
import os

# Function to reset the borders
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

# Function to reset the border lock sound
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
    
# Function for setting the questions for the game
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
    
# Function for resetting all question visibility
def reset_questions():
    cl = obs.ReqClient(host='localhost', 
                       port=4455, 
                       password='1cMYi1NmAdrIXsrh', 
                       timeout=30)
    for item_id in range(2, 38):
        cl.set_scene_item_enabled('Questions', item_id, False)
        cl.set_scene_item_enabled('Answers', item_id, False)

# Main function for the bot, utilizing /ready, /unready, 
# and /reset commands to control the borders and border lock sound. 
# ONLY EDIT THE USER UUIDS, USER NAMES, THE PLAYER DEFINITIONS, 
# OBS WEBSOCKET LOGIN, AND THE TOKEN.
def main():
    
    #################################### MAKE EDITS HERE ##############################################
    # Common Discord UUIDs for THE POND
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
    
    # Assign the user to a player
    player1 = cob
    player2 = gage
    player3 = nick
    player4 = andrew
    player5 = garrett
    player6 = chris
    player7 = matt
    player8 = justin
    
    admin = streamdeck

    # Load the bot token from the environment variable 'DISCORD_BOT_TOKEN'
    TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
    if TOKEN is None:
        print("Error: Discord bot token not provided.")
        return
    ####################################### STOP HERE #################################################

    # Connect to OBS websocket
    cl = obs.ReqClient(host='localhost', 
                       port=4455, 
                       password='1cMYi1NmAdrIXsrh', 
                       timeout=30)

    # Define intents
    intents = discord.Intents.default()
    intents.typing = True
    intents.presences = True
    intents.message_content = True

    # Create a bot instance with intents
    bot = commands.Bot(command_prefix='/', intents=intents)

    # Event: Bot is ready
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')
        
    # Command handling
    @bot.event
    async def on_message(message):
        # Ignore messages from the bot itself
        if message.author == bot.user:
            return
        # Allow messages from webhooks to be used as commands
        if message.webhook_id:
            ctx = await bot.get_context(message)
            await bot.invoke(ctx)
        await bot.process_commands(message)

    # Command: /ready
    # Usage:   /ready
    # Action:  Readies the user, enabling the border and border lock sound 
    #          linked by the user's UUID
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

    # Command: /unready
    # Usage:   /unready
    # Action:  Unreadies the user, disabling the border and border lock sound
    #          linked by the user's UUID
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
    
    # Command: /reset
    # Usage:   /reset
    # Action:  Resets the borders and border lock sound
    @bot.command()
    async def reset(ctx):
        user = ctx.author
        # Check if the user is an Admin
        if user.id == admin:
            # Reset the borders
            reset_borders()
            reset_lock_sound()
            # Reset the border lock sound
            reset_lock_sound()
        # If the user is not an Admin, send a message saying so
        else:
            response = f'Hey {ctx.author.mention}, you are not an Admin!'
            await ctx.send(response)
    
    # Command: /question /q
    # Usage:   /question <question> | /q <question>
    # Action:  Sets the question on the question board, switches the scene to
    #          the question board, resets the borders, and enables the question and answer text
    @bot.command()
    async def question(ctx, question):
        user = ctx.author
        # Check if the user is an Admin
        if user.id == admin:
            # Reset the borders
            reset_borders()
            reset_lock_sound()
            # Set the question
            set_questions(question)
        # If the user is not an Admin, send a message saying so
        else:
            response = f'Hey {ctx.author.mention}, you are not an Admin!'
            await ctx.send(response)
    @bot.command()
    async def q(ctx, question):
        user = ctx.author
        # Check if the user is an Admin
        if user.id == admin:
            # Reset the borders
            reset_borders()
            reset_lock_sound()
            # Set the question
            set_questions(question)
        # If the user is not an Admin, send a message saying so
        else:
            response = f'Hey {ctx.author.mention}, you are not an Admin!'
            await ctx.send(response)
    
    # Command: /clear
    # Usage:   /clear
    # Action:  Resets all question and answer visibility
    @bot.command()
    async def clear(ctx):
        user = ctx.author
        # Check if the user is Admin
        if user.id == admin:
            # Reset the questions
            reset_questions()
        # If the user is not an Admin, send a message saying so
        else:
            response = f'Hey {ctx.author.mention}, you are not an Admin!'
            await ctx.send(response)
    
    # Run the bot
    bot.run(TOKEN)

main()
