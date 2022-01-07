import socket
import sys
import platform

#sys.stdout = open("where_you_at.txt", "w")1

def get_os():
    os_name = platform.system()
    current_ver = platform.release()
    proc = platform.processor()
    machine = platform.machine()
    print(os_name + ' ' + current_ver)
    print(machine + ' ' + proc)

def get_hostname():
        hostname = socket.gethostname()
        hostip = socket.gethostbyname(hostname)
        print(f'Hostname {hostname}')

def get_IP():
    ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip.connect(("8.8.8.8", 80))
    ipv4 = ip.getsockname()[0]
    ip.close()
    return ipv4

def get_open_ports(my_ip):
    ip = get_IP()
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((ip, port))
        if result ==0:
            print(f"Port {port} is open")
        s.close()


get_os()
get_hostname()
get_IP()
print(get_IP())
open_ports = get_open_ports(get_IP())
da_ip = get_IP()
print(da_ip)


#sys.stdout.close()