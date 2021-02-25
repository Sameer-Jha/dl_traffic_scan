#!/usr/bin/env python3
from scapy.all import *
import os
import datetime as dt
import logging

def fileNameGen():
    WriteFile = f'{dt.datetime.now()}_sniffing_data.txt'
    return WriteFile


def writer(fileName, data):
    with open(fileName, 'a+') as file:
        file.write(data)


def main():
    fileName = fileNameGen()
    sniff(prn=lambda pkt: writer(fileName, pkt.summary()+"\n"))


if __name__  == '__main__':
    main()