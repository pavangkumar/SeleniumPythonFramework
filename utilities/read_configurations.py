from configparser import ConfigParser
import os

class ReadConfig:
    config = ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), "..", "configurations", "config.ini")
    config.read(config_path)

    @staticmethod
    def get_base_url():
        return ReadConfig.config.get("basic info", "baseURL")

    @staticmethod
    def get_browser():
        return ReadConfig.config.get("basic info", "browser")

    @staticmethod
    def get_username():
        return ReadConfig.config.get("basic info", "username")

    @staticmethod
    def get_password():
        return ReadConfig.config.get("basic info", "password")
