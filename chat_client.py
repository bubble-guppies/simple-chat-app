import socket

HOST = input('Provide server IP address: ')  # The server's hostname or IP address
PORT = int(input('Provide port number: '))  # The port used by the server


def join():
    '''
    Called when client wishes to connect to server.
    '''
    # if type(PORT) is not int:
    #     raise TypeError("Port number must be integer.")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(2048)

    print(f"Received {data!r}")

    pass

def leave():
    '''
    Called when client wishes to disconnect from the server.
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.disconnect((HOST, PORT))

def send_msg(msg: str):
    '''
    Called when client wishes to send a string to the server (msg).
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.send(msg)

if __name__ == "__main__":
    join()
