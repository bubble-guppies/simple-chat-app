import uuid
import socket

class Client:
    '''
    initializes variables as strings
    '''
    username = ""
    ip_address = ""
    password = ""
    uuid = ""

    def client(self, username, ip_address, password, uuid):
        self.username = username
        self.ip_address = ip_address
        self._password = password
        self.uuid = uuid
    
    def get_username(self):
        return self.username
    
    def get_ip_address(self):
        return self.ip_address
    
    def get_uuid(self):
        return self.uuid
    
    def send_message(self):
        pass

    def disconnect(self):
        pass

    