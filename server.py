# server.py - Server TCP đơn giản
import socket
import threading

clients = []

def handle_client(conn, addr):
    print(f"[KẾT NỐI] {addr} đã tham gia.")
    while True:
        try:
            msg = conn.recv(1024).decode("utf-8")
            if not msg:
                break
            print(f"[{addr}] {msg}")
            broadcast(f"{addr}: {msg}", conn)
        except:
            break
    conn.close()
    clients.remove(conn)
    print(f"[NGẮT] {addr} rời phòng.")

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message.encode("utf-8"))

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 5555))
    server.listen()
    print("[SERVER] Đang lắng nghe tại 127.0.0.1:5555")

    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
