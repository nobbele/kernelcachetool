from subprocess import call
import os
import sys
import platform
import subprocess
import urllib.request
from bs4 import *

class kcachedownloader:
	def __init__(self, device, deviceid, file):
		print('http://api.ipsw.me/v2.1/{}/{}/url'.format(device, deviceid))
		response = urllib.request.urlopen('http://api.ipsw.me/v2.1/{}/{}/url'.format(device, deviceid))
		ipsw = BeautifulSoup(response.read(), "html.parser")
		platform1 = platform.platform()
		if platform1 == "linux" or platform1 == "linux2" or platform1 == "darwin":
			call("./partialzip " + ipsw.get_text() + " " + file)
		else:
			is32bit = (platform.architecture()[0] == '32bit')
			system32 = os.path.join(os.environ['SystemRoot'], 
                        'SysNative' if is32bit else 'System32')
			bash = os.path.join(system32, 'bash.exe')
			print(ipsw.get_text())
			call(bash + " -c './partialzip " + ipsw.get_text() + " " + file + "'")

def download(device, deviceid, file):
	k = kcachedownloader(device, deviceid, file)
	
if __name__ == "__main__":
	download(sys.argv[1], sys.argv[2], sys.argv[3])
