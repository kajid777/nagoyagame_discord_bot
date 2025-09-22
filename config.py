# ボットの設定ファイル

# Discord Bot Token

import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# Discord Bot Token
# os.getenv()を使って、.envファイルに書かれたトークンを安全に取得する
BOT_TOKEN = os.getenv('BOT_TOKEN')

# チャンネルID (これは秘密情報ではないので、このままでOK)
ADMIN_CHANNEL_ID = 1415693690755874866