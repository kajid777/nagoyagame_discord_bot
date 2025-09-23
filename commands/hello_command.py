import discord
from discord import app_commands
from config import ADMIN_CHANNEL_ID

async def setup_hello_command(tree, client):
    """helloコマンドをCommandTreeに登録する"""
    
    @tree.command(name="hello", description="指定したチャンネルにhelloworldと送信します")
    async def hello_command(interaction: discord.Interaction):
        # メッセージを送信
        target_channel = client.get_channel(ADMIN_CHANNEL_ID)
        if target_channel:
            await target_channel.send("helloworld")
            # コマンドを実行した本人にだけ見える確認メッセージを送る
            await interaction.response.send_message(f"{target_channel.name} にメッセージを送りました！")
        else:
            # チャンネルが見つからなかった場合のエラーメッセージ
            await interaction.response.send_message("エラー: 指定されたチャンネルが見つかりませんでした。")
