import configparser
class Config:
    SDKPath = 'F:/hk/pyhikvision/lib/win64/'
    # SDKPath = 'D:/java/HKCamera/'
    User = 'admin'
    Password = 'jxlgust123'
    Port = 8000
    IP = '172.26.20.41'
    Plat = '1'  # 0-Linux，1-windows
    Suffix = '.dll'

    def InitConfig(self, path):
        # cnf = configparser.ConfigParser()
        # cnf.read(path)
        # self.SDKPath = cnf.get('DEFAULT', 'SDKPath')
        # self.User = cnf.get('DEFAULT', 'User')
        # self.Password = cnf.get('DEFAULT', 'Password')
        # self.Port = cnf.getint('DEFAULT', 'Port')
        # self.IP = cnf.get('DEFAULT', 'IP')
        # self.Plat = cnf.get('DEFAULT', 'Plat')

        # self.SDKPath = cnf.get('DEFAULT', 'SDKPath')
        # self.User = cnf.get('DEFAULT', 'User')
        # self.Password = cnf.get('DEFAULT', 'Password')
        # self.Port = cnf.getint('DEFAULT', 'Port')
        # self.IP = cnf.get('DEFAULT', 'IP')
        # self.Plat = cnf.get('DEFAULT', 'Plat')
        # if self.Plat == '1':
        #     self.Suffix = '.dll'
        return
