# hesher-discord-bot
A Discord bot that scrapes [the Metal Archives](https://www.metal-archives.com/) for information on bands, artists, and albums, and dumps into the text chat.  The bot utilizes the [metal-archives-lookup](https://github.com/baja-blastoise/metal-archives-lookup) python library to pull the requested information.

## Dependencies
Hesher uses Python3 and the following libraries:
1. os
2. dotenv
3. math
4. time
5. discord.py
6. [metal-archives-lookup](https://github.com/baja-blastoise/metal-archives-lookup) *(requires its own dependencies)*

## Installation
Discord has it's own process for creating and connecting bots.  You can follow along with [this guide](https://discordpy.readthedocs.io/en/stable/discord.html) if you need help getting one setup.

Install the required dependencies in your python environment.  Clone this repository using:

`git clone https://github.com/baja-blastoise/hesher-discord-bot`

Copy **malookup.py** into the same directory you will run the bot from, or otherwise add it to your environment.  Proceed to the configuration section below.

## Configuration
Most of the bot configuration is handled on the Discord site.  Once the bot is created, copy the token and create a file called **.env** and enter the line:
```
DISCORD_TOKEN=[*your token here*]
```

You can tweak some settings within the *hesher_discord.py* script itself.  Setting *bprint* to **True** prints commands the bot receives and it's responses in the terminal.  Useful for debugging or otherwise monitoring the bot when hosting it.  The *char_lim* setting controls the max length of the bot responses.  Anything longer than that will be split across multiple messages.  The Discord default max length is 2000 characters.

## Usage
Once you have finished configuring the bot, launch it in your terminal with:

`python3 hesher_discord.py`

The bot will stay active as long as the process is active.

The bot supports the following commands.  Detailed usage syntax with examples can be found in the help.txt file, or using the `$help` command in the IRC channel itself.
- **$help** - displays info contained in *help.txt*
- **$band** - returns basic information about a band
- **$discog** - returns a band's discograpy
- **$members** - returns a band's lineup
- **$similar** - returns similar bands based on Metal Arcives ratings
- **$artist** - returns basic artist information as well as band membership
- **$album** - returns album track listing and lineup


## Issues / Quirks

Web scraping is an imprecise practice (and I'm not good at it) and the archives have 20 years of submissions of varying quality.  Some of the formatting might not work for some of the less detailed bands.

Bands written in a script besides latin, or those using diacritics, can be difficult to use.  The library works by inferring the appropriate URL based on band/artist/album name.  Usually diacritics are ignored completely and other scripts are usually Romanized.  But it might take some trial and error to find the right string.

Share the command string if you encounter unexpected output.
