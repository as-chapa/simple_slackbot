from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

import pya3rt

@respond_to('今日の天気は？')
def say_hello(message):
    message.reply('外の天気に関係なく私の心はいつだって晴れだ')

@listen_to('ボット')
def listen_func(message):
    message.send('誰かが私の噂をしているようだ。')      # botからの投稿
    message.reply('君かね？')                       # botからのメンション

@default_reply()
def default_message(message):
    apikey = "{Your API KEY}"
    client = pya3rt.TalkClient(apikey)
    reply_message = client.talk(message.body['text'])
    message.reply(reply_message['results'][0]['reply'])
