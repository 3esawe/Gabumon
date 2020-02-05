
import requests 
from bs4 import BeautifulSoup
import re
from freq.utils import writeFile





links = []
script_links = []
img_src = []
keywrods = ['a', 'img', 'script']  


def source(url, out=None, js =False):
	if "http://" not in url and "https://" not in url:
		print("[+] You forgot to enter http:// or https://")
	# print(url)
	req = requests.get(url)

	if out == None:
		srcAnlayzer(req.text)
	
	else:	
		srcAnlayzer(req.text, out)


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


			for i in range(len(links[0])):
				
				if i == 0:					
					handle.write('********************href links********************')
				
				handle.write('\n%s\n' % links[0][i])
			
			for i in range(len(script_links[0])):
				
				if i == 0:					
					handle.write('\n********************script links********************\n')		
				handle.write('%s\n' % script_links[0][i])

			for i in range(len(img_src[0])):

				if i == 0:					
					handle.write('\n********************img links********************\n')

				handle.write('\n%s\n' % img_src[0][i])







