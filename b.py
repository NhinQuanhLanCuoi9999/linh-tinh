import subprocess
import threading
import ipaddress
from queue import Queue
import platform
import re
import os

def ping_device(ip):
    """
    Ping một địa chỉ IP để kiểm tra xem nó có thể giao tiếp không.
    """
    try:
        if platform.system().lower() == "windows":
            cmd = ["ping", "-n", "1", "-w", "1000", ip]  # Windows
        else:
            cmd = ["ping", "-c", "1", "-W", "1", ip]  # Linux/macOS

        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception:
        return False

def get_mac_from_arp(ip):
    """
    Lấy địa chỉ MAC từ bảng ARP của một địa chỉ IP.
    """
    try:
        if platform.system().lower() == "windows":
            cmd = f"arp -a {ip}"
        else:
            cmd = f"arp -n {ip}"
        result = subprocess.check_output(cmd, shell=True).decode()
        match = re.search(r"([a-fA-F0-9-:]{17})", result)
        return match.group(1) if match else "Không tìm thấy MAC."
    except Exception as e:
        return f"Lỗi khi lấy MAC: {e}"

def worker_ping(ip_queue, reachable_ips):
    """
    Worker để xử lý việc ping từng IP từ hàng đợi.
    """
    while not ip_queue.empty():
        ip = ip_queue.get()
        if ping_device(ip):
            reachable_ips.append(ip)
        ip_queue.task_done()

def worker_fetch_mac(ip_queue, mac_results):
    """
    Worker để lấy địa chỉ MAC của các IP từ hàng đợi.
    """
    while not ip_queue.empty():
        ip = ip_queue.get()
        mac = get_mac_from_arp(ip)
        mac_results.append((ip, mac))
        ip_queue.task_done()

def scan_network(start_ip, prefix):
    """
    Quét mạng, hiển thị IP có thể giao tiếp và lấy địa chỉ MAC.
    """
    reachable_ips = []
    ip_queue = Queue()

    # Xây dựng hàng đợi IP từ dải mạng
    network = ipaddress.IPv4Network(f"{start_ip}/{prefix}", strict=False)
    for ip in network.hosts():
        ip_queue.put(str(ip))

    # Bước 1: Ping tất cả các IP để xác định IP giao tiếp được
    print("[ĐANG QUÉT] Kiểm tra IP có thể giao tiếp...")
    threads = []
    for _ in range(10):  # Số luồng song song
        thread = threading.Thread(target=worker_ping, args=(ip_queue, reachable_ips))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    # Hiển thị các IP giao tiếp được
    os.system("cls" if platform.system().lower() == "windows" else "clear")
    if not reachable_ips:
        print("[THÔNG BÁO] Không có IP nào có thể giao tiếp.")
        return

    print("[KẾT QUẢ] Các IP có thể giao tiếp:")
    for ip in reachable_ips:
        print(f" - {ip}")

    # Bước 2: Lấy địa chỉ MAC của các IP giao tiếp được
    print("\n[ĐANG XỬ LÝ] Lấy địa chỉ MAC từ các IP...")
    mac_results = []
    ip_queue = Queue()
    for ip in reachable_ips:
        ip_queue.put(ip)

    threads = []
    for _ in range(10):  # Số luồng song song
        thread = threading.Thread(target=worker_fetch_mac, args=(ip_queue, mac_results))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    # Hiển thị kết quả MAC
    print("\n[KẾT QUẢ] Địa chỉ MAC:")
    for ip, mac in mac_results:
        print(f"{ip} - Địa chỉ MAC: {mac}")

if __name__ == "__main__":
    # Nhập thông tin từ người dùng
    start_ip = input("Nhập địa chỉ IP bắt đầu (ví dụ: 192.168.1.0): ")
    prefix = input("Nhập tiền tố CIDR (ví dụ: 24 cho mạng /24): ")

    # Bắt đầu quét mạng
    scan_network(start_ip, prefix)
