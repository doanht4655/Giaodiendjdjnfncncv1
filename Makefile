# Makefile cho Tool Manager
# Tác giả: Trần Đức Doanh

.PHONY: setup run install clean help

# Mặc định
help:
	@echo "🛠️  Tool Manager - Trần Đức Doanh"
	@echo "=================================="
	@echo "Các lệnh có sẵn:"
	@echo "  make setup    - Cài đặt và thiết lập"
	@echo "  make run      - Chạy Tool Manager"
	@echo "  make install  - Cài đặt dependencies"
	@echo "  make clean    - Dọn dẹp file tạm"
	@echo "  make help     - Hiển thị trợ giúp này"

# Cài đặt và thiết lập
setup:
	@echo "🔧 Đang thiết lập Tool Manager..."
	@python3 setup.py

# Chạy chương trình
run:
	@echo "🚀 Khởi động Tool Manager..."
	@python3 main_Version2.py

# Cài đặt dependencies
install:
	@echo "📦 Cài đặt dependencies..."
	@pip3 install -r requirements.txt

# Dọn dẹp
clean:
	@echo "🧹 Dọn dẹp file tạm..."
	@rm -rf __pycache__/
	@rm -rf temp/
	@rm -f *.pyc
	@rm -f *.pyo
	@echo "✅ Dọn dẹp hoàn tất!"

# Kiểm tra phiên bản Python
check:
	@echo "🔍 Kiểm tra môi trường..."
	@python3 --version
	@pip3 --version
