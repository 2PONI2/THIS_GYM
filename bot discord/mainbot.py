import discord
from gen import gen_pass
client = discord.Client( intents = discord.Intents.all() )

@client.event
async def on_ready(): #функ, отражающая готовность бота к работе
    print(f'вы зарегистрированы {client.user}')
    print('ваш пароль для входа', gen_pass(10) )
    
@client.event
async def on_message(message): #общение с юзером
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send('hi')
client.run('MTEzNTE1NDczNjA0ODM4NjA4OA.GV9Hak.U7-SiKVKg2vDPtWts_BVUrwHcGXbrxyK7FYDdI')
