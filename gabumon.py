from freq import getUrl
from main import subdomainfinder
import pyfiglet
import argparse
ascii_banner = pyfiglet.figlet_format("Gabumon",font="slant")
print (ascii_banner)
ascii_banner1 = pyfiglet.figlet_format("ALESAWE",font="digital")
print ("By \n"+ascii_banner1)


arparser = argparse.ArgumentParser()


arparser.add_argument(
"-m", "--mode", required=True, help="Enter the usage mode DNS\n for DNS enumaration\nHTML for HTML scanning"
)

arparser.add_argument(
"-d", "--domain", required=True, help="Domain to scan"
)

arparser.add_argument(
"-k", "--keywords", required=False, help="Subdomains to scan saperated by comma (e.g) corp,sports"
)

arparser.add_argument(
"-o", "--outputFile", required=False, help="Enter the name of the output file"
)

arparser.add_argument(
"-i", "--inputFile", required=False, help="Enter the name of the input file to get the subdomains from"
)


arparser.add_argument(
"-t", "--threads", required=False, help="Enter the number of threads"
)


parser = vars(arparser.parse_args())

MODE = parser['mode']



if MODE == 'DNS':

	domain = parser['domain']
	inputFile = parser['inputFile']
	threads = parser['threads']

	subdomainfinder(inputFile, domain, threads)

else: 
	pass

