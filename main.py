# main.py - Entry point của ứng dụng chat
import threading
import server
import client

if __name__ == "__main__":
    print("Chọn chế độ:")
    print("1. Server")
    print("2. Client")
    choice = input("Nhập số: ")

    if choice == "1":
        server.start_server()
    elif choice == "2":
        client.start_client()
    else:
        print("Lựa chọn không hợp lệ!")
