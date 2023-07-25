import json
import datetime
import uuid


class Message:
    def __init__(self, sender, payload, chatroomID, timestamp = datetime.datetime.now().strftime("%a, %H:%M:%S%p"), uniqueID=uuid.uuid4()):
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
    try:
        sender = json_msg["sender"]
    except Exception as e:
        sender = "null"
    try:
        payload = json_msg["payload"]
    except Exception as e:
        payload = "null"
    try:
        timestamp = json_msg["timestamp"]
    except Exception as e:
        timestamp = "null"
    try:
        chatroom_id = json_msg["chatroom"]
    except Exception as e:
        chatroom_id = 0
    try:
        msg_id = json_msg["uuid"]
    except Exception as e:
        msg_id = 0
    return Message(
        sender, payload, chatroom_id, timestamp, msg_id
    )
