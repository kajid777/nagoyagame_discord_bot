import discord
from discord import app_commands
from check_answer import check_answer

async def setup_key_command(tree, client):
    """keyコマンドをCommandTreeに登録する"""
    
    @tree.command(name="key", description="入力されたメッセージをチェックして正解判定します")
    async def key_command(interaction: discord.Interaction, text: str):
        # 正解判定
        is_correct = check_answer(text)
        
        if is_correct:
            # 正解の場合
            await interaction.response.send_message(f"🎉 **正解！** `{text}` は模範解答です！")
        else:
            # 不正解の場合
            await interaction.response.send_message(f"❌ **不正解** `{text}` は模範解答ではありません。")