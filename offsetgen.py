import sys
class offsetgen:
	def __init__(self, offsetlist):
		string = '["'
		for i in offsetlist:
			string += str(i) + '","'
	
		string = string[:-3] + '"]'
		self.string = string.replace('"offsetgen.py",', "")

def GenerateOffsetList(offsetlist):
	k = offsetgen(offsetlist)
	return k.string