import discord
from discord import app_commands

async def setup_key_command(tree, client):
    """keyコマンドをCommandTreeに登録する"""
    
    @tree.command(name="key", description="入力されたメッセージをオウム返しします")
    async def key_command(interaction: discord.Interaction, message: str):
        # 引数をそのままオウム返し
        await interaction.response.send_message(f"{message}")