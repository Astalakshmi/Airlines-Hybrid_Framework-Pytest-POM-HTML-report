from configparser import ConfigParser


def read_Configuration(category,key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category,key)
