import json
class Message:
    def __init__(self,sender, payload, timestamp, chatroomID, uniqueID):
        self.__sender = sender
        self.__payload = payload
        self.__timestamp = timestamp
        self.__chatroomID = chatroomID
        self.__uniqueID = uniqueID
    def message(self):
        '''
        Arranges information about message into displayed message
        :return: String of message
        '''
        chatLine = "(" + self.__timestamp + ") " + self.__sender + ": " + self.__payload
        return chatLine
    
    def get_sender(self):
        '''returns username of sender'''
        return self.__sender
    
    def get_payload(self):
        '''returns content of message'''
        return self.__payload
    
    def get_timestamp(self):
        '''returns time that message was sent'''
        return self.__timestamp
    
    def get_chatroomID(self):
        '''returns chatroomID'''
        return self.__chatroomID
    
    def get_uniqueID(self):
        '''returns uniqueID'''
        return self.__uniqueID
        
    def encode_message(self):
        '''Encodes content of other object'''
        encoded_message = self.__payload.encode("utf-8") # json.dumps(self).encode('utf8')
        return encoded_message