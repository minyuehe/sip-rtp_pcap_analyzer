# 记录上一个RTP包
judgeObj = {
  'isRTP': False,
  'seq': 0,
  'ssrc':0,
  'pt': 0
}


def judge(packet):
  # 只有seq，ts会变化
  # version = 2
  # p相同且为0
  # pt荷载 同一段通信相同123
  # ssrc源标识符一定
  # seq/ts
  # print(packet.version, packet.cc, packet.pt, packet.p, packet.ssrc, packet.ts, packet.seq)
  # print(packet.data,len(packet.data))

  if(packet.version == 2 and packet.p == 0 and (not judgeObj['isRTP'])):
    judgeObj['seq'] = packet.seq
    # ts = packet.ts
    judgeObj['ssrc'] = packet.ssrc
    judgeObj['pt'] = packet.pt
    judgeObj['isRTP'] = True
    return judgeObj['isRTP']
  if(judgeObj['isRTP'] and (packet.seq - 1) == judgeObj['seq'] and packet.ssrc == judgeObj['ssrc'] and packet.pt == judgeObj['pt']):
    return judgeObj['isRTP']
  else:
    judgeObj['isRTP'] = False
    return judgeObj['isRTP']
