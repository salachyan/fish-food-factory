from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACf88bce7991d5b18dfce285d41da9110a"
auth_token  = "2c37f1c5ec7bfc4aed5b6ab2b899a92c"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17036770846",
    from_="+18775408193",
    body="Your cucumbers are about to expire! Make sure to finish them or else Crumky "
         "the Cucumber Manatee will swim away :( ")

print(message.sid)