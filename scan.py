import argparse
import time
import socket
from mcrcon import MCRcon
import re
import json
import os

# Thông tin kết nối với RCON
RCON_HOST = "localhost"  # Địa chỉ của server Minecraft, có thể là IP của server hoặc localhost
RCON_PORT = 25575  # Cổng RCON (mặc định là 25575)
RCON_PASSWORD = "your_rcon_password"  # Mật khẩu RCON đã thiết lập trong server.properties

def ket_noi_rcon():
    try:
        rcon = MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT)
        rcon.connect()
        print("Đã kết nối đến server Minecraft qua RCON.")
        return rcon
    except Exception as e:
        print(f"Lỗi khi kết nối RCON: {e}")
        return None

# Quét IP và thông tin người chơi khi họ vào server
def quet_ip_rcon(rcon):
    while True:
        try:
            # Gửi lệnh để lấy danh sách người chơi và IP của họ
            response = rcon.command("list")  # Lệnh này trả về danh sách người chơi
            print(f"Thông tin người chơi: {response}")

            # Trích xuất IP từ response 
            ips = re.findall(r'\d+\.\d+\.\d+\.\d+', response)
            if ips:
                print("Các IP kết nối vào server Minecraft: ", ips)
            time.sleep(10)  # Kiểm tra lại sau mỗi 10 giây
        except Exception as e:
            print(f"Lỗi khi thực thi lệnh RCON: {e}")
            break

# Phát hiện IP lạ (so sánh với danh sách IP đã biết)
def detect_ip_lạ(current_ips, known_ips_file='known_ips.json'):
    if os.path.exists(known_ips_file):
        with open(known_ips_file, 'r') as f:
            known_ips = json.load(f)
    else:
        known_ips = []

    # Phát hiện IP lạ
    lạ = current_ips - set(known_ips)
    if lạ:
        print(f"IP lạ phát hiện: {lạ}")
        for ip in lạ:
            print(f"  - IP lạ: {ip}")
        # Cập nhật danh sách IP đã biết
        known_ips.extend(list(lạ))
        with open(known_ips_file, 'w') as f:
            json.dump(known_ips, f)
    else:
        print("Không phát hiện IP lạ.")

# Quét cổng và dịch vụ của một IP (nếu cần)
def quet_su_dung_nmap(ip):
    import nmap
    nm = nmap.PortScanner()
    try:
        print(f"Đang quét các cổng mở của IP: {ip}")
        nm.scan(ip, '1-1024')  # Quét các cổng từ 1 đến 1024
        for host in nm.all_hosts():
            print(f"Đã tìm thấy host: {host}")
            for proto in nm[host].all_protocols():
                print(f"  - Protocol: {proto}")
                lport = nm[host][proto].keys()
                for port in lport:
                    print(f"    - Port: {port}, State: {nm[host][proto][port]['state']}")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi quét: {e}")

# Kiểm tra lỗ hổng bảo mật phổ biến (ví dụ HTTP)
def kiem_tra_vuln(ip):
    import requests
    url = f"http://{ip}:80"
    try:
        response = requests.get(url, timeout=5)
        if "403 Forbidden" in response.text:
            print(f"[!] Lỗ hổng: HTTP 403 trên {ip}")
        elif "404 Not Found" in response.text:
            print(f"[!] Lỗ hổng: HTTP 404 trên {ip}")
        else:
            print(f"[+] Không phát hiện lỗi HTTP trên {ip}")
    except requests.RequestException as e:
        print(f"Không thể kết nối đến {ip}: {e}")

# Hàm quét sâu vào một IP
def quet_sau(ip):
    print(f"Đang quét sâu vào IP {ip}...")
    quet_su_dung_nmap(ip)  # Quét cổng
    kiem_tra_vuln(ip)      # Kiểm tra lỗ hổng

def main():
    parser = argparse.ArgumentParser(description="Công cụ quét và nhận IP khi người chơi kết nối đến server Minecraft")
    parser.add_argument("-u", "--url", help="Kết nối tới server Minecraft và nhận IP người chơi", action='store_true')
    parser.add_argument("-r", "--scan", help="Quét sâu một IP (quét cổng, dịch vụ, vuln)", required=False)
    parser.add_argument("-v", "--vuln", help="Kiểm tra lỗ hổng của một IP", required=False)
    parser.add_argument("--detect", help="Phát hiện IP lạ trong server", action='store_true', required=False)
    parser.add_argument("--scan-all", help="Quét tất cả các IP trong mạng (toàn bộ mạng nội bộ)", action='store_true', required=False)

    args = parser.parse_args()

    if args.url:
        # Kết nối tới server Minecraft và nhận IP người chơi
        rcon = ket_noi_rcon()
        if rcon:
            quet_ip_rcon(rcon)

    if args.scan_all:
        # Quét tất cả các IP trong mạng nội bộ
        import nmap
        nm = nmap.PortScanner()
        local_network = "192.168.1.0/24"  # Mạng nội bộ, bạn có thể thay đổi nếu cần
        print(f"Đang quét tất cả các IP trong mạng: {local_network}")
        try:
            nm.scan(hosts=local_network, arguments='-sn')  # Quét tất cả các host trong mạng
            ips = [host for host in nm.all_hosts()]
            print(f"Các IP kết nối đến mạng: {ips}")
        except Exception as e:
            print(f"Đã xảy ra lỗi khi quét mạng: {e}")

    if args.detect:
        # Phát hiện IP lạ
        print("Đang phát hiện IP lạ...")
        current_ips = set(quet_ip_rcon(None))  
        detect_ip_lạ(current_ips)

    if args.scan:
        # Quét sâu một IP
        print(f"Quét sâu IP: {args.scan}")
        quet_sau(args.scan)

    if args.vuln:
        # Kiểm tra lỗ hổng của một IP
        print(f"Kiểm tra lỗ hổng cho IP: {args.vuln}")
        kiem_tra_vuln(args.vuln)

if __name__ == "__main__":
    main()
