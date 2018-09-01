#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-16 21:16:35
# @Author  : zwe (zhengwei2015@gmail.com)
# @Link    : http://www.windfarm.cn
# @Version : $Id$


from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
import time
import datetime

a_pos = (373,536,"DOWN_AND_UP")
b_pos = (373,662,"DOWN_AND_UP")
c_pos = (373,787,"DOWN_AND_UP")

def choose_a(device_list):
	for i in device_list:
		i.touch(373,536,"DOWN_AND_UP")

def choose_b(device_list):
	for i in device_list:
		i.touch(373,662,"DOWN_AND_UP")

def choose_c(device_list):
	for i in device_list:
		i.touch(373,787,"DOWN_AND_UP")



if __name__ == '__main__':
    #1)getDevice
    #init ip addess
    ipPortTxtLst = []
    ipLastList = [0,1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21]
    for i in range(8):
        ipPortTxt = '192.168.56.'+str(101+i)+':5555'
        ipPortTxtLst.append(ipPortTxt)


    #get device
    deviceList = []
    for i in ipPortTxtLst:
        device=mr.waitForConnection(6,i)
        try:
            device.wake()
            deviceList.append(device)
        except:
            pass

    for i in deviceList:
        i.installPackage('D:\ZWE\huangjingshike\youku.apk')
        
        
    while(True):
        ans_list = [1,2,3]
        c = mr.choice('where to touch this time',ans_list,'title')
        if(c==0):
            choose_a(deviceList)
        elif(c==1):
            choose_b(deviceList)
        elif(c==2):
            choose_c(deviceList)
        


