from configparser import ConfigParser

config = ConfigParser()
config.read('aktien.ini')
default_conf = config['DEFAULT']
db_conf = config['DB']