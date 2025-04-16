import configparser
import os

class ReadProperties:
    config_path = os.path.join(os.path.dirname(__file__), "C:\\Users\Admin\\PycharmProjects\\OrangeHRM\\configurations\\config.ini")

    @staticmethod
    def get_application_url():
        config = configparser.RawConfigParser()
        config.read(ReadProperties.config_path)
        return config.get("common info", "baseURL")

    @staticmethod
    def get_username():
        config = configparser.RawConfigParser()
        config.read(ReadProperties.config_path)
        return config.get("common info", "username")

    @staticmethod
    def get_password():
        config = configparser.RawConfigParser()
        config.read(ReadProperties.config_path)
        return config.get("common info", "password")
