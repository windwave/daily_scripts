from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
import time

def installApp(d):
	pcks = d.shell("pm list packages -3") 
	splitedline = re.split(':|\r\n',pcks)
	if('package:com.ss.android.ugc.aweme' in splitedline):
		pass
	else:
		d.installPackage('D:\ZWE\Android\dy.apk')
	return True	

def startApp(d):
	d.startActivity(component = 'com.ss.android.ugc.aweme/.main.MainActivity')

def signIn(d,phoneNo,smsCode):
	d.touch(36,112)
	d.touch(669,1144)
	d.touch(268,434)
	d.type(phoneNo)
	d.touch(326,517)
	d.type(smsCode)
	d.touch(400,634)
	d.type('12345678')
	d.touch(403,856)

def logIn(d,phoneNo,password,smsCode):
	d.touch(691,1138)
	d.type(phoneNo)
	d.touch(372,682)
	d.type(password)
	d.touch(372,682)



def exResCard(d):
	#d.touch()*x



if __name__ == '__main__':
	#1)getDevice
	#init ip addess

	ipPortTxtLst = []
	for i in range(2):
		ipPortTxt = '192.168.56.'+str(101+i)+':5555'
		ipPortTxtLst.append(ipPortTxt)


	#get device
	deviceList = []
	for i in ipPortTxtLst:
    	device=oper_md.waitForConnection(6,i)
	    try:
	        device.wake()
	        deviceList.append(device)
	    except:
	        pass

	print deviceList