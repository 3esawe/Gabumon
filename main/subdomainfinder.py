'''

author Omar Bani-Issa
@omaroo99

'''

import requests
import json 
from freq.utils import *
from multiprocessing.dummy import Pool as ThreadPool




def parseJson(response, out=None):
	
	try:			
		json_data = json.loads(response)
		subdomains = set()
		# print(json_data)
		# print('s')
		for i in range(len(json_data)):
			if out != None:
				writeFile(json_data[i]['name_value'], out)
			else:
				subdomains.add(json_data[i]['name_value'].lstrip('\n').rstrip(' ').lstrip(' '))
		return subdomains
	except:
		pass




def subdomainsfinder(domain, threadNum=5, inputFile='/root/Gabumon/main/subdomains-top1million-5000.txt'):

	subdomains = []

	def sendRequest(sub):
		# print(sub)
		r = requests.session()
		certsh = "https://crt.sh"
		data = {"q":"%.{}.{}".format(sub, domain), "output":"json"}
		response = r.post(url = certsh, data= data)
		# print(response.text)
		ret = parseJson(response.text)
		
		try:
			subdomains.extend(list(ret))
		
		except:
			pass

	inputFile = parseFileToList(inputFile)
	pool = ThreadPool(int(threadNum))
	results = pool.map(sendRequest, inputFile)
	print(subdomains)


