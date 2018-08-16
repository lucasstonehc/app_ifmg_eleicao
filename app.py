# -*- Coding: UTF-8 -*-
#coding: utf-8
# encoding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from __future__ import unicode_literals
#import urllib2
from bs4 import BeautifulSoup
# Optional argument : if not specified WebDriver will search your system PATH environment variable for locating the chromedriver
from model import Model
from filegenerator import FileGenerator

class AppEleicoes(object):
    
	def __init__(self, arquivo_html):
		self.soup = BeautifulSoup(arquivo_html, 'html.parser') 
		self.soup.prettify() #normalizando


	def ToString(self):
		#Compartilhamento
		#procurar dentro da div os elementos necessários
		dives = self.soup.findAll("div", {"class":"_5pcr userContentWrapper"})

		count_dives = len(dives)
		posts = [] * count_dives
		i = 0 
		while i < count_dives:
			my_first_dive = dives[i] #minha primeira div, pegado atributos

			#datetimeOfPostPublication =  my_first_dive.find('abbr', class_ = '_5ptz timestamp livetimestamp').text #date
			try:
				datetimeOfPostPublication =  my_first_dive.find('abbr')['title'] #date
			except:
				datetimeOfPostPublication = ""

			try:
				datetimeOfCollect = "Today"
			except:
				datetimeOfCollect = ""

			try:
				text = "Text"
			except:
				text = ""

			try:
				comment = my_first_dive.find('a', class_ = '_ipm _-56').text #comment
			except:
			    comment = ""

			try:
				like = my_first_dive.find('span', attrs={'data-hover':'tooltip'}).text #likes
			except:
				like = ""

			try:
				share = my_first_dive.find('a', class_ = '_ipm _2x0m').text #shares
			except:
				share = ""

			try:
				tag = "tag"
			except:
				tag = ""

			try:
				view = my_first_dive.find('span', attrs={'aria-live':'polite'}) #view
			except:
				view = ""

			post = Model(datetimeOfPostPublication,datetimeOfCollect,text,comment,like,share,tag,view)
			posts.append(post.getModelObject())
			i+=1
		return posts #return list of posts
def namesOfCandidates(index):
	names = [0] * 13
	names[0] = "AlvaroDias"
	names[1] = "CaboDaciolo"
	names[2] = "CiroGomes"
	names[3] = "GeraldoAlckmin"
	names[4] = "GuilhermeBoulos"
	names[5] = "HenriqueMeirelles"
	names[6] = "JairBolsonaro"
	names[7] = "JoaoAmoedo"
	names[8] = "JoaoGoulartFilho"
	names[9] = "JoseMariaEymael"
	names[10] = "Lula"
	names[11] = "MarinaSilva"
	names[12] = "VeraLucia"
	if index == 0:
		return names[0]
	elif index == 1:
		return names[1]
	elif index == 2:
		return names[2]
	elif index == 3:
		return names[3]
	elif index == 4:
		return names[4]
	elif index == 5:
		return names[5]
	elif index == 6:
		return names[6]
	elif index == 7:
		return names[7]
	elif index == 8:
		return names[8]
	elif index == 9:
		return names[9]
	elif index == 10:
		return names[10]
	elif index == 11:
		return names[11]
	else:
		return names[12]



def main():
	listOfCandidates = [0] * 13 #all candidates

	listOfCandidates[0] = "https://www.facebook.com/pg/ad.alvarodias/posts/"
	listOfCandidates[1] = "https://www.facebook.com/pg/depudadocabodaciolo/posts/"
	listOfCandidates[2] = "https://www.facebook.com/pg/cirogomesoficial/posts/"
	listOfCandidates[3] = "https://www.facebook.com/pg/geraldoalckmin/posts/"
	listOfCandidates[4] = "https://www.facebook.com/pg/guilhermeboulos.oficial/posts/"
	listOfCandidates[5] = "https://www.facebook.com/pg/hmeirellesoficial/posts/"
	listOfCandidates[6] = "https://www.facebook.com/pg/jairmessias.bolsonaro/posts/"
	listOfCandidates[7] = "https://www.facebook.com/pg/JoaoAmoedoNOVO/posts/"
	listOfCandidates[8] = "https://www.facebook.com/pg/goulartoficial/posts/"
	listOfCandidates[9] = "https://www.facebook.com/pg/eymaelOficial/posts/"
	listOfCandidates[10] = "https://www.facebook.com/pg/Lula/posts/"
	listOfCandidates[11] = "https://www.facebook.com/pg/marinasilva.oficial/posts/"
	listOfCandidates[12] = "https://www.facebook.com/pg/verapstu/posts/"
    
    #login facebook
	driver = webdriver.Chrome(executable_path=r'C:\apps\chromedriver.exe')

	usr = "lucas-stone@live.com"
	pwd = ""
	# or you can use Chrome(executable_path="/usr/bin/chromedriver")
	driver.get("http://www.facebook.org")
	assert "Facebook" in driver.title
	elem = driver.find_element_by_id("email")
	elem.send_keys(usr)
	elem = driver.find_element_by_id("pass")
	elem.send_keys(pwd)
	elem.send_keys(Keys.RETURN)
	index = 0
	while index < len(listOfCandidates):
		driver.get(listOfCandidates[index])
		elem = driver.find_element_by_xpath("//*")
		source_code = elem.get_attribute("outerHTML")
		app = AppEleicoes(source_code)
		listOfPosts = app.ToString()
		file = FileGenerator(namesOfCandidates(index))
		i = 0
		while i < len(listOfPosts):
			file.write(listOfPosts[i])
			i+=1
		index+=1

	driver.quit()
	driver.close()

if __name__ == "__main__":
    main()

