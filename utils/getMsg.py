import scapy.all as scapy

class Message:
    def __init__(self, src, sport, dst, dport, time, content, type):
        self.src = src
        self.sport = sport
        self.dst = dst
        self.dport = dport
        self.time = time
        self.content = content
        self.type = type

data = scapy.rdpcap('./data/sip会话.pcap')
  
def initData(packet):
  dst = packet.payload.dst
  dport = packet.payload.dport
  sport = packet.payload.sport
  src = packet.payload.src
  time = packet.payload.time
  try: 
    content = packet['Raw'].load.decode('utf-8').split('\r\n')[0]
    type = 'SIP'
  except UnicodeDecodeError: 
    content = 'RTP'
    type = 'RTP'

  
  return Message(src, sport, dst, dport, time, content, type)

def getDataList():
  list = []
  for a in data:
    showData = initData(a)
    list.append(showData)

  return list