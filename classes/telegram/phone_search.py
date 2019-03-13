from telethon import events
from classes.connector import Connector


class PhoneSearch:

    def search_phone(phone):

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
