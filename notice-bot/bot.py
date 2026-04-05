import os
import discord
from keep_alive import keep_alive

# メッセージの中身を読み取るための権限（Intents）を設定
intents = discord.Intents.default()
intents.message_content = True

# Botの本体を作成
client = discord.Client(intents=intents)

# 環境変数を読み込み,int型に変換
CH_ID_1 = int(os.environ.get("CHANNEL_ID_1", 0))
CH_ID_2 = int(os.environ.get("CHANNEL_ID_2", 0))

# Botがdiscordに接続できたときに動く部分
@client.event
async def on_ready():
    print(f'{client.user} がオンラインになりました！監視を始めます。')

# メッセージを受信したときに動く部分
@client.event
async def on_message(message):
    # Bot自身のメッセージには反応しないようにする
    if message.author == client.user:
        return

    # チャンネルを指定
    if (message.channel.id == CH_ID_1) or (message.channel.id == CH_ID_2):

        print(f'{message.author.name}さんが発言しました: {message.content}')

        # IDを使ってアカウントを検知
        user = await client.fetch_user(657130921626959872)
        # 見つけたアカウント宛てにDMを送る
        await user.send(f'【サークル通知】{message.author.name}さんから連絡です！\n内容: {message.content}')
        
# Botを起動する
keep_alive()
TOKEN = os.environ.get("DISCORD_TOKEN")
client.run(TOKEN)