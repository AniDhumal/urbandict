import bs4
import csv

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#grabs the url
my_url="https://www.urbandictionary.com/popular.php?character=A"
#downloads the contents of the url
uClient= uReq(my_url) 
#reds the contents
page_html=uClient.read()
uClient.close()

page_soup= soup(page_html, "html.parser")
class_items=page_soup.findAll("li",{"class":"word"})

filename="WordsofmofuckinA2.csv"
with open(filename,"w", encoding= 'utf-8') as f:

	headers=["Links","words","meaning1","meaning2","meaning3"]
	thewriter=csv.DictWriter(f,fieldnames= headers)
	thewriter.writeheader()



	for i in range (0,140):

		word_code=class_items[i]
		link="https://www.urbandictionary.com"+word_code.a["href"]
		#link="https://www.urbandictionary.com/define.php?term=Alex"
		word_name=word_code.a.text
		i=i+1
		

		uClient2=uReq(link)
		page2_html=uClient2.read()
		uClient2.close()
		page2_soup= soup(page2_html, "html.parser")
		

		var_mean=page2_soup.findAll("div",{"class":"meaning"})
		
				
		meaning00=var_mean[0].text.strip()
		meaning01=var_mean[2].text.strip()
		meaning02=var_mean[3].text.strip()

		thewriter.writerow({"Links":link, "words": word_name,"meaning1": meaning00,"meaning2":meaning01,"meaning3":meaning02})
f.close()	



	
