# 🌸 **Minecraft IP Scanner Tool**

![Python](https://img.shields.io/badge/Python-%23blue.svg?style=for-the-badge&logo=python&logoColor=white)
![MIT License](https://img.shields.io/github/license/YourUsername/Minecraft-IP-Scanner?style=for-the-badge)
![Minecraft-IP-Scanner](https://img.shields.io/badge/Minecraft%20IP%20Scanner-%23ff69b4?style=for-the-badge)

---

## 🚀 **Giới thiệu**

**Minecraft IP Scanner Tool** là **công cụ quét IP** mạnh mẽ cho **Minecraft Server**. Công cụ này cho phép bạn kết nối tới server Minecraft qua **RCON**, theo dõi các IP người chơi kết nối, phát hiện các IP lạ, và kiểm tra các lỗ hổng bảo mật của các IP từ xa.

**Phục vụ:**  
✨ **Quản lý Server Minecraft**  
✨ **Phát hiện IP lạ**  
✨ **Kiểm tra bảo mật mạng Minecraft**  
✨ **Hỗ trợ quét cổng, dịch vụ, và lỗ hổng bảo mật**

---

## ⚡ **Tính năng**

✅ Kết nối tới server Minecraft qua **RCON** và theo dõi IP người chơi.  
✅ Phát hiện **IP lạ** và so sánh với danh sách IP đã biết.  
✅ Quét **cổng và dịch vụ** của IP từ xa sử dụng **nmap**.  
✅ Kiểm tra các **lỗ hổng bảo mật** trên cổng 80 của IP (HTTP).  
✅ Xuất kết quả dưới dạng **JSON/CSV/HTML**.  
✅ Cài đặt và sử dụng đơn giản, hỗ trợ **cross-platform**.

---

## 🛠️ **Cài đặt**

### Yêu cầu:
- Python 3.x
- Thư viện Python:
  - `mcrcon` (Để kết nối với server Minecraft qua RCON)
  - `nmap` (Để quét cổng và dịch vụ)
  - `requests` (Để kiểm tra các lỗ hổng bảo mật)

Cài đặt các thư viện yêu cầu:

```bash
pip install mcrcon nmap requests
```

### Clone repo:

```bash
git clone https://github.com/Yuri08loveElaina/scan-MC.git
cd scan-MC
```

---

## 🐳 **Chạy bằng Docker (Khuyến nghị nếu không muốn cài Python)**

Build Docker image:

```bash
docker build -t minecraft-ip-scanner .
```

Chạy công cụ với Docker:

```bash
docker run --rm minecraft-ip-scanner --target 192.168.1.5 --ports 22,80 --banner --finger --vuln
```

---

## ✨ **Cách sử dụng**

### ⚡ **Kết nối đến Minecraft và nhận IP người chơi:**
```bash
python scan.py -u
```

### ⚡ **Phát hiện IP lạ:**
```bash
python scan.py --detect
```

### ⚡ **Quét sâu một IP (quét cổng, dịch vụ):**
```bash
python scan.py -r <ip>
```

### ⚡ **Kiểm tra lỗ hổng bảo mật của một IP:**
```bash
python scan.py -v <ip>
```


---

## ❤️ **Góp ý / Issue**

Nếu bạn gặp lỗi hoặc muốn thêm tính năng mới, vui lòng:
- Mở [Issue](https://github.com/Yuri08loveElaina/scan-MC/issues)
- Hoặc fork và gửi **Pull Request**

---

## 📜 **License**

**MIT License**

---

## ✨ **Chúc bạn có những giờ phút vui vẻ với Minecraft!** 🎮🌍

