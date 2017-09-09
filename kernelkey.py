import json
import sys
class kernelkey:
	def __init__(self, device, buildid):
		self.kcache = []
		self.version = 0
		self.iDevice = device
		self.buildid = buildid
	def kcacher(self):
		with open('keys.json') as f:
			all = json.loads(f.read())
		for build in all:
			if build[self.iDevice]["build"] == self.buildid:
				self.kcache = build[self.iDevice]["kernelcache"]
				
def GetKernelKey(device, buildid):
	k = kernelkey(device, buildid)
	k.kcacher()
	return k.kcache
	
if __name__ == "__main__":
	GetKernelKey(sys.argv[1], sys.argv[2])
		