# NET-01: Network Traffic Analyzer
 
> Network traffic analysis tool using PyShark, Pandas and Matplotlib.
> Part of my professional portfolio [Carlos Rodriguez](https://github.com/CarlosRolo) — Telematic Engineer.
 
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![PyShark](https://img.shields.io/badge/PyShark-0.6-green)
![Pandas](https://img.shields.io/badge/Pandas-3.0-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)
 
---
 
## Description
 
Analyzes `.pcap` files captured with Wireshark and generates automatic visual reports:

- 📊 Protocol distribution (TCP, UDP, DNS, SSH, NTP...)
- 📈 Traffic volume over time (bytes/second)
- 🌐 Top source IPs by traffic volume

## Project Structure
 
```
net-traffic-analyzer/
├── src/
│   ├── capture.py       # Main script (CLI)
│   ├── analyzer.py      # .pcap parsing with PyShark + Pandas
│   └── visualizer.py    # Charts with Matplotlib + Seaborn
├── data/samples/        # Sample .pcap files
├── reports/figures/     # Generated charts (PNG)
├── tests/               # Unit tests
└── requirements.txt
```
 
## Installation
 
```bash
git clone https://github.com/CarlosRolo/net-traffic-analyzer.git
cd net-traffic-analyzer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sudo apt-get install -y tshark
```
 
## Usage
 
```bash
python3 src/capture.py data/samples/sample_http.pcap
```
 
### Expected output
 
```
[*] Analyzing: data/samples/sample_http.pcap
--------------------------------------------------
[+] Total packets    : 200
[+] Total bytes      : 57,682
[+] Avg packet size  : 288.41 bytes
[+] Top protocol     : TCP
[+] Unique IPs       : 10
--------------------------------------------------
[+] Analysis complete.
```
 
## Generated Charts
 
| Protocol Distribution | Top Source IPs | Traffic Over Time |
|:---------------------:|:--------------:|:-----------------:|
| ![](reports/figures/protocol_distribution.png) | ![](reports/figures/top_ips.png) | ![](reports/figures/traffic_over_time.png) |
 
## Tech Stack
 
| Tool | Purpose |
|---|---|
| PyShark 0.6 | .pcap file parsing |
| Pandas 3.0 | Data analysis and manipulation |
| Matplotlib + Seaborn | Visualization |
| Scapy | Test traffic generation |
| TShark | Capture backend (Wireshark CLI) |
 
## Author
 
**Carlos David Rodriguez Lopez**  
Telematic Engineer — ESPOCH  
Manta, Manabí, Ecuador  
Riobamba, Chimborazo, Ecuador  
[github.com/CarlosRolo](https://github.com/CarlosRolo)
 
## License
 
MIT License — see [LICENSE](LICENSE)

