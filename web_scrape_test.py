import bs4
import csv

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


woday="Schrödinger's Douchebag"
#number of pages in the current letter 
nos_page=744 
filename="webscrape_test4.csv"





with open(filename,"w", encoding= 'utf-8') as f:

	headers=["Links","words","meaning1","meaning2","meaning3"]
	thewriter=csv.DictWriter(f,fieldnames= headers)
	thewriter.writeheader()


	#grabs the url of the first page 

	my_url="https://www.urbandictionary.com/browse.php?character=A"
	#my_url="https://www.urbandictionary.com/browse.php?character=A&page=744"
	
	

	#downloads the contents of the url
	uClient= uReq(my_url) 
	#reds the contents
	page_html=uClient.read()
	uClient.close()

	page_soup= soup(page_html, "html.parser")
	pre_class_items=page_soup.find("ul", "no-bullet")
	class_items=pre_class_items.findAll("li")

	

	for i in range (0,len(class_items)): #looping through the words of a single page 

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
		var_def=page2_soup.findAll("div",{"class":"def-header"})

		
		if len(var_mean)==1:
			meaning00=var_mean[0].text.strip().replace(",", "  ")
			thewriter.writerow({"Links":link, "words": word_name,"meaning1": meaning00})


		else:

			sec_word=var_def[1].text
			if sec_word==woday:

				if len(var_mean)==2:
					meaning00=var_mean[0].text.strip()
					thewriter.writerow({"Links":link, "words": word_name,"meaning1": meaning00})

				elif len(var_mean)==3:
					meaning00=var_mean[0].text.strip()
					meaning01=var_mean[2].text.strip()
					thewriter.writerow({"Links":link, "words": word_name,"meaning1": meaning00,"meaning2":meaning01})	

				else :
					meaning00=var_mean[0].text.strip()
					meaning01=var_mean[2].text.strip()
					meaning02=var_mean[3].text.strip()
					thewriter.writerow({"Links":link, "words": word_name,"meaning1": meaning00,"meaning2":meaning01,"meaning3":meaning02})


			elif sec_word!=woday:

				if len(var_mean)==2:
					meaning00=var_mean[0].text.strip()
					meaning01=var_mean[1].text.strip()
					thewriter.writerow({"Links":link, "words": word_name,"meaning1": meaning00,"meaning2":meaning01})

				else :
					meaning00=var_mean[0].text.strip()
					meaning01=var_mean[1].text.strip()
					meaning02=var_mean[2].text.strip()
					thewriter.writerow({"Links":link, "words": word_name,"meaning1": meaning00,"meaning2":meaning01,"meaning3":meaning02})	 






	for j in range(2,4): #traverses through the multiple pages 
		#grabs the url
		my_url="https://www.urbandictionary.com/browse.php?character=A&page="+str(j)
		#my_url="https://www.urbandictionary.com/browse.php?character=A&page=744"
		
		

		#downloads the contents of the url
		uClient= uReq(my_url) 
		#reds the contents
		page_html=uClient.read()
		uClient.close()

		page_soup= soup(page_html, "html.parser")
		pre_class_items=page_soup.find("ul", "no-bullet")
		class_items=pre_class_items.findAll("li")

		

		for i in range (0,len(class_items)): #looping through the words of a single page 

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
			var_def=page2_soup.findAll("div",{"class":"def-header"})

			
			if len(var_mean)==1:
				meaning00=var_mean[0].text.strip().replace(",", "  ")
				thewriter.writerow({"Links":link, "words": word_name,"meaning1": meaning00})


			else:

				sec_word=var_def[1].text
				if sec_word==woday:

					if len(var_mean)==2:
						meaning00=var_mean[0].text.strip()
						thewriter.writerow({"Links":link, "words": word_name,"meaning1": meaning00})

					elif len(var_mean)==3:
						meaning00=var_mean[0].text.strip()
						meaning01=var_mean[2].text.strip()
						thewriter.writerow({"Links":link, "words": word_name,"meaning1": meaning00,"meaning2":meaning01})	

					else :
						meaning00=var_mean[0].text.strip()
						meaning01=var_mean[2].text.strip()
						meaning02=var_mean[3].text.strip()



				elif sec_word!=woday:

					if len(var_mean)==2:
						meaning00=var_mean[0].text.strip()
						meaning01=var_mean[1].text.strip()
						thewriter.writerow({"Links":link, "words": word_name,"meaning1": meaning00,"meaning2":meaning01})

					else :
						meaning00=var_mean[0].text.strip()
						meaning01=var_mean[1].text.strip()
						meaning02=var_mean[2].text.strip()
						thewriter.writerow({"Links":link, "words": word_name,"meaning1": meaning00,"meaning2":meaning01,"meaning3":meaning02})	 

f.close()	


