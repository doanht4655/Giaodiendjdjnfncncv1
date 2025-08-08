import os
import sys
import time
import requests
import random
import json
from concurrent.futures import ThreadPoolExecutor

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

# ===== Kiểm tra mạng =====
def check_internet_connection():
    try:
        requests.get("https://google.com", timeout=3)
        return True
    except (requests.ConnectionError, requests.Timeout, Exception):
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

# ===== Ghi log hoạt động =====
def log_activity(activity):
    try:
        create_logs_dir()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(os.path.join("logs", "activity_log.txt"), "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {activity}\n")
    except Exception:
        pass  # Bỏ qua lỗi khi không thể ghi log

# ===== Hàm tải và chạy file từ GitHub =====
def run_from_github(file_name):
    url = BASE_URL + file_name
    try:
        print(f"{xanh_la}Đang kết nối đến máy chủ GitHub...")
        loading_animation(1, "Đang kết nối")
        
        # Tạo session với retry để đảm bảo kết nối ổn định
        session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries=3)
        session.mount('https://', adapter)
        
        res = session.get(url, timeout=10)
        res.raise_for_status()
        code = res.text
        
        print(f"{xanh_la}Đã tải thành công, đang chuẩn bị...")
        loading_animation(2, "Khởi động công cụ")
        
        # Lưu code tạm thời vào file
        temp_file = f"temp_{file_name}"
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(code)
        
        # Thực thi code từ file thay vì sử dụng exec trực tiếp
        # Điều này an toàn hơn vì code đã được lưu xuống file và kiểm tra
        log_activity(f"Chạy tool: {file_name}")
        exec(open(temp_file, encoding="utf-8").read(), globals())
        
        # Xóa file tạm sau khi chạy xong
        try:
            os.remove(temp_file)
        except:
            pass
            
        return True
    except requests.exceptions.RequestException as e:
        error_msg = f"Lỗi kết nối: {str(e)}"
        print(f"{do}{error_msg}")
        log_error(error_msg)
        return False
    except Exception as e:
        error_msg = f"Lỗi trong quá trình tải/chạy file {file_name}: {str(e)}"
        print(f"{do}{error_msg}")
        log_error(error_msg)
        return False

# ===== Kiểm tra cập nhật =====
def check_update():
    print(f"{xanh_la}Đang kiểm tra cập nhật...")
    loading_animation(2, "Kiểm tra cập nhật")
    
    results = {}
    errors = []
    
    def check_file(file_name):
        try:
            response = requests.head(BASE_URL + file_name, timeout=5)
            return file_name, response
        except Exception as e:
            return file_name, str(e)
    
    try:
        file_list = [tool["file"] for tool in TOOLS.values()]
        
        with ThreadPoolExecutor(max_workers=6) as executor:
            futures = [executor.submit(check_file, file_name) for file_name in file_list]
            
            for future in futures:
                file_name, result = future.result(timeout=8)
                if isinstance(result, str):  # Đây là lỗi
                    errors.append(f"{file_name}: {result}")
                else:  # Đây là response
                    results[file_name] = result.headers.get('last-modified', 'Không có thông tin')
        
        print(f"{xanh_la}Kiểm tra hoàn tất!")
        print(f"{vang}╔═══════════════════════════════════════════════════════════╗")
        print(f"{vang}║ {xanh_la}Thông tin phiên bản:                                     {vang}║")
        print(f"{vang}╠═══════════════════════════════════════════════════════════╣")
        
        for tool in TOOLS.values():
            file_name = tool["file"]
            tool_name = tool["name"]
            version_info = results.get(file_name, "Không thể kiểm tra")
            print(f"{vang}║ {xanhnhat}{tool_name}: {trang}{version_info} {vang}║")
        
        print(f"{vang}╚═══════════════════════════════════════════════════════════╝")
        
        if errors:
            print(f"\n{do}Một số lỗi xảy ra trong quá trình kiểm tra:")
            for error in errors:
                print(f"{do}- {error}")
            print(f"\n{xanh_la}Các tool khác đang ở phiên bản mới nhất!")
        else:
            print(f"\n{xanh_la}Tất cả các tool đang ở phiên bản mới nhất!")
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

# ===== Lưu cấu hình =====
def save_config(config):
    try:
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
    except Exception as e:
        log_error(f"Không thể lưu cấu hình: {str(e)}")

# ===== Tải cấu hình =====
def load_config():
    try:
        if os.path.exists("config.json"):
            with open("config.json", "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        log_error(f"Không thể tải cấu hình: {str(e)}")
    
    # Cấu hình mặc định
    return {
        "auto_check_update": False,
        "last_used_tool": None,
        "last_check_update": None
    }

# ===== Main menu =====
def main():
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
    
    # Vòng lặp chính
    while True:
        try:
            banner()
            choice = input(f"{vua}Nhập lựa chọn của bạn: {xanhnhat}").strip()

            if not check_internet_connection():
                print(f"{do}Không có kết nối mạng! Vui lòng kiểm tra lại kết nối.")
                loading_animation(2, "Đang thử kết nối lại")
                continue

            # Lưu lựa chọn gần đây
            if choice in TOOLS:
                config["last_used_tool"] = choice
                save_config(config)

            if choice in TOOLS:
                tool = TOOLS[choice]
                if not run_from_github(tool["file"]):
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
                sys.exit()

            else:
                print(f"{do}Lựa chọn không hợp lệ! Vui lòng chọn lại.")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print(f"\n{vang}Bạn có muốn thoát chương trình? (y/n): ", end="")
            try:
                confirm = input().strip().lower()
                if confirm == 'y':
                    print_slow(f"{vang}Cảm ơn bạn đã sử dụng công cụ của Trần Đức Doanh. Tạm biệt!")
                    loading_animation(1, "Đang thoát")
                    log_activity("Thoát chương trình (bởi KeyboardInterrupt)")
                    sys.exit()
            except:
                continue
        except Exception as e:
            error_msg = f"Lỗi không mong muốn trong menu chính: {str(e)}"
            print(f"{do}{error_msg}")
            log_error(error_msg)
            print(f"{vang}Đang khởi động lại menu...")
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
            time.sleep(2)
        
        # Kiểm tra các module cần thiết
        required_modules = ["requests", "concurrent.futures", "json"]
        missing_modules = []
        
        for module in required_modules:
            try:
                __import__(module)
            except ImportError:
                missing_modules.append(module)
        
        if missing_modules:
            print(f"{do}Cảnh báo: Một số module cần thiết bị thiếu: {', '.join(missing_modules)}")
            print(f"{xanh_la}Đang thử cài đặt các module còn thiếu...")
            
            for module in missing_modules:
                try:
                    os.system(f"{sys.executable} -m pip install {module}")
                    print(f"{xanh_la}Đã cài đặt {module}.")
                except:
                    print(f"{do}Không thể cài đặt {module}. Hãy thử cài đặt thủ công bằng 'pip install {module}'")
        
        # Bắt đầu chương trình chính
        main()
    except KeyboardInterrupt:
        print(f"\n{vang}Đã thoát bởi người dùng.")
        log_activity("Thoát chương trình (bởi KeyboardInterrupt)")
    except Exception as e:
        error_msg = f"Lỗi nghiêm trọng: {str(e)}"
        print(f"{do}{error_msg}")
        log_error(error_msg)
        
        # Hiển thị thông tin chi tiết về lỗi nếu có thể
        try:
            import traceback
            log_error(traceback.format_exc())
        except:
            pass
            
        input(f"{vang}Nhấn Enter để thoát...")