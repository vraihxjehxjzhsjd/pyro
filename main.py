import pyrogram

with open("message.txt", "r+") as file:
    message = file.read().split("\n")
    file.close()

pyrogram.Client("1").start()
print("log as 1")
pyrogram.Client("2").start()
print("log as 2")
print("send 'а' to chat")
pyrogram.idle()
