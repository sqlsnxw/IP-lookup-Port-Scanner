# @uhroyal on github

import socket
import ipaddress
from colorama import Fore, init
import requests
from concurrent.futures import ThreadPoolExecutor

def get_ip_info(ip):
    api_url = f"https://api.iplocation.net/?ip={ip}"
    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            info = {
                'country': data.get('country_name', 'Unknown'),
                'country_code': data.get('country_code2', 'Unknown'),
                'isp': data.get('isp', 'Unknown')
            }
            return info
        else:
            return None
    except Exception as e:
        print(f"{Fore.RED}Error fetching IP info: {e}{Fore.RESET}")
        return None
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"{Fore.GREEN}Port {port} is open on {ip}{Fore.RESET}")
        sock.close()
    except Exception as e:
        print(f"{Fore.RED}Error scanning port {port} on {ip}: {e}{Fore.RESET}")
def main():
    init()
    print(f"{Fore.BLUE}IP Lookup + Port Scanner{Fore.RESET}\n")
    print("------------------------------\n")
    ip = input("IP address: ").strip()
    
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print(f"{Fore.RED}Invalid IP.{Fore.RESET}")
        return
    
    info = get_ip_info(ip)
    
    if info:
        print(f"\nIP: {ip}")
        print(f"Country: {info['country']} ({info['country_code']})")
        print(f"ISP: {info['isp']}")
    else:
        print(f"{Fore.RED}Couldn't get IP info{Fore.RESET}")
    
    print(f"\nScanning ports...\n")
    
    with ThreadPoolExecutor(max_workers=200) as executor:
        for port in range(1, 1025):
            executor.submit(scan_port, ip, port)
    
    print(f"{Fore.BLUE}Finished!{Fore.RESET}")
if __name__ == "__main__":
    main()

    input(f"\n{Fore.YELLOW} ||| Press Enter to exit |||{Fore.RESET}") 