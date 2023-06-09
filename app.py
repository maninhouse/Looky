from flask import Flask, request, abort
import os
from dotenv import load_dotenv
from chat import ask

load_dotenv()

channel_access_token = os.getenv('CHANNEL_ACCESS_TOKEN')
channel_secret = os.getenv('CHANNEL_SECRET')

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

@app.route("/")
def home():
    return f"<h1>Hello World</h1>"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    rcv_message: str = event.message.text.lower()
    # Looky answers when the message contains "Looky"
    if 'looky' in rcv_message:
        answer: str = ask(rcv_message.replace('looky', ''))
        while len(answer) > 0 and (answer[0] == ' ' or answer[-1] == ' '):
            answer = answer.strip()

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=answer))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)