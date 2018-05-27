from twilio.rest import Client

# Your Account SID from twilio.com/console
account = "account hide"
# Your Auth Token from twilio.com/console
token  = "token hide"



client = Client(account, token)

message = client.messages.create(to="receiver number", from_="my twilio number",
                                 body="Hello there!")