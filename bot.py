import discord
from discord.ext import commands
import time
import os

# HOST HEALTH BULLSHIT

import threading
from flask import Flask

app = Flask('')

def run():
    app.run(host='0.0.0.0', port=8080)

threading.Thread(target=run).start()

@app.route('/')
def home():
    return 'OK', 200


# BOT

# Pour charger les variables d'environnement depuis un fichier .env
from dotenv import load_dotenv
load_dotenv()  # charge les variables depuis un fichier .env s'il existe

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.members = True 

bot = commands.Bot(command_prefix='!', intents=intents)

#bot = discord.Client(intents=discord.Intents.all()) 

#ID_DU_GOAT = 239746340559650816

#ID_DU_DOG = 216143911314391042

ID_DU_GOAT = 563434444321587202

ID_DU_DOG = 663792637094133790

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user}')

@bot.event
async def on_voice_state_update(member, before, after):
    # Vérifie si l'utilisateur vient de rejoindre un salon vocal
    if before.channel is None and after.channel is not None:
        if member.id == ID_DU_GOAT:
            channel = after.channel
            for m in channel.members:
                if m.id == ID_DU_DOG:
                    try:
                        await m.edit(mute=True)
                        print(f'Muselière appliquée: {m.name}')
                        time.sleep(3)
                        await m.edit(mute=False)
                        print(f'Muselière retirée: {m.name}')
                    except Exception as e:
                        print(f"Erreur en mutant {m.name}: {e}")

# token du bot
TOKEN = os.getenv('DISCORD_TOKEN')

bot.run(TOKEN)
