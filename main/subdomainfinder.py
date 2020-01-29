'''

author Omar Bani-Issa
@omaroo99

'''

import requests
import json 
from freq.utils import *
from multiprocessing.dummy import Pool as ThreadPool




def parseJson(response, out=None):
	json_data = json.loads(response)
	subdomains = set()
	# print(response)
	for i in range(len(json_data)):
		if out != None:
			writeFile(json_data[i]['name_value'], out)
		else:
			subdomains.add(json_data[i]['name_value'].strip())
	return subdomains





def subdomainsfinder(inputFile = "subdomains-top1million-5000.txt" ,domain ,threadNum=5):
	
	def sendRequest(sub):
		r = requests.session()
		certsh = "https://crt.sh"
		data = {"q":"%.{}.{}".format(sub, domain), "output":"json"}
		response = r.post(url = certsh, data= data)
		parseJson(response.text)

	inputFile = parseFileToList(inputFile)
	pool = ThreadPool(int(threadNum))
	results = pool.map(sendRequest, inputFile)



