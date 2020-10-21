from twilio.rest import Client

client = Client("AC679de3766e3c0c980f4355884d3ba3c5", "ae7ab35d843e28ffe99901118b107821")

for message in client.messages.list():
    print(message.body)
    #message.delete()


new_message = client.messages.create(
    to = "+840988864538",
    from_ = "+18189624116",
    body = "bonjour from python"
)
print(f"Created message successfully {new_message.sid}")