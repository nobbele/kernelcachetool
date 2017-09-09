from subprocess import call
import os
import sys
import platform
import subprocess
import urllib.request
from bs4 import *

class kcachedownloader:
	def __init__(self, device, deviceid):
		response = urllib.request.urlopen('http://api.ipsw.me/v2.1/{}/{}/url'.format(device, deviceid))
		ipsw = BeautifulSoup(response.read(), "html.parser")

		is32bit = (platform.architecture()[0] == '32bit')
		system32 = os.path.join(os.environ['SystemRoot'], 
                        'SysNative' if is32bit else 'System32')
		bash = os.path.join(system32, 'bash.exe')
		call(bash + " -c './partialzip " + ipsw.get_text() + " kernelcache.release.k93'")

def download(device, deviceid):
	k = kcachedownloader(device, deviceid)
	
if __name__ == "__main__":
	download(sys.argv[1], sys.argv[2])