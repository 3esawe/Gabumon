import requests
import concurrent.futures
from freq.utils import parseFileToList


statusC = []

def statusCodes(status):

	global statusC
	statusC = [int(i) for i in status.split(',')]

def bruteForceScanner(url, word):

	surl = url + '/' + word

	if len(statusC) > 0:
		
		response = requests.get(surl)
		if response.status_code in statusCCodes:
			print ("[+] found:- {}     {}".format(surl, response.statusC_code))
		

	else:
		
		response = requests.get(surl)
		
		if response.status_code == 200:
			
			print ("[+] found :- ",surl)

		else:	
			print ("[-] Not found :- ",surl)
			pass



def bruteForce(url ,wordlist ):

	#Schedules the callable, fn, to be executed as fn(*args **kwargs) and returns a Future object representing the execution of the callable.
	threadpool = concurrent.futures.ThreadPoolExecutor( 
	max_workers=1000)

	wordlist = parseFileToList(wordlist)
	futures = (threadpool.submit(bruteForceScanner, url, word) for word in wordlist) 

	for i in concurrent.futures.as_completed(futures):
		pass


