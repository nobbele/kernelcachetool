import sys
import urllib.request
from bs4 import *


class offsetgrabber:
	def __init__(self, device, version):
		link = 'http://wall.supplies/offsets/{}-{}'.format(device, version)
		response = urllib.request.urlopen(link)
		self.offsets = BeautifulSoup(response.read(), "html.parser")
		
def Offsets(device, version):
	k = offsetgrabber(device, version)
	return k.offsets
	
if __name__ == "__main__":
	Offsets(sys.argv[1], sys.argv[2])