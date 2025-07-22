
#-------------------------------------------------------------
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = 29742884
api_hash = 'd3f0e1677c841276399e9b2b24151463'

# Bu yerga 1-qadamda olingan stringni joylashtiring:
string_session = "1ApWapzMBu6taZKDoO7Btvj5rGNL5AJ2NM5NqBIIGWUEU_ND3nWi61T2Tn5-EcBMZZ2EiIwC1O4cXGrikqp0_4QCsHUWd_DgTQdxaSGL-NRMKxSTZEyB7t8DYdLlW0Y9onJ06e2_DWiNATR3-3KIpmNdcfo55ek1oROqIVAOrOjdSDy_Bt4drlzVqn5ODaJdvsqkrDZJGnFoi5XLreRPQw0VfdIEMAK7y0HK11Hge46M3agCbhpRUqrKlQMjPWc1FMTSeLsanoz6QwlrbHjGRnPqC1WwVYRV6_kRJpBz3iFXxokUJyBJccczwPGI7N6ms8ss9c8bQpP9R7xV48qv3S7XKslqSRug="

client = TelegramClient(StringSession(string_session), api_id, api_hash)

allowed_user_ids = [223606463,  632060122,  ]
channel_username = '@myphddoc'

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    sender = await event.get_sender()
    if sender.id not in allowed_user_ids:
        return
    if event.document:
        file_name = event.document.attributes[0].file_name.lower()
        if file_name.endswith(('.doc', '.docx', '.pdf')):
            await client.send_file(channel_username, event.document, caption=f"Yangi hujjat: {file_name}")

client.start()
client.run_until_disconnected()

