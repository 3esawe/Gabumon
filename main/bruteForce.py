import requests
import concurrent.futures
from freq.utils import parseFileToList


def bruteForceScanner(url, word):
	
	print(word)
	surl = url+word

	response = requests.get(surl)

	if (response.status_code == 200):
		print ("[+] found :- ",surl)
		write(word)
	
	else:	
		print ("[-] Not found :- ",surl)
		pass



def bruteForce(url ,wordlist = '/root/Gabumon/main/subdomains-top1million-5000.txt'):

	#Schedules the callable, fn, to be executed as fn(*args **kwargs) and returns a Future object representing the execution of the callable.
	threadpool = concurrent.futures.ThreadPoolExecutor( 
	max_workers=1000)

	wordlist = parseFileToList(wordlist)
	futures = (threadpool.submit(bruteForceScanner, url, word) for word in wordlist) 

	for i in concurrent.futures.as_completed(futures):
		pass



# for i in range(2000):
# 	word = fo.readline(10).strip()

# 	#print (surl)
	

# 	#print (response)
