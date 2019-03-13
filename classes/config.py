import configparser


class Config:

    config = configparser.ConfigParser()
    config.read("config.ini")

    api_id = config.get("telegram", "api_id")
    api_hash = config.get("telegram", "api_hash")
    session = config.get("telegram", "session")

    proxy_ip = config.get("proxy", "addr")
    proxy_port = int(config.get("proxy", "port"))
    proxy_login = config.get("proxy", "login")
    proxy_pass = config.get("proxy", "password")

    def __getattr__(self, attr):
        return attr
