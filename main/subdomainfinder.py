'''

author Omar Bani-Issa
@omaroo99

'''

import requests
import json 
import pycurl
from io import BytesIO
from urllib.parse import urlencode
import concurrent.futures
# from freq.utils import parseFileToList



def crtsh(domain):
	# print(sub)
	crtsh = []
	r = requests.session()
	certsh = "https://crt.sh"
	data = {"q":"%.{}".format( domain), "output":"json"}
	response = r.post(url = certsh, data= data)
	# print(response.text)
	try:			
		json_data = json.loads(response.text)
		for i in range(len(json_data)):
			# print('***********')
			# print(json_data[i]['name_value'])
			try:
				if len((json_data[i]['name_value'].split('\n'))) >  1:
					crtsh.extend( [i for i in json_data[i]['name_value'].split('\n')] )
				else:
					crtsh.append((json_data[i]['name_value']))
			except:
				pass
	except:		
		pass
	# print(crtsh)
	return crtsh
# ?domain=line.me&include_subdomains=true&expand=dns_names&expand=issuer&expand=cert"
def certspotter(sub):
	certspotter = []

	buffer = BytesIO()
	c = pycurl.Curl()
	c.setopt(c.URL, 'https://api.certspotter.com/v1/issuances?domain={}.line.me&include_subdomains=true&expand=dns_names&expand=issuer&expand=cert'.format(sub))
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()

	body = buffer.getvalue()
	# Body is a byte string.
	# We have to know the encoding in order to print it to a text file
	# such as standard output.
	# output = json.loads()
	try:			
		json_data = json.loads((body.decode('iso-8859-1')))
		for i in range(len(json_data)):
			print(json_data[i]['dns_names'].lstrip('\n').rstrip(' ').lstrip(' '))
	except:		
		pass


#  https://api.hackertarget.com/hostsearch/?q=line.me

def hackertarget(sub):
	hackertarget = []
	buffer = BytesIO()
	c = pycurl.Curl()
	# print('https://api.hackertarget.com/hostsearch/?q={}.line.me'.format(sub))
	c.setopt(c.URL, 'https://api.hackertarget.com/hostsearch/?q={}.line.me'.format(sub))
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()

	body = buffer.getvalue()
	# Body is a byte string.
	# We have to know the encoding in order to print it to a text file
	# such as standard output.
	# output = json.loads()
	for i in range(len(body.decode('iso-8859-1').split(','))):
		
		try:
			if len(body.decode('iso-8859-1').split(',')[i].split('\n')) > 1:

				hackertarget.append(body.decode('iso-8859-1').split(',')[i].split('\n')[1])
			else:
				hackertarget.append(body.decode('iso-8859-1').split(',')[i])
		
		except:			
			pass
	
	return hackertarget

def subdomainsfinder(domain):
	
	subdomains = []
	_crtsh = []
	_hackertarget = []

	_crtsh = crtsh(domain)
	_hackertarget = hackertarget(domain)

	subdomains = _crtsh + _hackertarget

	return list(set(subdomains))
# print(crtsh('line.me', 'game'))