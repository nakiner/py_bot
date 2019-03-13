from telethon.sync import TelegramClient
from classes.config import Config
import asyncio
import socks


class Connector:

    # type: TelegramClient
    def start() -> TelegramClient:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        client = TelegramClient(Config.session, Config.api_id, Config.api_hash, loop=loop,
                                proxy=(socks.SOCKS5, Config.proxy_ip, Config.proxy_port, 'true', Config.proxy_login, Config.proxy_pass))
        return client
