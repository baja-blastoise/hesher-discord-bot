import os
import discord
from dotenv import load_dotenv
from malookup import BANDLOOKUP, DISCOGLOOKUP, MEMBERLOOKUP, SIMILAR, ARTISTLOOKUP, ALBUMLOOKUP, RANDOM
import time
from math import ceil

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

bprint = True
char_lim = 2000

# function to limit message return to 2000 characters


def msg_lim(msg_text, char_lim):
    chunks = []
    if len(msg_text) > char_lim:
        start = 0
        num_chunks = ceil(len(msg_text) / char_lim)
        for i in range(0, num_chunks):
            end = start + char_lim
            if end > len(msg_text):
                end = len(msg_text)
            split_pos = msg_text[start:end].rfind('\n')
            chunks.append(msg_text[start:(start + split_pos)])
            start = start + split_pos
    else:
        chunks.append(msg_text)
    return chunks


# try to read in help message
try:
    helpmsg = 1
    with open('help.txt') as f:
        lines = f.read()
except Exception as e:
    helpmsg = 0
    print('Could not find help.txt in this folder.')
    print(e)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return  # don't respond to messages from yourself

    # help command - text should be read in on startup
    if message.content.startswith('$help'):
        print('$help command found')
        print(message.content)
        if helpmsg == 1:
            await message.channel.send(lines)
        else:
            await message.channel.send('no help.txt found')

    # returns basic band info
    if message.content.startswith('$band '):
        print('$band command found')
        text = message.content
        print(message.content)
        t0 = time.time()
        # if disambiguation number
        if text.find('|') != -1:
            text = text.split('|')
            bandnumber = text[-1]
            text = text[0].split('$band')
            bandname = text[-1].strip()
            print('Band name: ' + bandname)
            print('Band number: ' + str(bandnumber))
            results = BANDLOOKUP(bandname, bandnumber, bprint)
            output = msg_lim(results, char_lim)
            for i in range(0, len(output)):
                msg = '```' + output[i] + '```'
                await message.channel.send(msg)
        else:
            t = text.split('$band')
            bandname = t[-1].strip()
            print('Band name: ' + bandname)
            results = BANDLOOKUP(bandname, 0, bprint)
            output = msg_lim(results, char_lim)
            for i in range(0, len(output)):
                msg = '```' + output[i] + '```'
                await message.channel.send(msg)
        t1 = time.time()
        print(t1-t0)

    # lookup discography
    if message.content.startswith('$discog '):
        print('$discog command found')
        text = message.content
        print(text)
        t0 = time.time()
        # get discog type first
        if text.find(',') != -1:
            disctype = text.split(',')[-1].strip()
            text = text.split(',')[0]
        else:
            disctype = 'main'
        # disambiguation
        if text.find('|') != -1:
            text = text.split('|')
            bandnumber = text[-1]
            text = text[0].split('$discog')
            bandname = text[-1].strip()
            print('Band name: ' + bandname)
            print('Band number: ' + str(bandnumber))
            print('Type: ' + disctype)
            results = DISCOGLOOKUP(bandname, bandnumber, disctype, bprint)
            output = msg_lim(results, char_lim)
            for i in range(0, len(output)):
                msg = '```' + output[i] + '```'
                await message.channel.send(msg)
        else:
            t = text.split('$discog')
            bandname = t[-1].strip()
            print('Band name: ' + bandname)
            print('Type: ' + disctype)
            results = DISCOGLOOKUP(bandname, 0, disctype, bprint)
            output = msg_lim(results, char_lim)
            for i in range(0, len(output)):
                msg = '```' + output[i] + '```'
                await message.channel.send(msg)
        t1 = time.time()
        print(t1-t0)

    # look up band members
    if message.content.startswith('$members '):
        print('$members command found')
        text = message.content
        print(text)
        t0 = time.time()
        # get member type - default to either Active or last known
        if text.find(',') != -1:
            membertype = text.split(',')[-1].strip()
            text = text.split(',')[0]
        else:
            membertype = 'Current'
        # handles band numbers for disambiguation
        if text.find('|') != -1:
            text = text.split('|')
            bandnumber = text[-1]
            text = text[0].split('$members')
            bandname = text[-1].strip()
            print('Band name: ' + bandname)
            print('Band number: ' + str(bandnumber))
            print('Type: ' + membertype)
            results = MEMBERLOOKUP(bandname, bandnumber, membertype, bprint)
            output = msg_lim(results, char_lim)
            for i in range(0, len(output)):
                msg = '```' + output[i] + '```'
                await message.channel.send(msg)
        else:
            t = text.split('$members')
            bandname = t[-1].strip()
            print('Band name: ' + bandname)
            print('Type: ' + membertype)
            results = MEMBERLOOKUP(bandname, 0, membertype, bprint)
            output = msg_lim(results, char_lim)
            for i in range(0, len(output)):
                msg = '```' + output[i] + '```'
                await message.channel.send(msg)
        t1 = time.time()
        print(t1-t0)

    # look up similar bands
    if message.content.startswith('$similar '):
        print('$similar command found')
        text = message.content
        print(text)
        t0 = time.time()
        # band number for disambiguation
        if text.find('|') != -1:
            text = text.split('|')
            bandnumber = text[-1]
            text = text[0].split('$similar')
            bandname = text[-1].strip()
            print('Band name: ' + bandname)
            print('Band number: ' + str(bandnumber))
            results = SIMILAR(bandname, bandnumber, bprint)
            output = msg_lim(results, char_lim)
            for i in range(0, len(output)):
                msg = '```' + output[i] + '```'
                await message.channel.send(msg)
        else:
            t = text.split('$similar')
            bandname = t[-1].strip()
            print('Band name: ' + str(bandnumber))
            results = SIMILAR(bandname, 0, bprint)
            output = msg_lim(results, char_lim)
            for i in range(0, len(output)):
                msg = '```' + output[i] + '```'
                await message.channel.send(msg)
        t1 = time.time()
        print(t1-t0)

    # look up artist
    if message.content.startswith('$artist '):
        print('$artist command found')
        text = message.content
        print(text)
        t0 = time.time()
        # artist disambiguation number
        if text.find('|') != -1:
            text = text.split('|')
            artistnumber = text[-1]
            text = text[0].split('$artist')
            artistname = text[-1].strip()
            print('Artist name: ' + artistname)
            print('Artist number: ' + str(artistnumber))
            results = ARTISTLOOKUP(artistname, artistnumber, bprint)
            output = msg_lim(results, char_lim)
            for i in range(0, len(output)):
                msg = '```' + output[i] + '```'
                await message.channel.send(msg)
        else:
            t = text.split('$artist')
            artistname = t[-1].strip()
            artistnumber = 0
            print('Artist name: ' + artistname)
            results = ARTISTLOOKUP(artistname, artistnumber, bprint)
            output = msg_lim(results, char_lim)
            for i in range(0, len(output)):
                msg = '```' + output[i] + '```'
                await message.channel.send(msg)
        t1 = time.time()
        print(t1-t0)

    # look up album
    if message.content.startswith('$album '):
        print('$album command found')
        text = message.content
        print(text)
        t0 = time.time()
        # album disambiguation
        if text.find('|') != -1:
            text = text.split('|')
            albumnumber = text[-1].strip()
            text = text[0].split('$album')
            text2 = text[-1].split('$album')[-1].strip().split(':')
            albumname = text2[-1].strip()
            bandname = text2[0].strip()
            print('Album name: ' + albumname)
            print('Band name: ' + bandname)
            print('Album number: ' + albumnumber)
            results = ALBUMLOOKUP(bandname, albumname, albumnumber, bprint)
            output = msg_lim(results, char_lim)
            for i in range(0, len(output)):
                msg = '```' + output[i] + '```'
                await message.channel.send(msg)
        else:
            t = text.split('$album')
            text2 = text.split('$album')[-1].strip().split(':')
            bandname = text2[0].strip()
            albumname = text2[-1].strip()
            print('Album name: ' + albumname)
            print('Band name: ' + bandname)
            albumnumber = 0
            results = ALBUMLOOKUP(bandname, albumname, albumnumber, bprint)
            output = msg_lim(results, char_lim)
            for i in range(0, len(output)):
                msg = '```' + output[i] + '```'
                await message.channel.send(msg)
        t1 = time.time()
        print(t1-t0)
    
    # random
    if message.content.startswith('$random '):
        print('$random command found')
        t0 = time.time()
        results = RANDOM(bprint)
        output = msg_lim(results, char_lim)
        for i in range(0, len(output)):
            msg = '```' + output[i] + '```'
            await message.channel.send(msg)
        t1 = time.time()
        print(t1-t0)

client.run(TOKEN)
