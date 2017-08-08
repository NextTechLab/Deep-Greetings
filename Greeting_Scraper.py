#dependencies
from bs4 import BeautifulSoup
import requests
import re

#stores url
url = raw_input("Enter a website to extract the URL's from: ")

req = requests.get(url)

#stores All the text on that page 
data = req.text

extract = "";

#soup ready
soup = BeautifulSoup(data)

#replace em with required html header
for link in soup.find_all('p'):
    extract=extract+(str(link))

#File created  
f1=open('Halloween_Data', 'a')

#Tag removal
result = re.sub('<.*?>','',extract)

#Data Writtern
f1.write(result)
	
f1.close()
