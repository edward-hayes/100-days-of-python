import os
from twilio.rest import Client


account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body="🧪 This is a test",
        from_="",  # telephone number
        to=""      # telephone number
    )