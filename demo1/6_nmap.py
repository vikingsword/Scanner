import socket

import nmap

# nm = nmap.PortScanner()
# nmap_path = [r"C:\Program Files (x86)\Nmap\nmap.exe",]

ip = socket.gethostbyname('www.xiaodi8.com')

scanner = nmap.PortScanner()
res = scanner.scan(ip + '-100', '80', '-sV')
print(res)
