import scapy.all as scapy
import re


data = scapy.rdpcap('./data/sip会话.pcap')

# res/10101010/payload/
print(data[10].payload.dst)
print(data[10].payload.dport)
print(data[10].payload.sport)
print(data[10].payload.src)
print(data[10].payload.time)

# ['Raw']层
a = data[0]['Raw']
# print(a.load.decode('UTF-8'))
# 解码后
aString = a.load.decode('utf-8')
aList = re.split('[\r\n|;]', aString) #'\r\n' or 
# 0: 包信息  1: via 2: from 3: to
print(aList[0])
print(aList[7])