# Made in Python 3.5

import urllib.request

def find_links():
    print("[ + ] Collecting MD5 hash links")
    links = []
    content = urllib.request.urlopen("https://virusshare.com/hashes.4n6").read().decode("utf-8").splitlines()
    for i in content:
        if 'http' and ".md5" in i:
            tmp = i
            start = tmp.find('href="') + len('href="')
            tmp = tmp[start:]
            end = tmp.find('"')
            tmp  = tmp[:end]
            links.append("https://virusshare.com/" + tmp)
    return visit_links(links)

def visit_links(links):
    print("[ + ] Writing hashes that were found on into text files")
    print("[ ! ] This may take long as you downloading over 30 million signatures (all in all around to 1 GB) ")
    for url in links:
        if ".md5" in url: # the crawler can f*ck up the links sometimes
            signatures = urllib.request.urlopen(url).read().decode("utf-8").splitlines()
            tmp = url.strip("https://virusshare.com/")
            file = tmp + ".txt"
            print("[ * ] Writing hashes from url {0} into {1}".format(url, file))
            f = open(file, "w")
            for i in range(6, len(signatures)):
                f.write(signatures[i] + "\n")
            f.close

find_links()
