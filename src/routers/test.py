import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ""
auth_token = ''
client = Client(account_sid, auth_token)

call = client.calls.create(
    from_="+15017122661",
    to="+14155551212",
    url="http://demo.twilio.com/docs/voice.xml",
)

print(call.sid)