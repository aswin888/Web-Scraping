# webscarping with python
import re
#we are going to scrape google
import requests
#request is a module to make a request to a web page and to print the response

from bs4 import BeautifulSoup
#bs4 helps to pull data from HTML and XML files

result = requests.get("https://www.google.com/")
#sent a GET request to the url

print(result.status_code)
#The above statement is just to show that the request was succesful

#print(result.headers)
#The above prints the header to make sure that we are on the required page 

src = result.content
#To store the content
#print(src) ----> prints all the content of the web page

soup = BeautifulSoup(src , 'lxml')
#parsing uisng bs

links = soup.find_all("a")
#finds all elemts with anchoe tag

for link in links:
    if "About" in link.text:
# looks for link with about text           
        print(link)
#prints them        
        print(link.attrs['href'])