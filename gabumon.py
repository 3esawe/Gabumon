from freq import *

from main.subdomainfinder import subdomainsfinder
from main.HTMLscanner import source
from freq.utils import isLink
import pyfiglet
import argparse
import requests

ascii_banner = pyfiglet.figlet_format("Gabumon",font="slant")
print (ascii_banner)
ascii_banner1 = pyfiglet.figlet_format("ALESAWE",font="digital")
print ("By \n"+ascii_banner1)


arparser = argparse.ArgumentParser()


arparser.add_argument(
"-m", "--mode", required=True, help="Enter the usage mode DNS\n for DNS enumaration\nHTML for HTML scanning (i.e.) python3 gabumon [mode]"
)

arparser.add_argument(
"-d", "--domain", required=False, help="Domain to scan in [DNS] mode"
)

arparser.add_argument(
"-u", "--url", required=False, help="Url to scan in [URL] mode"
)

arparser.add_argument(
"-js", "--javascript", required=False, help="javascript file to parse url from in [URL] mode"
)


arparser.add_argument(
"-o", "--outputFile", required=False, help="Enter the name of the output file"
)

arparser.add_argument(
"-i", "--inputFile", required=False, help="Enter the name of the input file to get the subdomains from"
)


arparser.add_argument(
"-t", "--threads", required=False, help="Enter the number of threads in [DNS] mode"
)


parser = vars(arparser.parse_args())

MODE = parser['mode']



if MODE == 'DNS':

	domain = parser['domain']
	inputFile = parser['inputFile']
	threads = parser['threads']

	if inputFile != None and threads != None:
		subdomainsfinder(domain, threads, inputFile)

	elif inputFile == None and threads != None:
		subdomainsfinder(domain, threads)
	
	else:
		subdomainsfinder(domain)
else: 
	
	url = parser['url']
	print(url)
	
	if isLink(url) and parser['javascript'] == None:

		source_code = requests.get(url).text
		outputFile = ''

		if parser['outputFile'] != None:
			outputFile = parser['outputFile']
			source(source_code, outputFile)
		else:
			source(source_code)
	
	elif isLink(url) and parser['js'] != None:
		
		source_code = requests.get(url).text
		jsLinks(source_code)


