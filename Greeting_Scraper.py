#dependencies
from bs4 import BeautifulSoup
import requests

#stores url
url = raw_input("Enter a website to extract the URL's from: ")

req = requests.get(url)

#stores All the text on that page 
data = req.text

extract = [];

#soup ready
soup = BeautifulSoup(data)

#replace em with required html header
for link in soup.find_all('p'):
    extract.append(str(link))

#File created 
#File re-writtern each time 
f1=open('Halloween_Data', 'w+')

#Slight Processing
for sentence in extract:
	sentence = sentence[4:len(sentence)-5]
	for char in sentence:
		#replace kink(~) with any other character that precedes
		#author name/unwanted excess in data
		if char=='~':
			break
		f1.write(char)
	f1.write('\n')

f1.close()
