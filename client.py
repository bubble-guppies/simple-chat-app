from message import Message
import message
import time
import uuid

class Client:
    '''
    creates variables as strings
    '''
    username = ""
    ip_address = ""
    password = ""
    uuid = ""

    def __init__(self, username, ip_address, password, uuid):
        '''
        Initializes variables
        password is protected
        '''
        self.username = username
        self.ip_address = ip_address
        self._password = password
        self.uuid = uuid

    def get_username(self):
        '''
        returns username
        '''
        return self.username
    
    def get_ip_address(self):
        '''
        returns user ip address
        '''
        return self.ip_address
    
    def get_uuid(self):
        '''
        returns user uuid
        '''
        return self.uuid
    
    def create_message(self, chatroomID, payload):
        '''
        creates a message
        '''
        message1 = Message(self.username, payload, time.time(), chatroomID, self.uuid)
        return message1.encode_message()

