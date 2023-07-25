from message import Message
import datetime
import socket

class Client:
    '''
    creates variables as strings
    '''
    username = ""
    ip_address = ""
    _password = ""
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
        message1 = Message(self.username, payload, datetime.datetime.now().strftime("%a, %H:%M:%S%p"), chatroomID, self.uuid)
        return message1.encode_message()

    def authenticate(self, s: socket) -> bool:
        """
        Attempts to authenticate the client against the server.
        This is done by sending a specific message to the server, of the form:
        '$USERDATA$:username,password'
        The server then parses this username and password and compares it to the server's stored, obfuscated password for the user.
        If the given password matches with the stored one, then the server sends a string of '$AUTHENTICATED$' back to the client.
        If it does not match, then the server sends '$FAILED$'.
        """
        user_data = f"$USERDATA$:{self.username},{self._password}"
        s.send(user_data.encode())

        auth_status = s.recv(1024).decode("utf-8")
        if auth_status == "$AUTHENTICATED$":
            return True
        elif auth_status == "$FAILED$":
            return False
        else:
            return None

            

