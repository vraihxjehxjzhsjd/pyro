import pyrogram, random

@pyrogram.Client.on_message()
async def ok(client, message):
    count = 0
    trigger = "а"
    if message.text != trigger:
        return
    for _ in range(100):
        await client.send_message(message.chat.id, random.choice(message) + str(count))
        print(f"sended. COUNT: {count}")
 
