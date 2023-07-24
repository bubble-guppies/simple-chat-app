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
        if type(message) != str:
            self.messages.append(["Message Error: Not String"])
        else:
            self.messages.append([[message.get_sender()],[message.get_payload()],[calendar.timegm(gmtime)],[self.uuid],[message.get_uniqueID()]])

    def modifyChatroomName(self, name):
        self.name = name

    def getChatroom(self):
        return [[self.name],[self.uuid]]
    
    def getMessages(self):
        return self.messages
    
    def getLastMessageData(self):
        return self.messages[len(self.messages)-1]



    