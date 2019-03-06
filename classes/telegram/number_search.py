from classes.connector import Connector


class NumberSearch:

    def search_number(number):
        conn = Connector.connect()
        conn.send_message('flooterbot', '/help')

        return "no msg"
