from time import gmtime
import uuid
import calendar

class Chatroom:
    name = "Generic Room"
    uuid = uuid.uuid4()
    messages = []

    def __init__(self, name):
        self.name = name

    def addMessage(self, message):
        '''Arguments: Message Object
        Functionality: Adds a message to an array of messages sent in a chatroom'''
        if type(message) != str:
            self.messages.append(["Message Error: Not String"])
        else:
            self.messages.append([[message.get_sender()],[message.get_payload()],[calendar.timegm(gmtime)],[self.uuid],[message.get_uniqueID()]])

    def modifyChatroomName(self, name):
        '''Change the name of a chatroom'''
        self.name = name

    def getChatroom(self):
        '''Gets the information of a chatroom in an array 
        (formated x[0] = name x=[1] = uuid)'''
        return [[self.name],[self.uuid]]
    
    def getMessages(self):
        '''Get messages array'''
        return self.messages
    
    def getLastMessageData(self):
        '''Get the last message sent (not text but the object)'''
        return self.messages[len(self.messages)-1]



    