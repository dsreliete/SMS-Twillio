from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC3088fd2b65b3a2a8436335dc1e5be36f"
auth_token = "5460b2a8fa472ecdcebb82d7b3d0e07e"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello there!", to="+5511995396355",
                                 from_="+554139087762")
print(message.sid)
