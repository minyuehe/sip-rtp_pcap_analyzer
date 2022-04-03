import scapy.all as scapy
import copy
import re
import datetime
import json
import glob

class Message:
  def __init__(self, src, sport, dst, dport, time, content, type):
    self.src = src
    self.sport = sport
    self.dst = dst
    self.dport = dport
    self.time = time
    self.content = content
    self.type = type
  
def initData(packet):
  dst = packet.payload.dst
  dport = packet.payload.dport
  sport = packet.payload.sport
  src = packet.payload.src
  time = datetime.datetime.fromtimestamp(float(packet.time)).strftime("%H:%M:%S.%f")
  # how to judge sip-packet or rtp-packet? 
  # just use this charc of rtp-load message which will throw UnicodeDecodeError when we use 'utf-8' as the decode method.
  try:
    # TODO: there is a bug in first-bye-packet.
    aString = packet['Raw'].load.decode('utf-8')
    aList = re.split('[\r\n|;]', aString)
    content = aList[0] + aList[7]
    type = 'SIP'
  except UnicodeDecodeError:
    content = 'RTP'
    type = 'RTP'

  return Message(src, sport, dst, dport, time, content, type)

def getDataList():
  filePathList = glob.glob(r'app/download/*.pcap')
  if(filePathList == []):
    raise Exception("亲，您还没上传文件呢！")

  # 目前只支持单一文件解析
  filePath = filePathList[0]
  print('filePath', filePath)
  data = scapy.rdpcap(filePath)
  table = {}
  isRTP = False
  endRTP = {}
  for a in data:
    showData = initData(a)
    isRTP = showData.type == 'RTP'
    if((not isRTP) and endRTP):
      table[endRTP.time] = json.dumps(endRTP.__dict__)
      endRTP = {}
    if(not (isRTP and endRTP)):
      table[showData.time] = json.dumps(showData.__dict__)
    if(isRTP):
      endRTP = showData
  return [table, filePath]