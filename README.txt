Startup Procedure
When a client wishes to connect to the server, information has to be
exchanged between them to authenticate the user and give the client
up to date information about the chatroom. 
The sequence of messages exchanged between the client and server 
is like this:
    Client> $STARTUP$
    Server> $STARTUP$
    Client> $SENDING_USERDATA$
    Client> <username>,<password>
    Server> $AUTHENTICATED$ *or* $FAILED$
    if authentication is successful:
    Client> $REQUEST_CHATROOM_DATA$
    Server> <chatroom_name>
    Server> <chatroom_id>
    Server> <last_10_messages>
    Client> $END_STARTUP$