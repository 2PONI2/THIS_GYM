# Так можно прочитать весь файл
#f = open('text.txt', 'r', encoding='utf-8')
#text = f.read()
#print(text)
#f.close()

# А так перезапишем файл полностью
#f = open('text.txt', 'w', encoding='utf-8')
#text = 'Новый текст'
#f.write(text)
#f.close()

# А вот сокращенная версия
#with open('text.txt', 'r', encoding='utf-8') as f:
    #print(f.read())
import discord
from discord.ext import commands
import os
import random
import requests


bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
@bot.command()
async def animals(ctx):
    img_name = random.choice(os.listdir('imga'))
    with open(f'imga/{img_name}', 'rb') as f:
        
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
    
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
bot.run('MTEzNTE1NDczNjA0ODM4NjA4OA.GlkirZ.w54x7kMgFe62pYawGmCYoxqE9aURXMqAkndp2U')












