# chat-client-server
cách chạy:
Bước 1: Chạy Server
     python server.py
Server sẽ chạy ở 127.0.0.1:12345 (có thể chỉnh port trong code nếu cần).
Hiện thông báo: Server listening on port 12345...

Bước 2: Chạy Client
Có 2 cách:
Nếu muốn dùng console:
    python client.py
→ Gõ tin nhắn và thấy server trả về.

Nếu muốn dùng GUI:
    python gui.py
→ Cửa sổ chat xuất hiện, nhập tin nhắn, nhấn gửi.
Mở nhiều lần gui.py (hoặc client.py) để giả lập nhiều người tham gia chat.

3.2. Quy trình chạy demo cho nhóm
Một máy làm server (server.py).
Các máy khác (hoặc nhiều terminal) chạy client/gui.
Nhập tin nhắn → tất cả client khác nhận được qua server.

4. Lưu ý khi test nhóm
Nếu server + client chạy trên cùng máy → dùng 127.0.0.1 (localhost).
Nếu chạy trên mạng LAN (khác máy):
Máy chủ lấy địa chỉ IP thật (VD: 192.168.1.10).
Trong client.py và gui.py, sửa HOST = "127.0.0.1" thành IP đó.
Các máy khác kết nối được qua IP LAN.
