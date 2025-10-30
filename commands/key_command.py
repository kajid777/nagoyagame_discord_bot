import discord
from discord import app_commands
from check_answer import check_answer, EBIFLY_CORRECT, HAMIGAKI_CORRECT
from config import ALLOWED_CHANNEL_IDS

async def setup_key_command(tree, client):
    """keyコマンドをCommandTreeに登録する"""
    
    @tree.command(name="key", description="入力されたメッセージをチェックして正解判定します")
    async def key_command(interaction: discord.Interaction, text: str):
        # コマンドが発動したチャンネルIDを取得
        channel_id = interaction.channel_id
        channel = interaction.channel
        
        # チャンネルIDチェック
        if channel_id not in ALLOWED_CHANNEL_IDS:
            await interaction.response.send_message(
                "自分のチームのチャンネルでしかこのコマンドは使用できませんw",
                ephemeral=True  # 本人にだけ見えるメッセージ
            )
            return
        
        # 正解判定
        which_answer = check_answer(text)
        
        # メッセージ内容を決定
        if which_answer == EBIFLY_CORRECT:
            # エビフライ正解の場合
            message = "ゆきやのかんがえたすと－りー、１"
        elif which_answer == HAMIGAKI_CORRECT:
            # 歯磨き正解の場合
            message = "ゆきやのかんがえたすと－りー、２"
        else:
            # 不正解の場合
            message = f"❌ **不正解だよw**「 `{text}` 」は模範解答ではありませんw"
        
        # コマンドが発動したチャンネルにメッセージを送信
        await interaction.response.send_message(message)
        
        # ログにチャンネル情報を出力
        print(f"[key command] チャンネルID: {channel_id}, メッセージ: {message}")