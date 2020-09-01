import bs4
import csv

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

filename="WordsStartingFromA.csv"
with open(filename,"w", encoding= 'utf-8') as f:

	headers=["Links","words","meaning1","meaning2","meaning3"]
	thewriter=csv.DictWriter(f,fieldnames= headers)
	thewriter.writeheader()

	#grabs the url
	my_url="https://www.urbandictionary.com/browse.php?character=A"
	#downloads the contents of the url
	uClient= uReq(my_url) 
	page_html=uClient.read()
	uClient.close()
	#reds the contents
	page_soup=soup(page_html, "html.parser")

	for k in range (2,1000):
		#loop for browsing through pages
		k_st=str(k)
		link="https://www.urbandictionary.com/browse.php?character=A&page="+k_st

		#reads link of the current page
		uClient2=uReq(link)
		link_html=uClient2.read()
		uClient2.close()
		page_soup2= soup(link_html,"html.parser")

		class_items_ul=page_soup2.findAll("ul",{"class","no-bullet"})
		class_items=class_items_ul[0].findAll("li")
		i=0
		for i in range (i,len(class_items)):

			word_code=class_items[i]
			link_word='https://www.urbandictionary.com'+word_code.a["href"]
			
			word_name=word_code.a.text
			i=i+1
			

			uClient3=uReq(link_word)
			page3_html=uClient3.read()
			uClient3.close()
			page3_soup= soup(page3_html, "html.parser")
			

			var_mean=page3_soup.findAll("div",{"class":"meaning"})
			
			#error here 
			#var_mean is the list of the various meanings of the same word
			#var_mean[1] is excluded because it is for the word of the day

			meaning00=var_mean[0].text.strip()
			meaning01=0
			meaning02=0

			thewriter.writerow({"Links":link, "words": word_name,"meaning1": meaning00,"meaning2":meaning01,"meaning3":meaning02})#hithe pn problem yeil vattay

		k=k+1
	f.close()
