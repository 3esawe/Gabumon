
import requests 
from bs4 import BeautifulSoup
import re
from freq.utils import writeFile





links = []
script_links = []
img_src = []
keywrods = ['a', 'img', 'script']  


def source(url):
	if "http://" not in url and "https://" not in url:
		print("[+] You forgot to enter http:// or https://")
	req = requests.get(url)
	return req.text


def jsLinks(inputFile):

	links = []
	matches = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', inputFile)
	for match in matches:
		writeFile(match, 'ScriptLinks')


def srcAnlayzer(source_code):
	
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






