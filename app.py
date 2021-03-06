﻿from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__1111job__)

# Channel Access Token
line_bot_api = LineBotApi('L/0Npk/IntIGOiYL2m/mrwiuEO6H+Q5aAdQSsuougCLNS0qjI6OzqyJXFZ8bwT/pH26pg6YntaSJzKZ6Z8t7CCZ0tLkKHU2VOpaHprz3Va9ndGCx7tcMbiAU8goDK/ZMT1yyPk40JtLcJoc/2HGl9AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('975d4c8d9ee2cb8da4a9cc06d40133df')

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
