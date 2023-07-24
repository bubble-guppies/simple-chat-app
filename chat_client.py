import socket

HOST = input('Provide server IP address: ')  # The server's hostname or IP address
PORT = int(input('Provide port number: '))  # The port used by the server


def join():
    # if type(PORT) is not int:
    #     raise TypeError("Port number must be integer.")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(2048)

    print(f"Received {data!r}")

    pass

def leave():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.disconnect((HOST, PORT))

def send_msg(msg: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.send(msg)

if __name__ == "__main__":
    join()
