import pyrogram, random
global count, trigger, message

count = 0
@pyrogram.Client.on_message()
async def ok(client, message):
    if message.text != trigger:
        return
    for _ in range(100):
        await client.send_message(message.chat.id, random.choice(message) + str(count))
        print(f"sended. COUNT: {count}")
 
