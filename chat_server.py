from server import Server

if __name__ == "__main__":
    
    PORT = int(input('Provide port number: '))  # The port used by the server
    CHATNAME = input('Chat Name: ')  # The port used by the server

    Server("", PORT, CHATNAME)

