import flask
from flask import Flask, request, abort
from flask_mongoengine import MongoEngine
import os
import json
from env_loader import (
    get_channel_access_token, get_channel_secret, get_mongo_host, get_mongo_port, get_mongo_username, get_mongo_passwd
)
from chat import get_ai_response
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, QuickReply, QuickReplyButton, URIAction
)


channel_access_token = get_channel_access_token()
channel_secret = get_channel_secret()

db = MongoEngine()
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = [
    {
        'db': 'looky',
        'host': get_mongo_host(),
        'port': get_mongo_port(),
        'username': get_mongo_username(),
        'password': get_mongo_passwd(),
        'alias': 'default',
    }
]
db.init_app(app)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

@app.route('/')
def home():
    return f'<h1>Good Night World</h1>'


@app.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print('Invalid signature. Please check your channel access token/channel secret.')
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    rcv_message: str = event.message.text.lower()

    source_type: str = event.source.type
    user_id: str = event.source.user_id
    group_id: str = event.source.group_id if source_type == 'group' else None

    json_url: str = ''
    gpt_model: str = 'gpt-3.5-turbo'

    if rcv_message == 'change model':
        quick_reply = QuickReply(items=[
            QuickReplyButton(action=URIAction(label='GPT-4(Preview)', text='change model to GPT-4(Preview)')),
            QuickReplyButton(action=URIAction(label='GPT-4', text='change model to GPT-4')),
            QuickReplyButton(action=URIAction(label='GPT-3', text='change model to GPT-3')),
        ])
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='Which model do you want to use?', quick_reply=quick_reply))

    answer: str = ''

    # Check if the message is from a group or from a user
    if source_type == 'group':
        # In a group, Looky answers when the message contains 'Looky'
        if 'looky' in rcv_message:
            answer = chat(rcv_message.replace('looky', ''))
    elif source_type == 'user':
        # In a 1-to-1 chat, Looky answers any message
        answer = chat(rcv_message)

    if answer != '':        
        # Remove leading and trailing spaces
        answer = answer.strip()

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=answer))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)