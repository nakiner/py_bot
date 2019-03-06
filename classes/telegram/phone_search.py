import asyncio
from telethon import events
from telethon.sync import TelegramClient
from config import Config
from classes.connector import Connector

class PhoneSearch:

    def search_phone(phone):

        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)
        # client = TelegramClient(Config.session, Config.api_id, Config.api_hash, loop=loop)
        # client.connect()

        client = Connector.start()
        client.connect()

        client.send_message('flooterbot', '/help')

        @client.on(events.NewMessage)
        async def my_event_handler(event):
            if 'help' in event.raw_text:
                await event.reply('hi!')
                print("got msg")
                client.disconnect()

        client.run_until_disconnected()
        print("exit")
        return "ok"
