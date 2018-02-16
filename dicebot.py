#!/usr/bin/env python3

"""
Dice roller bot for discord, most i saw where far to heavy (or
node..), I just for the moment want roll20 like dice rolling
"""
import discord
import asyncio
import roller

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Invite: https://discordapp.com/oauth2/authorize?client_id={}&scope=bot'.format(client.user.id))
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!r') or message.content.startswith('/r'): # TODO: Limit to !r and !roll
        log(message.channel.name, message.author.name, message.content)
        tmp = await client.send_message(message.channel, 'Rolling...')
        # Roll the dices
        dice_expression = message.content[message.content.find(' ')+1:].strip()
        try:
            result = roller.roll(dice_expression)
            response = 'Rolled: ' + result
        except:
            response = "Sorry I don't understand that roll '{}'".format(dice_expression)

        log(message.channel.name, 'dicebot', response)
        await client.edit_message(tmp, response)
    elif message.content in ('!help', '/help'):
        await client.send_message(message.channel, 'try `!r 1d6+1d2+2`')

def get_token():
    with open('token', 'r') as f:
        return f.readline().strip()

def log(where, who, message):
    """Make pretty later"""
    print("[{}] {}: {}".format(where, who, message))

client.run(get_token())
