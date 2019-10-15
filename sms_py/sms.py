from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+1206823****',
    to='+183284*****',
    body='Test message-- HELLOOOOO'
)

print(message.sid)
