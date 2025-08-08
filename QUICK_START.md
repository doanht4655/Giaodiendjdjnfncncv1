# 🚀 HƯỚNG DẪN CHẠY NHANH

## Cách 1: Setup Tự Động (Khuyến nghị)
```bash
python3 setup.py
```
- ✅ Tự động kiểm tra Python
- ✅ Cài đặt dependencies
- ✅ Tạo thư mục cần thiết
- ✅ Kiểm tra kết nối mạng
- ✅ Chạy chương trình sau khi setup

## Cách 2: Chạy Trực Tiếp

### Linux/Mac:
```bash
./run.sh          # Hoặc
make run           # Hoặc
python3 main_Version2.py
```

### Windows:
```cmd
run.bat            # Hoặc
python main_Version2.py
```

## Cách 3: Makefile (Linux/Mac)
```bash
make help          # Xem tất cả lệnh
make setup         # Setup và chạy
make run           # Chỉ chạy
make install       # Cài dependencies
make clean         # Dọn dẹp
```

## 🔧 Troubleshooting

### Lỗi permission (Linux/Mac):
```bash
chmod +x run.sh setup.py
```

### Lỗi Python không tìm thấy:
- Cài đặt Python 3.6+
- Windows: Thêm Python vào PATH
- Linux: `sudo apt install python3`
- Mac: `brew install python3`

### Lỗi pip:
```bash
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
```

---
**Tác giả:** Trần Đức Doanh | **Telegram:** https://t.me/doanhvip1
