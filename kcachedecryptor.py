import kernelkey
import os
import sys
import platform
import json
from subprocess import call

class kcachedecryptor:
	def __init__(self, device, deviceid):
		device = kernelkey.GetKernelKey(device, deviceid)
		bashexec = "./kc --in kernelcache.release.k93 --iv {} --key {}".format(device['iv'], device['key'])
		is32bit = (platform.architecture()[0] == '32bit')
		system32 = os.path.join(os.environ['SystemRoot'], 'SysNative' if is32bit else 'System32')
		bash = os.path.join(system32, 'bash.exe')
		call(bash + " -c '" + bashexec + "'")
		call(bash + " -c '" + "mv kcache/kernelcache.bin ./" + "'")
		call(bash + " -c '" + "rm -r kcache" + "'")
		
def decrypt(device, deviceid):
	k = kcachedecryptor(device, deviceid)
	
if __name__ == "__main__":
	decrypt(sys.argv[1], sys.argv[2])
