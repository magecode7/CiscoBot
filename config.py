import configparser
import sys
import os

path = 'settings.ini'
token = ''
admin = 0
search_percent = 50

    
if __name__ == "__main__":
    config = configparser.ConfigParser()

    config.add_section('Settings')
    config.set('Settings', 'token', input('Enter bot token: '))
    config.set('Settings', 'admin', input('Enter admin id: '))
    config.set('Settings', 'search', '50')

    with open(path, 'w') as config_file:
        config.write(config_file)

else:
    config = configparser.ConfigParser()
    if os.path.exists(path):
        config.read(path)

    if not config.has_section('Settings'):
        config.add_section('Settings')

    try:
        token = config.get('Settings', 'token')
        if len(token) <= 0:
            sys.exit(f'Bot token missed in {path}')
    except:
        config.set('Settings', 'token', '')
        sys.exit(f'Bot token missed in {path}')

    try:   
        admin = config.getint('Settings', 'admin')
        if admin <= 0:
            sys.exit(f'Admin id missed in {path}')
    except:
        config.set('Settings', 'admin', '')
        sys.exit(f'Admin id missed in {path}')

    try:
        search_percent = config.getint('Settings', 'search')
    except:
        config.set('Settings', 'search', '50')


    with open(path, 'w') as config_file:
        config.write(config_file)

