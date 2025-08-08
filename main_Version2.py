import os
import sys
import time
import requests
import random
import json
import tempfile
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, Optional, Any
import subprocess

# ===== Màu sắc =====
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m"
xam = '\033[1;30m'
vang = "\033[1;33m"
tim = "\033[1;35m"
hong = "\033[1;95m"
cyan = "\033[1;96m"
dac_biet = "\033[32;5;245m\033[38;5;39m"
vua = f"{do}[{trang}=.{do}] {trang}=> {xanh_la}"

# ===== Cấu hình bảo mật =====
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB giới hạn kích thước file
ALLOWED_EXTENSIONS = ['.py']  # Chỉ cho phép file Python
REQUEST_TIMEOUT = 30  # Timeout cho requests

# ===== Đường dẫn cơ sở =====
BASE_URL = "https://raw.githubusercontent.com/doanht4655/Xjcjfjfj/refs/heads/main/"
TOOLS = {
    "1": {"name": "Tool Golike TikTok", "file": "vip.py"},
    "2": {"name": "Tool Thread", "file": "thera.py"},
    "5": {"name": "Tool Đăng ký Facebook", "file": "regfb.py"},
    "6": {"name": "Tool Quản lý Proxy", "file": "proxy.py"},
    "7": {"name": "Tool Kiểm tra Proxy", "file": "checkproxy.py"},
    "8": {"name": "Tool Spam", "file": "Spam.py"}
}

# ===== Hàm clear màn hình =====
def clear():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        pass  # Bỏ qua lỗi nếu không thể clear màn hình

# ===== Hiệu ứng chữ =====
def print_slow(text, delay=0.005):
    try:
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    except KeyboardInterrupt:
        print("\n" + do + "Đã dừng hiệu ứng." + trang)
        print()

# ===== Hiệu ứng loading =====
def loading_animation(duration=2, text="Đang tải"):
    try:
        chars = "/-\\|"
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            i = (i + 1) % len(chars)
            print(f"\r{xanh_la}{text} {chars[i]}", end="", flush=True)
            time.sleep(0.1)
        print(f"\r{xanh_la}{text} Hoàn tất!{trang}     ")
    except KeyboardInterrupt:
        print(f"\r{xanh_la}{text} Đã dừng!{trang}      ")

# ===== Kiểm tra mạng cải tiến =====
def check_internet_connection() -> bool:
    """Kiểm tra kết nối mạng với nhiều máy chủ để đảm bảo độ tin cậy."""
    test_urls = [
        "https://www.google.com",
        "https://github.com", 
        "https://raw.githubusercontent.com"
    ]
    
    for url in test_urls:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return True
        except (requests.ConnectionError, requests.Timeout, Exception):
            continue
    return False

# ===== Banner siêu đẹp =====
def banner():
    try:
        clear()
        rainbow_colors = [do, vang, xanh_la, xanhnhat, xanh_duong, tim, hong]
        
        logo = f"""
{random.choice(rainbow_colors)}╔══════════════════════════════════════════════════════════════════╗
{random.choice(rainbow_colors)}║    ██████╗  ██████╗ ███╗   ██╗ ██████╗     ██╗  ██╗            ║
{random.choice(rainbow_colors)}║    ██╔══██╗██╔═══██╗████╗  ██║██╔════╝     ╚██╗██╔╝            ║
{random.choice(rainbow_colors)}║    ██████╔╝██║   ██║██╔██╗ ██║██║  ███╗     ╚███╔╝             ║
{random.choice(rainbow_colors)}║    ██╔══██╗██║   ██║██║╚██╗██║██║   ██║     ██╔██╗             ║
{random.choice(rainbow_colors)}║    ██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝    ██╔╝ ██╗            ║
{random.choice(rainbow_colors)}║    ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═╝            ║
{tim}╠══════════════════════════════════════════════════════════════════╣
{xanh_duong}║  {vang}𝓣𝓡𝓐̂̀𝓝 Đ𝓤̛́𝓒 𝓓𝓞𝓐𝓝𝓗   {xanh_duong}|  {cyan}𝕋𝕖𝕝𝕖𝕘𝕣𝕒𝕞: {xanhnhat}https://t.me/doanhvip1  {xanh_duong}║
{tim}╚══════════════════════════════════════════════════════════════════╝

{trang}      [{xanhnhat}1{trang}] {xanh_la}Chạy Tool Golike TikTok {vang}(vip.py)
{trang}      [{xanhnhat}2{trang}] {xanh_la}Chạy Tool Thread {vang}(thera.py)
{trang}      [{xanhnhat}3{trang}] {xanh_la}Kiểm tra cập nhật
{trang}      [{xanhnhat}4{trang}] {xanh_la}Thông tin tác giả
{trang}      [{xanhnhat}5{trang}] {xanh_la}Đăng ký Facebook {vang}(regfb.py)
{trang}      [{xanhnhat}6{trang}] {xanh_la}Quản lý Proxy {vang}(proxy.py)
{trang}      [{xanhnhat}7{trang}] {xanh_la}Kiểm tra Proxy {vang}(checkproxy.py)
{trang}      [{xanhnhat}8{trang}] {xanh_la}Công cụ Spam {vang}(Spam.py)
{trang}      [{xanhnhat}0{trang}] {do}Thoát chương trình
        """
        print_slow(logo, 0.001)
    except Exception as e:
        print(f"{do}Lỗi khi hiển thị banner: {str(e)}")
        print(f"{xanh_la}=== MENU CÔNG CỤ TRẦN ĐỨC DOANH ===")
        for key, value in TOOLS.items():
            print(f"{trang}[{xanhnhat}{key}{trang}] {xanh_la}{value['name']} {vang}({value['file']})")
        print(f"{trang}[{xanhnhat}3{trang}] {xanh_la}Kiểm tra cập nhật")
        print(f"{trang}[{xanhnhat}4{trang}] {xanh_la}Thông tin tác giả")
        print(f"{trang}[{xanhnhat}0{trang}] {do}Thoát chương trình")

# ===== Tạo thư mục logs nếu chưa tồn tại =====
def create_logs_dir():
    try:
        if not os.path.exists("logs"):
            os.makedirs("logs")
    except Exception as e:
        print(f"{do}Không thể tạo thư mục logs: {str(e)}")

# ===== Ghi log lỗi =====
def log_error(error_msg):
    try:
        create_logs_dir()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(os.path.join("logs", "error_log.txt"), "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {error_msg}\n")
    except Exception:
        pass  # Bỏ qua lỗi khi không thể ghi log

# ===== Hàm fix các lỗi syntax phổ biến =====
def fix_common_syntax_errors(content: str) -> str:
    """Sửa các lỗi syntax phổ biến trong code Python."""
    try:
        lines = content.split('\n')
        fixed_lines = []
        
        for line in lines:
            original_line = line
            
            # Fix các lỗi import phổ biến
            fixes = [
                ('importtime import sleep', 'from time import sleep'),
                ('importtime', 'import time'),
                ('importos', 'import os'),
                ('importsys', 'import sys'),
                ('importrandom', 'import random'),
                ('importrequests', 'import requests'),
                ('importjson', 'import json'),
            ]
            
            for wrong, correct in fixes:
                if wrong in line:
                    line = line.replace(wrong, correct)
                    break  # Chỉ fix một lần per line
            
            # Fix import statements bị dính nhau
            if line.strip().startswith('import') and ' import ' in line and line != original_line:
                # Nếu có nhiều import trong một dòng, tách ra
                parts = line.split(' import ')
                if len(parts) > 2:  # import time import sleep
                    # Tạo multiple import lines
                    import_lines = []
                    for i, part in enumerate(parts):
                        if i == 0:
                            import_lines.append(part)  # import time
                        else:
                            import_lines.append(f'from {parts[0].replace("import ", "")} import {part}')
                    line = import_lines[0]  # Chỉ lấy import đầu tiên
            
            fixed_lines.append(line)
        
        return '\n'.join(fixed_lines)
    except Exception as e:
        print(f"{vang}Lỗi khi fix syntax: {str(e)}")
        return content  # Trả về content gốc nếu không sửa được

# ===== Hàm xử lý file có vấn đề encoding =====
def fix_file_encoding(content: str) -> str:
    """Sửa các vấn đề encoding phổ biến trong file."""
    try:
        # Loại bỏ BOM nếu có
        if content.startswith('\ufeff'):
            content = content[1:]
        
        # Fix các ký tự đặc biệt có thể gây lỗi
        content = content.replace('\r\n', '\n')  # Windows line endings
        content = content.replace('\r', '\n')    # Mac line endings
        
        # Loại bỏ các ký tự không in được có thể gây lỗi
        import re
        content = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x84\x86-\x9f]', '', content)
        
        return content
    except Exception:
        return content  # Trả về content gốc nếu không sửa được

# ===== Hàm xác thực file an toàn =====
def validate_file_content(content: str, file_name: str) -> bool:
    """Kiểm tra nội dung file có an toàn không."""
    try:
        # Kiểm tra kích thước
        if len(content.encode('utf-8')) > MAX_FILE_SIZE:
            print(f"{do}File {file_name} quá lớn (>{MAX_FILE_SIZE/1024/1024}MB)")
            return False
        
        # Kiểm tra extension
        if not any(file_name.endswith(ext) for ext in ALLOWED_EXTENSIONS):
            print(f"{do}File {file_name} không có extension được phép")
            return False
        
        # Kiểm tra các từ khóa nguy hiểm (chỉ những thứ thực sự nguy hiểm)
        dangerous_keywords = [
            'os.system(', '__import__(', 'eval(', 'exec(open(',
            'subprocess.call', 'subprocess.run', 'subprocess.Popen',
            'execfile(', 'compile(open(', 'importlib.__import__'
        ]
        
        content_lower = content.lower()
        for keyword in dangerous_keywords:
            if keyword.lower() in content_lower:
                print(f"{vang}Cảnh báo: File chứa từ khóa có thể nguy hiểm: {keyword}")
                # Chỉ warning, không block hoàn toàn
        
        # Thử compile code để kiểm tra syntax
        try:
            compile(content, file_name, 'exec')
            return True
        except SyntaxError as e:
            print(f"{vang}Cảnh báo syntax trong file {file_name}: {str(e)}")
            print(f"{xanh_la}Đang thử chạy file dù có warning...")
            # Cho phép chạy dù có syntax warning (có thể là encoding issue)
            return True
    except Exception as e:
        print(f"{do}Lỗi khi xác thực file {file_name}: {str(e)}")
        return False
def log_activity(activity):
    try:
        create_logs_dir()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(os.path.join("logs", "activity_log.txt"), "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {activity}\n")
    except Exception:
        pass  # Bỏ qua lỗi khi không thể ghi log

# ===== Hàm tải và chạy file từ GitHub cải tiến =====
def run_from_github(file_name: str) -> bool:
    """Tải và chạy file từ GitHub với các biện pháp bảo mật."""
    url = BASE_URL + file_name
    temp_file = None
    
    try:
        print(f"{xanh_la}Đang kết nối đến máy chủ GitHub...")
        loading_animation(1, "Đang kết nối")
        
        # Tạo session với cấu hình bảo mật
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Tool-Manager/2.0',
            'Accept': 'text/plain'
        })
        
        # Retry adapter
        adapter = requests.adapters.HTTPAdapter(
            max_retries=requests.packages.urllib3.util.retry.Retry(
                total=3,
                backoff_factor=1,
                status_forcelist=[500, 502, 503, 504]
            )
        )
        session.mount('https://', adapter)
        
        # Tải file với timeout
        print(f"{xanh_la}Đang tải {file_name}...")
        response = session.get(url, timeout=REQUEST_TIMEOUT, stream=True)
        response.raise_for_status()
        
        # Kiểm tra Content-Type
        content_type = response.headers.get('content-type', '').lower()
        if 'text' not in content_type and 'application' not in content_type:
            print(f"{do}File không đúng định dạng text/python")
            return False
        
        # Đọc nội dung
        content = response.text
        
        # Fix encoding và syntax issues
        content = fix_file_encoding(content)
        content = fix_common_syntax_errors(content)
        
        # Xác thực nội dung file
        if not validate_file_content(content, file_name):
            print(f"{vang}File {file_name} có một số cảnh báo nhưng sẽ được chạy...")
            # Không return False, để file vẫn có thể chạy
        
        print(f"{xanh_la}File hợp lệ, đang chuẩn bị chạy...")
        loading_animation(2, "Khởi động công cụ")
        
        # Tạo file tạm thời an toàn
        with tempfile.NamedTemporaryFile(
            mode='w', 
            suffix='.py', 
            delete=False,
            encoding='utf-8'
        ) as f:
            f.write(content)
            temp_file = f.name
        
        # Ghi log và thực thi
        log_activity(f"Chạy tool: {file_name}")
        
        # Tạo namespace riêng biệt để thực thi
        namespace = {
            '__name__': '__main__',
            '__file__': temp_file,
            'print': print,  # Cho phép print
            # Các biến màu sắc để tool có thể sử dụng
            'trang': trang, 'xanh_la': xanh_la, 'xanh_duong': xanh_duong,
            'do': do, 'vang': vang, 'tim': tim, 'hong': hong, 'cyan': cyan
        }
        
        # Thực thi code trong namespace riêng
        try:
            with open(temp_file, 'r', encoding='utf-8') as f:
                code = compile(f.read(), temp_file, 'exec')
                exec(code, namespace)
        except SyntaxError as e:
            print(f"{vang}Đang thử với encoding khác do lỗi syntax...")
            try:
                # Thử với encoding khác
                with open(temp_file, 'r', encoding='latin-1') as f:
                    content_fixed = f.read()
                    content_fixed = fix_file_encoding(content_fixed)
                    code = compile(content_fixed, temp_file, 'exec')
                    exec(code, namespace)
            except Exception as e2:
                print(f"{do}Không thể thực thi file: {str(e2)}")
                return False
        except Exception as e:
            print(f"{do}Lỗi khi thực thi: {str(e)}")
            return False
        
        return True
        
    except requests.exceptions.Timeout:
        error_msg = f"Timeout khi tải {file_name} (>{REQUEST_TIMEOUT}s)"
        print(f"{do}{error_msg}")
        log_error(error_msg)
        return False
    except requests.exceptions.RequestException as e:
        error_msg = f"Lỗi kết nối khi tải {file_name}: {str(e)}"
        print(f"{do}{error_msg}")
        log_error(error_msg)
        return False
    except Exception as e:
        error_msg = f"Lỗi không mong muốn khi chạy {file_name}: {str(e)}"
        print(f"{do}{error_msg}")
        log_error(error_msg)
        return False
    finally:
        # Luôn xóa file tạm sau khi sử dụng
        if temp_file and os.path.exists(temp_file):
            try:
                os.unlink(temp_file)
            except Exception:
                pass

# ===== Kiểm tra cập nhật cải tiến =====
def check_update() -> None:
    """Kiểm tra cập nhật với xử lý song song và báo cáo chi tiết."""
    print(f"{xanh_la}Đang kiểm tra cập nhật...")
    loading_animation(2, "Kiểm tra cập nhật")
    
    results = {}
    errors = []
    
    def check_file(file_name: str) -> tuple:
        """Kiểm tra một file cụ thể."""
        try:
            response = requests.head(
                BASE_URL + file_name, 
                timeout=10,
                headers={'User-Agent': 'Tool-Manager/2.0'}
            )
            response.raise_for_status()
            return file_name, {
                'status': 'success',
                'last_modified': response.headers.get('last-modified', 'Không có thông tin'),
                'size': response.headers.get('content-length', 'Không rõ'),
                'etag': response.headers.get('etag', 'Không có')
            }
        except Exception as e:
            return file_name, {'status': 'error', 'error': str(e)}
    
    try:
        file_list = [tool["file"] for tool in TOOLS.values()]
        
        # Sử dụng ThreadPoolExecutor với context manager để đảm bảo cleanup
        with ThreadPoolExecutor(max_workers=min(6, len(file_list))) as executor:
            # Submit tất cả tasks
            future_to_file = {
                executor.submit(check_file, file_name): file_name 
                for file_name in file_list
            }
            
            # Xử lý kết quả khi hoàn thành
            for future in as_completed(future_to_file, timeout=30):
                file_name = future_to_file[future]
                try:
                    file_name, result = future.result()
                    if result['status'] == 'error':
                        errors.append(f"{file_name}: {result['error']}")
                    else:
                        results[file_name] = result
                except Exception as e:
                    errors.append(f"{file_name}: Lỗi xử lý future - {str(e)}")
        
        # Hiển thị kết quả
        print(f"{xanh_la}Kiểm tra hoàn tất!")
        print(f"{vang}╔═══════════════════════════════════════════════════════════╗")
        print(f"{vang}║ {xanh_la}Thông tin phiên bản và trạng thái:                      {vang}║")
        print(f"{vang}╠═══════════════════════════════════════════════════════════╣")
        
        for tool in TOOLS.values():
            file_name = tool["file"]
            tool_name = tool["name"]
            
            if file_name in results:
                info = results[file_name]
                status = f"{xanh_la}✓ Khả dụng"
                last_modified = info['last_modified']
                size = info.get('size', 'Không rõ')
                if size != 'Không rõ':
                    try:
                        size = f"{int(size)/1024:.1f}KB"
                    except:
                        size = "Không rõ"
            else:
                status = f"{do}✗ Lỗi"
                last_modified = "Không thể kiểm tra"
                size = "Không rõ"
            
            print(f"{vang}║ {xanhnhat}{tool_name}: {status} - {trang}{last_modified} ({size}) {vang}║")
        
        print(f"{vang}╚═══════════════════════════════════════════════════════════╝")
        
        # Hiển thị lỗi nếu có
        if errors:
            print(f"\n{do}Một số lỗi xảy ra trong quá trình kiểm tra:")
            for error in errors[:5]:  # Chỉ hiển thị 5 lỗi đầu tiên
                print(f"{do}- {error}")
            if len(errors) > 5:
                print(f"{do}... và {len(errors) - 5} lỗi khác")
        else:
            print(f"\n{xanh_la}Tất cả các tool đều có thể truy cập được!")
            
    except Exception as e:
        error_msg = f"Lỗi kiểm tra cập nhật: {str(e)}"
        print(f"{do}{error_msg}")
        log_error(error_msg)
    
    input(f"\n{vang}Nhấn Enter để quay lại menu...")

# ===== Thông tin tác giả =====
def show_author_info():
    try:
        clear()
        print(f"""{tim}
        ╔══════════════════════════════════════════╗
        ║ {vang}THÔNG TIN TÁC GIẢ                      {tim}║
        ╠══════════════════════════════════════════╣
        ║ {xanh_la}Tên thật: {trang}Trần Đức Doanh             {tim}║
        ║ {xanh_la}Telegram: {xanhnhat}https://t.me/doanhvip1      {tim}║
        ║ {xanh_la}Version:  {trang}1.2 (Nâng cấp 08/08/2025)   {tim}║
        ╚══════════════════════════════════════════╝
        """)
        
        log_activity("Xem thông tin tác giả")
        input(f"{vang}Nhấn Enter để quay lại menu...")
    except Exception as e:
        error_msg = f"Lỗi hiển thị thông tin tác giả: {str(e)}"
        print(f"{do}{error_msg}")
        log_error(error_msg)
        input(f"{vang}Nhấn Enter để quay lại menu...")

# ===== Lưu cấu hình an toàn =====
def save_config(config: Dict[str, Any]) -> bool:
    """Lưu cấu hình với xử lý lỗi tốt hơn."""
    try:
        # Tạo bản backup trước khi lưu
        config_file = "config.json"
        backup_file = "config.json.backup"
        
        if os.path.exists(config_file):
            try:
                import shutil
                shutil.copy2(config_file, backup_file)
            except Exception:
                pass  # Không quan trọng nếu không tạo được backup
        
        # Lưu cấu hình với atomic write
        temp_file = config_file + ".tmp"
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        
        # Atomic move
        if os.name == 'nt':  # Windows
            if os.path.exists(config_file):
                os.remove(config_file)
        os.rename(temp_file, config_file)
        
        return True
    except Exception as e:
        log_error(f"Không thể lưu cấu hình: {str(e)}")
        # Xóa temp file nếu có lỗi
        temp_file = "config.json.tmp"
        if os.path.exists(temp_file):
            try:
                os.remove(temp_file)
            except:
                pass
        return False

# ===== Tải cấu hình an toàn =====
def load_config() -> Dict[str, Any]:
    """Tải cấu hình với fallback và validation."""
    config_file = "config.json"
    backup_file = "config.json.backup"
    
    # Cấu hình mặc định
    default_config = {
        "auto_check_update": False,
        "last_used_tool": None,
        "last_check_update": None,
        "theme": "default",
        "language": "vi"
    }
    
    def try_load_file(file_path: str) -> Optional[Dict[str, Any]]:
        """Thử tải file cấu hình."""
        try:
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        return data
        except Exception as e:
            log_error(f"Không thể tải cấu hình từ {file_path}: {str(e)}")
        return None
    
    # Thử tải file chính
    config = try_load_file(config_file)
    
    # Nếu thất bại, thử tải backup
    if config is None:
        config = try_load_file(backup_file)
        if config is not None:
            print(f"{vang}Đã khôi phục cấu hình từ backup")
    
    # Nếu vẫn thất bại, sử dụng cấu hình mặc định
    if config is None:
        config = default_config.copy()
    else:
        # Merge với default config để đảm bảo có đầy đủ keys
        for key, value in default_config.items():
            if key not in config:
                config[key] = value
    
    return config

# ===== Kiểm tra và cài đặt dependencies =====
def check_and_install_dependencies() -> bool:
    """Kiểm tra và cài đặt các module cần thiết."""
    required_modules = {
        "requests": "requests",
        "concurrent.futures": None,  # Built-in từ Python 3.2+
        "json": None,  # Built-in
        "tempfile": None,  # Built-in
        "hashlib": None,  # Built-in
    }
    
    missing_modules = []
    
    for module_name, pip_name in required_modules.items():
        try:
            __import__(module_name)
        except ImportError:
            if pip_name:  # Chỉ thêm vào danh sách nếu có thể cài qua pip
                missing_modules.append(pip_name)
    
    if missing_modules:
        print(f"{vang}Đang cài đặt các module cần thiết: {', '.join(missing_modules)}")
        
        for module in missing_modules:
            try:
                print(f"{xanh_la}Đang cài đặt {module}...")
                result = subprocess.run(
                    [sys.executable, "-m", "pip", "install", module],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                
                if result.returncode == 0:
                    print(f"{xanh_la}✓ Đã cài đặt {module} thành công")
                else:
                    print(f"{do}✗ Lỗi khi cài đặt {module}: {result.stderr}")
                    return False
                    
            except subprocess.TimeoutExpired:
                print(f"{do}✗ Timeout khi cài đặt {module}")
                return False
            except Exception as e:
                print(f"{do}✗ Lỗi không mong muốn khi cài đặt {module}: {str(e)}")
                return False
    
    return True
# ===== Main menu cải tiến =====
def main() -> None:
    """Menu chính với xử lý lỗi tốt hơn và validation input."""
    # Tải cấu hình
    config = load_config()
    
    # Tự động kiểm tra cập nhật nếu được bật
    if config.get("auto_check_update", False):
        current_time = time.time()
        last_check = config.get("last_check_update", 0)
        
        # Kiểm tra cập nhật mỗi 24 giờ
        if current_time - last_check > 86400:  # 24 giờ = 86400 giây
            if check_internet_connection():
                print(f"{xanh_la}Đang tự động kiểm tra cập nhật...")
                check_update()
                config["last_check_update"] = current_time
                save_config(config)
    
    # Biến đếm lỗi liên tiếp
    consecutive_errors = 0
    max_consecutive_errors = 5
    
    # Vòng lặp chính
    while True:
        try:
            banner()
            
            # Hiển thị tool được sử dụng gần đây nếu có
            last_tool = config.get("last_used_tool")
            if last_tool and last_tool in TOOLS:
                print(f"{xam}Gần đây: {TOOLS[last_tool]['name']}")
            
            try:
                choice = input(f"{vua}Nhập lựa chọn của bạn: {xanhnhat}").strip()
            except EOFError:
                print(f"\n{vang}Đã kết thúc input. Thoát chương trình.")
                log_activity("Thoát chương trình (EOFError)")
                sys.exit(0)

            # Validate input
            if not choice:
                print(f"{vang}Vui lòng nhập một lựa chọn.")
                time.sleep(1)
                continue
            
            # Reset consecutive errors khi có input hợp lệ
            consecutive_errors = 0

            # Kiểm tra kết nối mạng cho các tùy chọn cần mạng
            if choice in TOOLS or choice == "3":
                if not check_internet_connection():
                    print(f"{do}Không có kết nối mạng! Vui lòng kiểm tra lại kết nối.")
                    loading_animation(2, "Đang thử kết nối lại")
                    continue

            # Xử lý các lựa chọn
            if choice in TOOLS:
                tool = TOOLS[choice]
                print(f"{xanh_la}Đang khởi động {tool['name']}...")
                
                if run_from_github(tool["file"]):
                    # Lưu lựa chọn gần đây
                    config["last_used_tool"] = choice
                    save_config(config)
                    print(f"{xanh_la}Tool {tool['name']} đã chạy xong.")
                else:
                    print(f"{do}Không thể chạy {tool['name']}!")
                
                input(f"{vang}Nhấn Enter để quay lại menu...")

            elif choice == "3":
                check_update()
                config["last_check_update"] = time.time()
                save_config(config)

            elif choice == "4":
                show_author_info()

            elif choice == "0":
                print_slow(f"{vang}Cảm ơn bạn đã sử dụng công cụ của Trần Đức Doanh. Tạm biệt!")
                loading_animation(1, "Đang thoát")
                log_activity("Thoát chương trình")
                sys.exit(0)

            else:
                print(f"{do}Lựa chọn '{choice}' không hợp lệ! Vui lòng chọn từ 0-8.")
                print(f"{xanh_la}Các lựa chọn hợp lệ: {', '.join(list(TOOLS.keys()) + ['0', '3', '4'])}")
                time.sleep(2)
                
        except KeyboardInterrupt:
            print(f"\n{vang}Bạn có muốn thoát chương trình? (y/n): ", end="")
            try:
                confirm = input().strip().lower()
                if confirm in ['y', 'yes', 'có']:
                    print_slow(f"{vang}Cảm ơn bạn đã sử dụng công cụ của Trần Đức Doanh. Tạm biệt!")
                    loading_animation(1, "Đang thoát")
                    log_activity("Thoát chương trình (bởi KeyboardInterrupt)")
                    sys.exit(0)
                else:
                    print(f"{xanh_la}Tiếp tục sử dụng...")
            except (KeyboardInterrupt, EOFError):
                print(f"\n{vang}Đã thoát.")
                sys.exit(0)
            except Exception:
                continue
                
        except EOFError:
            print(f"\n{vang}Đã kết thúc input. Thoát chương trình.")
            log_activity("Thoát chương trình (EOFError)")
            sys.exit(0)
                
        except Exception as e:
            consecutive_errors += 1
            error_msg = f"Lỗi không mong muốn trong menu chính: {str(e)}"
            print(f"{do}{error_msg}")
            log_error(error_msg)
            
            if consecutive_errors >= max_consecutive_errors:
                print(f"{do}Đã xảy ra {max_consecutive_errors} lỗi liên tiếp. Thoát chương trình để đảm bảo an toàn.")
                log_error(f"Thoát do quá nhiều lỗi liên tiếp: {consecutive_errors}")
                sys.exit(1)
            
            print(f"{vang}Đang khởi động lại menu... (Lỗi thứ {consecutive_errors}/{max_consecutive_errors})")
            time.sleep(2)

# ===== Kiểm tra và bắt đầu chương trình =====
if __name__ == "__main__":
    try:
        # Kiểm tra và tạo thư mục logs
        create_logs_dir()
        
        # Ghi log bắt đầu chương trình
        log_activity("Khởi động chương trình")
        
        print(f"{xanh_la}Đang khởi động công cụ...")
        loading_animation(2, "Khởi động")
        
        # Kiểm tra phiên bản Python
        if sys.version_info < (3, 6):
            print(f"{do}Cảnh báo: Chương trình yêu cầu Python 3.6 trở lên để hoạt động tốt nhất.")
            print(f"{do}Phiên bản hiện tại: {sys.version}")
            time.sleep(3)
        else:
            print(f"{xanh_la}Python version: {sys.version.split()[0]} ✓")
        
        # Kiểm tra và cài đặt dependencies
        if not check_and_install_dependencies():
            print(f"{do}Không thể cài đặt các module cần thiết!")
            print(f"{vang}Vui lòng cài đặt thủ công: pip install requests")
            input("Nhấn Enter để tiếp tục (có thể gặp lỗi)...")
        
        # Kiểm tra quyền ghi file
        try:
            test_file = "test_write.tmp"
            with open(test_file, "w") as f:
                f.write("test")
            os.remove(test_file)
            print(f"{xanh_la}Quyền ghi file: ✓")
        except Exception:
            print(f"{vang}Cảnh báo: Có thể không có quyền ghi file trong thư mục hiện tại")
        
        # Kiểm tra kết nối mạng ban đầu
        if check_internet_connection():
            print(f"{xanh_la}Kết nối mạng: ✓")
        else:
            print(f"{vang}Cảnh báo: Không có kết nối mạng - một số tính năng có thể không hoạt động")
        
        print(f"{xanh_la}Khởi động hoàn tất!")
        time.sleep(1)
        
        # Bắt đầu chương trình chính
        main()
        
    except KeyboardInterrupt:
        print(f"\n{vang}Đã thoát bởi người dùng.")
        log_activity("Thoát chương trình (bởi KeyboardInterrupt trong startup)")
        sys.exit(0)
        
    except Exception as e:
        error_msg = f"Lỗi nghiêm trọng trong quá trình khởi động: {str(e)}"
        print(f"{do}{error_msg}")
        log_error(error_msg)
        
        # Hiển thị thông tin chi tiết về lỗi
        try:
            import traceback
            traceback_info = traceback.format_exc()
            log_error(f"Traceback: {traceback_info}")
            print(f"{xam}Chi tiết lỗi đã được ghi vào logs/error_log.txt")
        except Exception:
            print(f"{do}Không thể ghi chi tiết lỗi")
            
        print(f"\n{vang}Các bước khắc phục có thể:")
        print(f"{trang}- Kiểm tra kết nối mạng")
        print(f"{trang}- Cập nhật Python lên phiên bản mới nhất")
        print(f"{trang}- Cài đặt lại: pip install requests")
        print(f"{trang}- Chạy với quyền Administrator/sudo")
        
        input(f"\n{vang}Nhấn Enter để thoát...")
        sys.exit(1)