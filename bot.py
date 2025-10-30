import discord
from discord import app_commands
import asyncio
from config import BOT_TOKEN

# 接続に必要なオブジェクトを生成
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# コマンドを直接ここで登録
from commands.hello_command import setup_hello_command
# from commands.submit_command import setup_submit_command
from commands.key_command import setup_key_command

# 起動時にターミナルにログイン通知が表示される
@client.event
async def on_ready():
    print('ログインしました')
    
    # コマンドをセットアップ
    await setup_hello_command(tree, client)
    # await setup_submit_command(tree, client)
    await setup_key_command(tree, client)
    
    # スラッシュコマンドを同期
    try:
        synced = await tree.sync()
        print(f'{len(synced)}個のコマンドが同期されました')
        for cmd in synced:
            print(f'- {cmd.name}')
    except Exception as e:
        print(f'コマンドの同期に失敗しました: {e}')

# ボットを起動
client.run(BOT_TOKEN)