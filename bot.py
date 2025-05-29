from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = 12345678  # 🔁 Replace with your actual API ID
API_HASH = "your_api_hash"  # 🔁 Replace with your API HASH
BOT_TOKEN = "your_bot_token"  # 🔁 Replace with your BOT TOKEN

app = Client("port_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("port") & filters.private)
async def port_check(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply("Usage: `/port <port_number>`", quote=True)

    port = message.command[1]
    if not port.isdigit():
        return await message.reply("❌ Invalid port number.", quote=True)

    port = int(port)
    # Dummy logic: Treat ports 80, 443, 8080 as open
    if port in [80, 443, 8080]:
        status = "✅ Port is open (dummy response)"
    else:
        status = "❌ Port is closed (dummy response)"

    await message.reply(f"🔍 Port `{port}` status:\n{status}", quote=True)

app.run()
