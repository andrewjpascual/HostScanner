import argparse
import os
import socket
import re
from colorama import Fore

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
    for port in uPort:
        response = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        response.settimeout(1)
        result = response.connect_ex((uIP, port))
        response.close()
        if result == 0:
            print(Fore.GREEN + f"Port {port} is OPEN on {uIP}" + Fore.RESET)
        else:
            print(Fore.RED + f"Port {port} is CLOSED on {uIP}" + Fore.RESET)


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
    if inPort:
        uPort = [int(port.strip()) for port in inPort.split(",")]
    else:
        uPort = []
    

    
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