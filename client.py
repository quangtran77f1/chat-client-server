# client.py - Client TCP đơn giản
import socket
import threading

def receive(sock):
    while True:
        try:
            msg = sock.recv(1024).decode("utf-8")
            if msg:
                print(msg)
        except:
            print("[LỖI] Mất kết nối đến server.")
            break

def start_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 5555))

    thread = threading.Thread(target=receive, args=(sock,))
    thread.start()

    while True:
        msg = input("")
        sock.send(msg.encode("utf-8"))
