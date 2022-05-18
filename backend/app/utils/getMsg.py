import dpkt
import socket
from app import app
from app.utils.judgeRTP import *
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


def initData(ip, udp, raw, ts, type):
    dst = socket.inet_ntoa(ip.dst)
    dport = udp.dport
    sport = udp.sport
    src = socket.inet_ntoa(ip.src)
    time = datetime.datetime.fromtimestamp(float(ts)).strftime("%H:%M:%S.%f")

    if(type == 'SIP'):
        if(hasattr(raw, 'method')):
            content = { 'method': raw.method, 'from': raw.headers['from'], 'to': raw.headers['to']}
        else:
            content = { 'reason': raw.reason, 'from': raw.headers['from'], 'to': raw.headers['to']}
    else:
        content = 'RTP MEG'

    return Message(src, sport, dst, dport, time, content, type)


def rdpcap(filePath):
    f = open(filePath, 'rb')
    pcap = dpkt.pcap.Reader(f)
    dataList = []

    for ts, buf in pcap:
        # Unpack the Ethernet frame (mac src/dst, ethertype)
        eth = dpkt.ethernet.Ethernet(buf)

        # Make sure the Ethernet data contains an IP raw
        if not isinstance(eth.data, dpkt.ip.IP):
            print('Non IP raw type not supported %s\n' %
                  eth.data.__class__.__name__)
            continue

        # Now grab the data within the Ethernet frame (the IP raw)
        ip = eth.data
        # Make sure the Ethernet data contains an IP raw
        if not isinstance(ip.data, dpkt.udp.UDP):
            print('Non UDP raw type not supported %s\n' %
                  ip.data.__class__.__name__)
            continue

        # Now grab the data within the Ethernet frame (the IP raw)
        udp = ip.data
        if not len(udp.data):  # 如果应用层负载长度为0，即该包为单纯的udp包，没有负载，则丢弃
            continue

        try:
            req = dpkt.sip.Request(udp.data)
            dataList.append(initData(ip, udp, req, ts, 'SIP'))
        except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
            try:
                res = dpkt.sip.Response(udp.data)
                dataList.append(initData(ip, udp, res, ts, 'SIP'))
            except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                try:
                    rtp = dpkt.rtp.RTP(udp.data)
                    if not judge(rtp):
                        continue
                    dataList.append(initData(ip, udp, rtp, ts, 'RTP'))
                except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                    continue
    f.close()

    return dataList


def getDataList():
    filePathList = glob.glob(r'app/download/*.pcap')
    if(filePathList == []):
        raise Exception("亲，您还没上传文件呢！")

    # 目前只支持单一文件解析
    filePath = filePathList[0]
    print('filePath', filePath)

    # 读取pcap文件
    dataList = rdpcap(filePath)
    table = {}
    isRTP = False
    firstRTP = {}
    endRTP = {}
    for item in dataList:
        isRTP = item.type == 'RTP'
        if((not isRTP) and endRTP):
            if (firstRTP.src == endRTP.src):
                temp = endRTP.src
                endRTP.src = endRTP.dst
                endRTP.dst = temp
                tempPort = endRTP.sport
                endRTP.sport = endRTP.dport
                endRTP.dport = tempPort

            table[endRTP.time] = json.dumps(endRTP.__dict__)
            endRTP = {}
            firstRTP = {}
        if(not (isRTP and endRTP)):
            if (item.type == 'RTP' and firstRTP == {}):
                firstRTP = item
            table[item.time] = json.dumps(item.__dict__)
        if(isRTP):
            endRTP = item
    return [table, filePath]
