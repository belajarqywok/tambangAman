#!/bin/env python3
import os
import sys
import json
from time import sleep
from pyspectator.processor import Cpu
class cpuConf:
    def __init__(self):
        fileLocation=open('setelan.json')
        self.data=json.loads(fileLocation.read())
        self.cpu=Cpu(monitoring_latency=1)
    def cpuConfig(self):
        superCritical=100#deg [ default value ]
        if self.cpu.temperature>=superCritical:
            print("ane kluar gan, drpd ane rusax nantinya...")
            sys.exit(0)
        elif self.cpu.temperature>=self.data["cpu"]["max_temperature"]:
            self.outputValue=False
        elif self.cpu.temperature<=self.data["cpu"]["max_temperature"]:
            self.outputValue=True
        return self.outputValue
class miningConf:
    def __init__(self):
        fileLocation=open('setelan.json')
        self.data=json.loads(fileLocation.read())
        self.getCpuConfValue=cpuConf().cpuConfig()
    def miningConfig(self):
        while True:
            if self.getCpuConfValue==True:
                os.system("./tambang -a verus -o stratum+tcp://ap.luckpool.net:3956 -u "+str(self.data["mining"]["wallet_address"])+"."+str(self.data["mining"]["worker_name"])+" -p x -t "+str(self.data["mining"]["miner"]))
            elif self.getCpuConfValue==False:
                print("sabar dulu ya gan, soalnye ane kepanasan.....")
                sleep(10) # delay 10 second
                os.system("clear")
class executed:
    def __init__(self):
        self.run=miningConf()
        self.run.miningConfig()
if __name__ == "__main__":
    try:   
        os.system("clear")
        print("resiko kerusakan akibat kerakusan user tidak ditanggung developer")
        sleep(15)
        os.system("clear")
        print("maksimal penggunaan 7 jam (nonstop), mau lebih dri itu terserah")
        sleep(12)
        os.system("clear")
        executed()
    except KeyboardInterrupt:
        print("keluar gan")
