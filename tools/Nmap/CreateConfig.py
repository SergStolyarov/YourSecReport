import configparser
config = configparser.ConfigParser()
config['EMAILAUTH'] = {'Login': 'yoursecreport@gmail.com',
                      'Password': 'fTlBF7u5I5p8'}
with open('config.ini', 'w') as configfile:
    config.write(configfile)