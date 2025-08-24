# gui.py - GUI cho client dùng Tkinter
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode("utf-8")
            chat_box.config(state=tk.NORMAL)
            chat_box.insert(tk.END, msg + "\n")
            chat_box.config(state=tk.DISABLED)
            chat_box.yview(tk.END)
        except:
            break

def send_msg():
    msg = entry.get()
    client.send(msg.encode("utf-8"))
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Chat Client")

chat_box = scrolledtext.ScrolledText(root, state=tk.DISABLED)
chat_box.pack(padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=10)
send_btn = tk.Button(root, text="Gửi", command=send_msg)
send_btn.pack(side=tk.RIGHT, padx=10)

threading.Thread(target=receive, daemon=True).start()

root.mainloop()
