from message import Message
import socket
import uuid

class Client:
    '''
    creates variables as strings
    '''
    username = ""
    ip_address = ""
    _password = ""
    uuid = ""

    def __init__(self, username, ip_address, password):
        '''
        Initializes variables
        password is protected
        '''
        self.username = username
        self.ip_address = ip_address
        self._password = password
        self.uuid = uuid.uuid4()

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
        message1 = Message(self.username, payload, chatroomID)
        return message1.encode_message()

    def authenticate(self, s: socket) -> bool:
        """
        Attempts to authenticate the client against the server.
        This is done by sending a specific message to the server, of the form:
        '$SENDING_USERDATA$'
        The server then expects the next message to be 'username,password'
        The server then parses this username and password and compares it to the server's stored, obfuscated password for the user.
        If the given password matches with the stored one, then the server sends a string of '$AUTHENTICATED$' back to the client.
        If it does not match, then the server sends '$FAILED$'.
        For more information about startup procedure, refer to README.txt.
        """
        start_msg = "$SENDING_USERDATA$".encode("utf-8")
        s.send(start_msg)
        user_data = f"{self.username},{self._password}".encode("utf-8")
        s.send(user_data)

        auth_status = s.recv(2048).decode("utf-8")
        if auth_status == "$AUTHENTICATED$":
            return True
        elif auth_status == "$FAILED$":
            return False
        else:
            return None

            

