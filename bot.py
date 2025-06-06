import discord
from discord.ext import commands
import os

# Pour charger les variables d'environnement depuis un fichier .env (optionnel mais recommandé en local)
from dotenv import load_dotenv
load_dotenv()  # charge les variables depuis un fichier .env s'il existe

bot = discord.Client(intents=discord.Intents.all()) 

# Remplace ceci par l'ID de l'utilisateur qui déclenche le mute
ID_DU_GOAT = 239746340559650816

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user}')

@bot.event
async def on_message(message: discord.Message):
    channel = message.channel
    if message.content == "i" and channel.id == 1283064453386080402 :
        await channel.send("ratio loser")

@bot.event
async def on_voice_state_update(member, before, after):
    # Vérifie si l'utilisateur vient de rejoindre un salon vocal
    if before.channel is None and after.channel is not None:
        if member.id == ID_DU_GOAT:
            channel = after.channel
            for m in channel.members:
                if m.id != ID_DU_GOAT and not m.bot:
                    try:
                        await m.edit(mute=True)
                        print(f'Muted: {m.name}')
                    except Exception as e:
                        print(f"Erreur en mutant {m.name}: {e}")

# token du bot
TOKEN = os.getenv('DISCORD_TOKEN')

bot.run(TOKEN)
