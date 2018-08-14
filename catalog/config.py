import configparser


config = configparser.ConfigParser()
config.read("/home/adm1n01//bots/kidsReferal/env/APBot2test/catalog/config.ini")
token = config["DEFAULT"]["token"]
