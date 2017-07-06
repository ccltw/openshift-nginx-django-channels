import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http

def ws_receive(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    message.reply_channel.send({
        "text": message['text'],
    })

#@channel_session_user_from_http
def ws_connect(message):
    # message.reply_channel.send({"accept": True})
    message.reply_channel.send({
        "text": "connect",
    })
    

#@channel_session_user
def ws_disconnect(message):
    message.reply_channel.send({
        "text": "disconnect",
    })
