
import requests 
from bs4 import BeautifulSoup
import re
from freq.utils import writeFile





links = []
script_links = []
img_src = []
keywrods = ['a', 'img', 'script']  


def source(url, out=None):
	if "http://" not in url and "https://" not in url:
		print("[+] You forgot to enter http:// or https://")
	req = requests.get(url)
	
	if out == None:
		srcAnlayzer(req.text)
		jsLinks(req.text)

	else: 
		srcAnlayzer(req.text, out)
		jsLinks(req.text, out)

def jsLinks(source_code, out = None):

	links = []
	matches = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', source_code)
	for match in matches:
		
		if out == None:
			print(match)
		
		else:
			writeFile(match, out)


def srcAnlayzer(source_code, out = None):
	
	soap =	BeautifulSoup(source_code,features="lxml")
	for key in keywrods:

		if key == 'a':
			tag = soap.a
			links.append([a['href'] for a in soap.find_all('a', {"href":True})])
		
		if key == 'script' :
			
			tag = soap.script
			content = soap.script.string
			script_links.append([s['src'] for s in soap.find_all('script', {'src':True})])
		

		if key == 'img':
			
			tag = soap.img
			if tag != None:
				img_src.append([s['src'] for s in soap.find_all('img', {'src':True})])
	if out != None:
		with open(out ,'w') as handle:
			handle.write(['%s ********************href links********************\n' % i for i in links])
			handle.write(['\n%s ********************script links********************\n' % i for i in script_links])
			handle.write(['\n%s ********************img links********************\n' % i for i in img_src])






