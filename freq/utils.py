def isLink(url):

	if "http://" not in url and "https://" not in url:
		return False
	return True


def parseFileToList(inFile):
	with open (inFile, 'r') as handle:
		inList = handle.readlines()
	inList = [x.strip() for x in inList]
	# print(inList)
	return inList



def writeFile(data, fileName):
	with open (fileName, 'a') as fd:
		fd.write(data+'\n')


def getUrl(url, GET):
    if GET:
        return url.split('?')[0]
    else:
        return url


