#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script setup tự động cho Tool Manager
Tác giả: Trần Đức Doanh
"""

import os
import sys
import subprocess
import platform

# Màu sắc
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

def print_colored(message, color=WHITE):
    """In ra thông báo có màu"""
    print(f"{color}{message}{RESET}")

def print_banner():
    """Hiển thị banner setup"""
    banner = f"""
{CYAN}╔════════════════════════════════════════════════════════════╗
{CYAN}║                     TOOL MANAGER SETUP                    ║
{CYAN}║                  Tác giả: Trần Đức Doanh                  ║
{CYAN}╚════════════════════════════════════════════════════════════╝{RESET}
"""
    print(banner)

def check_python_version():
    """Kiểm tra phiên bản Python"""
    print_colored("🔍 Kiểm tra phiên bản Python...", BLUE)
    python_version = sys.version_info
    
    if python_version < (3, 6):
        print_colored("❌ Cần Python 3.6 trở lên!", RED)
        print_colored(f"   Phiên bản hiện tại: {python_version.major}.{python_version.minor}.{python_version.micro}", RED)
        return False
    else:
        print_colored(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro} - OK", GREEN)
        return True

def install_requirements():
    """Cài đặt các dependencies"""
    print_colored("📦 Cài đặt dependencies...", BLUE)
    
    # Danh sách các package cần thiết
    required_packages = [
        "requests",
        "colorama"
    ]
    
    for package in required_packages:
        try:
            print_colored(f"   Đang cài đặt {package}...", YELLOW)
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", package, "--quiet"
            ])
            print_colored(f"   ✅ {package} đã được cài đặt", GREEN)
        except subprocess.CalledProcessError:
            print_colored(f"   ❌ Không thể cài đặt {package}", RED)
            return False
    
    return True

def create_directories():
    """Tạo các thư mục cần thiết"""
    print_colored("📁 Tạo thư mục cần thiết...", BLUE)
    
    directories = ["logs", "downloads", "temp"]
    
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            print_colored(f"   ✅ Thư mục '{directory}' đã sẵn sàng", GREEN)
        except Exception as e:
            print_colored(f"   ⚠️  Không thể tạo thư mục '{directory}': {e}", YELLOW)

def check_internet_connection():
    """Kiểm tra kết nối mạng"""
    print_colored("🌐 Kiểm tra kết nối mạng...", BLUE)
    
    try:
        import requests
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            print_colored("   ✅ Kết nối mạng OK", GREEN)
            return True
        else:
            print_colored("   ❌ Không có kết nối mạng", RED)
            return False
    except Exception:
        print_colored("   ❌ Không có kết nối mạng", RED)
        return False

def create_run_script():
    """Tạo script chạy nhanh"""
    print_colored("🚀 Tạo script chạy nhanh...", BLUE)
    
    # Script cho Linux/Mac
    if platform.system() != "Windows":
        run_script_content = """#!/bin/bash
# Script chạy nhanh Tool Manager
cd "$(dirname "$0")"
python3 main_Version2.py
"""
        try:
            with open("run.sh", "w", encoding="utf-8") as f:
                f.write(run_script_content)
            os.chmod("run.sh", 0o755)
            print_colored("   ✅ Script 'run.sh' đã được tạo", GREEN)
        except Exception as e:
            print_colored(f"   ⚠️  Không thể tạo run.sh: {e}", YELLOW)
    
    # Script cho Windows
    run_bat_content = """@echo off
cd /d "%~dp0"
python main_Version2.py
pause
"""
    try:
        with open("run.bat", "w", encoding="utf-8") as f:
            f.write(run_bat_content)
        print_colored("   ✅ Script 'run.bat' đã được tạo", GREEN)
    except Exception as e:
        print_colored(f"   ⚠️  Không thể tạo run.bat: {e}", YELLOW)

def update_requirements_txt():
    """Cập nhật file requirements.txt"""
    print_colored("📝 Cập nhật requirements.txt...", BLUE)
    
    requirements_content = """# Dependencies cho Tool Manager
requests>=2.25.0
colorama>=0.4.0
"""
    
    try:
        with open("requirements.txt", "w", encoding="utf-8") as f:
            f.write(requirements_content)
        print_colored("   ✅ requirements.txt đã được cập nhật", GREEN)
    except Exception as e:
        print_colored(f"   ⚠️  Không thể cập nhật requirements.txt: {e}", YELLOW)

def run_main_program():
    """Chạy chương trình chính"""
    print_colored("🎯 Khởi động Tool Manager...", BLUE)
    print_colored("=" * 60, CYAN)
    
    try:
        subprocess.run([sys.executable, "main_Version2.py"])
    except KeyboardInterrupt:
        print_colored("\n👋 Tạm biệt!", YELLOW)
    except Exception as e:
        print_colored(f"❌ Lỗi khi chạy chương trình: {e}", RED)

def main():
    """Hàm chính của setup"""
    print_banner()
    
    # Kiểm tra phiên bản Python
    if not check_python_version():
        input("Nhấn Enter để thoát...")
        return
    
    # Tạo thư mục cần thiết
    create_directories()
    
    # Cài đặt dependencies
    if not install_requirements():
        print_colored("❌ Có lỗi khi cài đặt dependencies!", RED)
        input("Nhấn Enter để tiếp tục (có thể gặp lỗi)...")
    
    # Kiểm tra kết nối mạng
    check_internet_connection()
    
    # Cập nhật requirements.txt
    update_requirements_txt()
    
    # Tạo script chạy nhanh
    create_run_script()
    
    print_colored("\n🎉 Setup hoàn tất!", GREEN)
    print_colored("💡 Cách sử dụng:", CYAN)
    
    if platform.system() != "Windows":
        print_colored("   • Chạy: ./run.sh hoặc python3 main_Version2.py", WHITE)
    else:
        print_colored("   • Chạy: run.bat hoặc python main_Version2.py", WHITE)
    
    print_colored("   • Hoặc: python3 setup.py để setup lại", WHITE)
    
    # Hỏi có muốn chạy ngay không
    try:
        choice = input(f"\n{YELLOW}Bạn có muốn chạy Tool Manager ngay bây giờ? (y/n): {RESET}").lower().strip()
        if choice in ['y', 'yes', 'có', '']:
            run_main_program()
    except KeyboardInterrupt:
        print_colored("\n👋 Tạm biệt!", YELLOW)

if __name__ == "__main__":
    main()
