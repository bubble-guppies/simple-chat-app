import numpy as np
import uuid

class Client:
    '''
    initializes variables as strings
    '''
    username = ""
    ip_address = ""
    password = ""
    uuid = ""

    def Client(self):
        pass

    def Client(self, username, ip_address, password, uuid):
        self.username = username
        self.ip_address = ip_address
        self.password = password
        self.uuid = uuid

    