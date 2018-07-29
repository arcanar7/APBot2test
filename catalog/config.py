import configparser


config = configparser.ConfigParser()
config.read("config.ini")
token = config["DEFAULT"]["token"]
