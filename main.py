import argparse
import os
import socket
import re
from colorama import Fore
import concurrent.futures
import threading

#Check if the provided IP is valid
def isValidIP(uIP):
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    return re.match(regex, uIP) is not None

#Scan the valid IP
def scanIP(uIP):
    response = os.popen(f"ping {uIP}").read()
    if "ttl=" in response.lower():
        print(f"{uIP} Ping Successful, Host is UP!")
    else:
        print(f"{uIP} Ping Unsuccessful, Host is DOWN.") 


#Scan the valid port on the valid IP
def scanPorts(uPort, uIP):
    stop_event = threading.Event()
    unreachable = [0]
    def check_port(port):
        if stop_event.is_set():
            return
        response = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        response.settimeout(0.5)
        result = response.connect_ex((uIP, port))
        response.close()
        
        if result == 0:
            print(Fore.GREEN + f"Port {port} is OPEN on {uIP}" + Fore.RESET)
        else:
            unreachable[0] += 1

#Use ThreadPoolExecutor to run scans in parallel
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=250) as executor:
            executor.map(check_port, uPort)
        print(Fore.RED + f"There are {unreachable} CLOSED ports on {uIP}" + Fore.RESET)
    except KeyboardInterrupt:
        stop_event.set() #Stop threads
        print(f"Scan interrupted.")

def main():
    parser = argparse.ArgumentParser(
        description='This script will identify accessible IPs and Ports'
    )
    parser.add_argument('-ip', help ='Use an IP to scan', type =str)
    parser.add_argument('-p', help ='Use a Port or list of Ports to scan separated by comma', type =str)
    args = parser.parse_args()
    uIP = args.ip
    inPort = args.p

    #Conver input Ports (comma separated str) into a list of integers
    uPort = []
    if inPort:
        for part in inPort.split(","):
            part = part.strip()
            if("-") in part: #Handle the range of ports
                start, end = map(int, part.split("-"))
                try:

                    if start > end or start < 1 or 65535 < end:
                        print(f"Please input a valid port number (1-65535) since the given range is not acceptable")
                        return
                    uPort.extend(range(start, end + 1))
                except ValueError:
                    print(f"Invalid port range format: {part}. Use start-end (e.g., 20-25).")
                    return
            else: #Handle the single ports
                try:
                    port = int(part)
                    if port < 1 or port > 65535:
                        print(f"Please input a valid port number (1-65535)")
                        return
                    else:
                        uPort.append(port)
                except ValueError:
                    print(f"Invalid port format {part}. Use numbers or ranges")
                    return
    
    #check if there is an IP provided
    if not uIP or not isValidIP(uIP):
        print(f"Please input a valid IP Address.")
        return
    
    if uIP:
        scanIP(uIP)

    #Check if there is a port provided
    if uPort and uIP:
        for port in uPort:
            if port < 1 or port > 65535:
                print(f"Please input a valid port number (1-65535) since {port} is not acceptable")
                return
        scanPorts(uPort, uIP)
    else:
        print(f"No port provided for this scan")

if __name__ == "__main__":
    main()