from scapy.all import *
import random

packets = []
ips = ["192.168.1.1", "192.168.1.2", "8.8.8.8", "1.1.1.1", "10.0.0.5"]
protocols = [
    (TCP, 80),  (TCP, 443), (TCP, 22),
    (UDP, 53),  (UDP, 123)
]

for i in range(200):
    src = random.choice(ips)
    dst = random.choice(ips)
    proto_class, dport = random.choice(protocols)
    pkt = (
        IP(src=src, dst=dst) /
        proto_class(sport=random.randint(1024,65535), dport=dport) /
        Raw(load=b"X" * random.randint(20, 500))
    )
    packets.append(pkt)

wrpcap("sample_http.pcap", packets)
print("[+] sample_http.pcap generado con 200 paquetes.")
