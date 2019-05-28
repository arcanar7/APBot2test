import configparser


config = configparser.ConfigParser()
config.read("/home/ubuntu/bots/kidsReferal/env/APBot2test/catalog/config.ini")
# config.read("config.ini")
token = config["DEFAULT"]["token"]
