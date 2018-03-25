from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__huan1111job__)

# Channel Access Token
line_bot_api = LineBotApi('OMrEDvlmTVfwYi0IZ8GAWcPISUh33LBSBdzPCh1cs2HNG1xT2hO1Y57PvjcOg0A6H26pg6YntaSJzKZ6Z8t7CCZ0tLkKHU2VOpaHprz3Va9fW0dNJ7008cqMFvWfgkgmHvPoHQ31SkxPlxhTWeSYtQdB04t89/1O/w1cDnyilFU=iazefK4Wxy5y9FMo0yMX5hB8Xb+AodTHiDywjCnwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('62e4c1f533318e02abc0b0f8f4a18fb0')

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
