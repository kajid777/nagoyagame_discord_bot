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
            message = "「エビフリャー...？わけがわからないな...。」\n\n「そういえば、エビフリャーってタモリが言い出した架空の方言で、\n名古屋の人は言わないらしいな...。\nということは犯人は名古屋の人ではないかもしれない。」\n\n「犯人は僕たちと同じ観光客...？\nくそ、人を殺して自分は呑気に観光ってわけか！\nそうはさせないぞ..！\nよし、名古屋の一番の観光地と言えば....」\n"
            
            # メッセージを送信
            await interaction.response.send_message(message)
            
            # 画像を送信
            try:
                image_file = discord.File("名古屋城へ向かえ.png")
                await channel.send(file=image_file)
            except FileNotFoundError:
                print("エラー: 画像ファイルが見つかりません")
            except Exception as e:
                print(f"画像送信エラー: {e}")
            
            # ログ出力
            print(f"[key command] チャンネルID: {channel_id}, メッセージ: {message}")
            return
            
        elif which_answer == HAMIGAKI_CORRECT:
            # 歯磨き正解の場合
            message = "「ハミガキ...？なんだこれ！おちょくっているのか！！」\n\n堀はなかなか核心にたどり着けないことに苛立ちを覚えていた。\n\n\n「犯人を追って名古屋の観光地をたくさん回ったけど、\n　結局何も手がかりをつかめなかった。\n　もはや僕もこれまでか...」\n\n親友の敵を討つことができず、悔しさで顔をゆがませながら\n梶原の後を追おうとしたその瞬間、1枚の紙切れが舞い落ちてきた。\nその紙には最後の希望が記されていた。\n"
            
            # メッセージを送信
            await interaction.response.send_message(message)
            
            # 画像を送信
            try:
                image_file = discord.File("最後の目的地_中村公園駅.png")
                await channel.send(file=image_file)
            except FileNotFoundError:
                print("エラー: 画像ファイルが見つかりません")
            except Exception as e:
                print(f"画像送信エラー: {e}")
            
            # ログ出力
            print(f"[key command] チャンネルID: {channel_id}, メッセージ: {message}")
            return
        else:
            # 不正解の場合
            message = f"❌ **不正解**「 `{text}` 」は違う"
        
        # コマンドが発動したチャンネルにメッセージを送信
        await interaction.response.send_message(message)
        
        # ログにチャンネル情報を出力
        print(f"[key command] チャンネルID: {channel_id}, メッセージ: {message}")