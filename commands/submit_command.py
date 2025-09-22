import discord
from discord import app_commands
from config import ADMIN_CHANNEL_ID

# ボタンを持つViewクラス
class SubmitView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)  # 5分でタイムアウト
    
    @discord.ui.button(label='承認', style=discord.ButtonStyle.green, emoji='✅')
    async def approve_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('承認されました！')
    
    @discord.ui.button(label='拒否', style=discord.ButtonStyle.red, emoji='❌')
    async def reject_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('拒否されました！')

async def setup_submit_command(tree, client):
    """submitコマンドをCommandTreeに登録する"""
    
    @tree.command(name="submit", description="指定したチャンネルに2つのボタンを表示します")
    async def submit_command(interaction: discord.Interaction):
        # ボタンを含むViewを作成
        view = SubmitView()
        
        # 指定されたチャンネルにメッセージとボタンを送信
        target_channel = client.get_channel(ADMIN_CHANNEL_ID)
        if target_channel:
            await target_channel.send("申請が送信されました。以下のボタンで承認・拒否してください：", view=view)
            # コマンドを実行した本人にだけ見える確認メッセージを送る
            await interaction.response.send_message(f"{target_channel.name} にボタンを送信しました！", ephemeral=True)
        else:
            # チャンネルが見つからなかった場合のエラーメッセージ
            await interaction.response.send_message("エラー: 指定されたチャンネルが見つかりませんでした。", ephemeral=True)
