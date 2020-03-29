from freq import *

from main.bruteForce import bruteForce, statusCodes
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
"-m", "--mode", required=True, help="Enter the usage mode DNS\n for DNS enumaration\nURL for HTML scanning \nDIR for Directory Brute-Forcing\n(i.e.)python3 gabumon [mode]"
)

arparser.add_argument(
"-d", "--domain", required=False, help="Domain to scan in [DNS] mode"
)

arparser.add_argument(
"-u", "--url", required=False, help="Url to scan in [URL, DIR] mode"
)

arparser.add_argument(
"-o", "--outputFile", required=False, help="Enter the name of the output file"
)

arparser.add_argument(
"-i", "--inputFile", required=False, help="Enter the path to the wordlist [DIR] mode"
)


arparser.add_argument(
"-s", "--status", required=False, help="Enter HTTP response codes you want to see "
)



parser = vars(arparser.parse_args())

MODE = parser['mode']


if MODE not in ['DNS', 'URL', 'URL']:
	arparser.print_help()
	exit()

	
if MODE == 'DNS':

	domain = parser['domain']
	inputFile = parser['inputFile']


	if inputFile != None:
		subdomainsfinder(domain, threads, inputFile)


	else:
		res = subdomainsfinder(domain)
		for i in res:
			print(i)

elif MODE == 'URL':
	
	url = parser['url']
	
	outputFile = ''

	if parser['outputFile'] != None:
		outputFile = parser['outputFile']
		source(url, outputFile)
	else:
		source(url)

else:

	url = parser['url']
	status = parser['status']
	
	if status:
		statusCodes(status)

	if parser['inputFile']:
		bruteForce(url, parser['inputFile'])
	
	else:
		
		bruteForce(url)



