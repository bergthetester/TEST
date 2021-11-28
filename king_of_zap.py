import discord
import pyautogui
from time import sleep

TOKEN = 'ODk2NTM5MDc4NDc1MDAxODk3.YWIlFQ.Fu2V_IzG1VKJub5eOBFL2PBXHlo'

client = discord.Client()

@client.event

async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dem_channel.send(f'Hi {member.name}!')


def spam(msg, maxMsg):

    count = 0
    count_3 = count

    while count != maxMsg:
        count += 1
        print('Message: ', str(count))
        print(str(count))
        pyautogui.write(msg)
        pyautogui.sleep(0.3)
        pyautogui.press('enter')
        #await message.channel.send('XXXDDD')

        #if count == 100:
            #sleep(8)

"""def bot_spam(msg, MaxMsg):

    count_2 = 0
    while count_2 != MaxMsg:
        count_2 += 1
        print('Message: ', str(count_2))
        print(str(count_2))
        await message.channel.send(msg, 100)"""

@client.event

async def on_message(message):

    username = str(message.author).split('#')[0]
    userMessage = str(message.content).lower()
    channel = str(message.channel.name)

    #if message.author == client.user:
     #   return


    if message.channel.name == 'caos':

        if userMessage == '&spamar':

            #spam('@everyone', 100)

            #spam('hehe ', 10)

            count_3 = 0

            while count_3 != 300:

                count_3 += 1
                #await message.channel.send('<@!748545167719399465>')  # ---> alex
                await message.channel.send('<@!612810418825723925>') # tokito


            #await message.channel.send('XD')
            #await message.channel.send('@everyone')
        #if userMessage

    if message.channel.name == 'HEHE':
        spam('@KRONUZBR#7429 ', 100)

        await message.channel.send('XD')

client.run(TOKEN)


"""

 
 @Sub Dono
 @Sub Dono
 @Sub Dono
 @Sub Dono
"""
#
