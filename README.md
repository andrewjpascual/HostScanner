# HostScanner
This will identify live IPs, ports, and port ranges


## About the Project
HostScanner is a simple and efficient Python-based tool for scanning ports and CIDR ranges.


![single ip scan](https://github.com/user-attachments/assets/8d1dbc6e-27eb-4f0b-93a3-b108dc1810b1)

![Port range](https://github.com/user-attachments/assets/a699ee7c-4907-4257-b674-b30b20463ae8)

![CIDR scan](https://github.com/user-attachments/assets/5e98efba-f40f-4151-b5ff-e3f81d3bad40)

I decided to build this project with Python due to it's simplicity and cross-platform compatability. There is also multiple libraries and community support which made troubleshooting and extending functionality much easier.

## Getting Started

Instructions to set up this project in your local environment are listed down below

### Prerequisites

* Git
  ```
  https://git-scm.com/
  ```

  ## Installation

   Get the repository with
   ```sh
   git clone https://github.com/andrewjpascual/HostScanner.git
   ```

## Options
### `-ip [IP Address]`
Target IP Address/es whose Ports need to be scanned. It can parse single IP Address for Port Scanning as well as CIDR which can be used for Host Discovery.

For example:
```
-ip 192.168.1.1
```

CIDR example:
```
-ip 192.168.1.1/30
```

### `-p [Port Numbers]` `--port [Port Numbers]`
Specifies the ports to be scanned to get their status. Port Numbers are required for Port Scanning and will not be considered during Host Discovery.

For example:
```
-p 80,443,21
```

Port Range example:
### **Scan for a range of open ports on a single host**
It will scan for open ports from 1-9000 and also label the common ports.
```
python main.py --ip 192.168.1.1 -p 1-100
```
<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the GNU License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Andrew Pascual - andrewjpascual@gmail.com

https://github.com/andrewjpascual/HostScanner


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Furious Port Scanner](https://github.com/liamg/furious)
* [TutorialEdge](https://tutorialedge.net/projects/building-security-tools-in-go/building-port-scanner-go/)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [Elliot Chance](https://elliotchance.medium.com/goroutines-and-channels-a-real-ly-simple-server-in-go-93ba49ff7c5c)
