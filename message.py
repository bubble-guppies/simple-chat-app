import json
import uuid


class Message:
    def __init__(self, sender, payload, timestamp, chatroomID, uniqueID):
        self.__sender = sender
        self.__payload = payload
        self.__timestamp = timestamp
        self.__chatroomID = chatroomID
        self.__uniqueID = uniqueID

    def message(self):
        """
        Arranges information about message into displayed message
        :return: String of message
        """
        chatLine = f"({self.__timestamp}) {self.__sender}: {self.__payload}"
        return chatLine

    def get_sender(self):
        """returns username of sender"""
        return self.__sender

    def get_payload(self):
        """returns content of message"""
        return self.__payload

    def get_timestamp(self):
        """returns time that message was sent"""
        return self.__timestamp

    def get_chatroomID(self):
        """returns chatroomID"""
        return self.__chatroomID

    def get_uniqueID(self):
        """returns uniqueID"""
        return self.__uniqueID

    def encode_message(self):
        """Encodes content of other object"""
        message_dict = {
            "sender": self.__sender,
            "payload": self.__payload,
            "timestamp": self.__timestamp,
            "chatroom": self.__chatroomID.int,
            "uuid": self.__uniqueID.int,
        }
        encoded_message = json.dumps(message_dict).encode("utf8")
        return encoded_message


def decode_message(msg):
    """
    Decodes a stringified json (e.g. the output of encode_message) into a Message object.
    """
    json_msg = json.loads(msg)
    return Message(
        json_msg["sender"],
        json_msg["payload"],
        json_msg["timestamp"],
        uuid.UUID(int=json_msg["chatroom"]),
        uuid.UUID(int=json_msg["uuid"]),
    )
