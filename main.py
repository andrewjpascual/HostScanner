import argparse
import os
import socket

def scanIP(uIP):
    response = os.popen(f"ping {uIP}").read()
    if "ttl=" in response.lower():
        print(f"UP {uIP} Ping Successful, Host is UP!")
    else:
        print(f"DOWN {uIP} Ping Unsuccessful, Host is DOWN.") 

def scanPorts(uPort, uIP):
    response = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    response.settimeout(1)
    result = response.connect_ex((uIP, uPort))
    response.close()

    if result == 0:
        print(f"Port {uPort} is OPEN on {uIP}")
    else:
        print(f"Port {uPort} is CLOSED on {uIP}")



def main():
    parser = argparse.ArgumentParser(
        description='This script will identify accessible IPs and Ports'
    )
    parser.add_argument('-ip', help ='Use an IP to scan', type =str)
    parser.add_argument('-p', help ='Use a Port to scan', type =int)
    args = parser.parse_args()
    uIP = args.ip
    uPort = args.p
    
    if uIP:
        scanIP(uIP)
    else:
        print(f"Please input an IP")

    if uPort and uIP:
        scanPorts(uPort, uIP)

if __name__ == "__main__":
    main()