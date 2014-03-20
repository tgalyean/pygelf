import ConfigParser
import io
import os

# check for config.ini
if os.path.isfile('config.ini') == True:
    # parse config.ini contents
    _CONFIG = ConfigParser.RawConfigParser()
    _CONFIG.read(io.BytesIO('config.ini'))
    _ENV = _CONFIG.get('global','env')
else:
    print "Configuration file missing.. config.ini required in " + os.getcwd()
    exit(1)
def get(key):
    return _CONFIG.get(_ENV, key)
