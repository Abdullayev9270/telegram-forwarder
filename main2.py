from telethon import TelegramClient, events

# 👉 API ma'lumotlaringiz
api_id = 29742884
api_hash = 'd3f0e1677c841276399e9b2b24151463'

# 👉 Ruxsat etilgan foydalanuvchi ID'lari (bir nechta bo'lishi mumkin)
allowed_user_ids = [
    223606463,  # misol uchun foydalanuvchi 1
    632060122,  # misol uchun foydalanuvchi 2
]

# 👉 Fayllar forward qilinadigan kanal username yoki ID
channel = '@myphddoc'  # yoki -100XXXXXXXXXXXX

# 👉 Client sessiyasini ishga tushiramiz
client = TelegramClient('my_session', api_id, api_hash)

# 👉 Har bir yangi xabarni kuzatamiz
@client.on(events.NewMessage(incoming=True))
async def handler(event):
    sender = await event.get_sender()

    # Faqat ruxsat etilgan foydalanuvchilardan bo‘lsa
    if sender.id not in allowed_user_ids:
        print(f"❌ Ruxsat yo‘q: {sender.id}")
        return

    # Hujjat bo‘lsa va .doc/.docx/.pdf formatda bo‘lsa
    if event.document:
        file_name = event.document.attributes[0].file_name.lower()
        if file_name.endswith(('.doc', '.docx', '.pdf')):
            print(f"📄 Qabul qilindi: {file_name} ({sender.id} dan)")
            await client.send_file(channel, event.document, caption=f"Yangi hujjat: {file_name}")
        else:
            print(f"⛔ Noto‘g‘ri fayl turi: {file_name}")
    else:
        print("⚠️ Hujjat emas.")

# 👉 Clientni ishga tushuramiz
client.start()
print("🚀 Dastur ishga tushdi. Lichkaga kelgan fayllar kuzatilmoqda...")
client.run_until_disconnected()
