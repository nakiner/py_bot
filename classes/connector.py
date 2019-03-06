from telethon.sync import TelegramClient
from config import Config
import asyncio
import socks


class Connector:

    # type: TelegramClient
    def start() -> TelegramClient:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        client = TelegramClient(Config.session, Config.api_id, Config.api_hash, loop=loop,
                                proxy=(socks.SOCKS5, 'worldpics.pro', 2016, 'true', 'nakiner', 'nakiner1'))
        return client

# client.send_message('me', 'Hello! Talking to you from Telethon')
# client.send_file('fighter_kit', '/Users/admin/Downloads/tech-bg.jpg')


# @client.on(events.NewMessage(incoming=True, pattern='(?i)hi'))
# async def handler(event):
#     await event.reply('Hello!')

# client.run_until_disconnected()
