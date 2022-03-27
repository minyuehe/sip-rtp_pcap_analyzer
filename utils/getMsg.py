import scapy.all as scapy
import copy
import re

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
  # TODO this time isn't the true time.
  time = packet.payload.time
  # how to judge sip-packet or rtp-packet? 
  # just use this charc of rtp-load message which will throw UnicodeDecodeError when we use 'utf-8' as the decode method.
  try: 
    # TODO: there is a bug in first-bye-packet.
    aString = packet['Raw'].load.decode('utf-8')
    aList = re.split('[\r\n|;]', aString)
    content = aList #aList[0] + aList[7]
    type = 'SIP'
  except UnicodeDecodeError:
    content = 'RTP'
    type = 'RTP'

  return Message(src, sport, dst, dport, time, content, type)

def getDataList():
  list = []
  isRTP = False
  endRTP = {}
  for a in data:
    showData = initData(a)
    isRTP = showData.type == 'RTP'
    if((not isRTP) and endRTP):
      list.append(copy.copy(endRTP)) # 浅拷贝就可以了
      endRTP = {}
    if(not (isRTP and endRTP)):
      list.append(showData)
    if(isRTP):
      endRTP = showData

  return list