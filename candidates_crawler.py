

# varrer às páginas públicas dos candidatos
# estipular um período de varredura

#Suposta lista -> exemplo -> depois coletar realmente quais serão os candidatos
#Luiz Inácio Lula, Ciro Gomes, Aécio Neves, Marina Silva, Álvaro Dias, Cristovam, José Serra, Geraldo Alckmin, Jair Bolsonaro, Ronaldo Caíado

#PEGAR TUDO DE UMA VEZ
	#GET graph.facebook.com
	#/photos?ids={user-id-a},{user-id-b}


#Página oficial ID: Luiz Inácio Lula-> 114272049388983

import requests
import json
import os
from file_generator import FileGenerator

class CandidatesCrawler(object):

	def __init__(self): #construtor
		self.access_token = "EAACEdEose0cBABaZB0zr7PdlzcUZB4TcdCCZBktbbzlUQo5ZAd7owZBcUZCPrqwsWviah5DvoDZBFf932OkYlnZBohcAY81ZC2G52rjiNs3h9ZADyHPbEf0P50nHgQrxFnj64VZCYgpHYURlyNchgJlL267ctQleeZC7Tk9gizrcoQl4n9kdCnOOncD2Em3THlwMA5YZD"
		self.base_url ="https://graph.facebook.com/v3.0"
		self.after = ""
		self.sql_lists = set()

	def sqllinecommand(self):
		sql_feed = self.base_url+"/feed&access_token="+self.access_token
		self.sql_lists.add(sql_feed)

	def get_feed(self):
		file = FileGenerator() #instância para o gerador de arquivos
		#Pela primeira vez devo pegar o field after para montar a query logo em seguida
		#segunda vez
		#flag para 20 nexts, porém terei que descobrir até quando posso fazer o next
		i = 0
		while i < 4:
			if i == 0:
				response = requests.get(self.base_url+"/114272049388983/feed?&access_token="+self.access_token+"&pretty=0&limit=100")

				if response.status_code == 200:
					data = response.json()
				
				#file.write_file("FEED "+str(i))
				file.write_file(data["data"])
				
				self.after = data["paging"]["cursors"]["after"]
				i+=1
			else:

				#montando a request para as seguintes páginas
				response = requests.get(self.base_url+"/114272049388983/feed?&access_token="+self.access_token+"&pretty=0&limit=100&after="+self.after)

				if response.status_code == 200:
					data = response.json()

				file.write_file("FEED "+str(i))
				file.write_file(data["data"])
				
				self.after = data["paging"]["cursors"]["after"]

			i+=1

c = CandidatesCrawler() 
c.get_feed()



#"next": "https://graph.facebook.com/v3.0/114272049388983/feed?access_token=EAACEdEose0cBAKDVJ8AKnmUsciastE3wFUFxPfZATArKZC4FVQkmYb04bOdjotlQc3599l2D9D0UclWX438ct30Vc6AOjfKAhPJ0rZAjoTeknUr5J0tVbse9G5AZBmnxJWm73MF92vIjAXsh9rDHTyikxlNeQ5AI6EK9PLJg9vTJjHmxaqx9cOEMtcz1aZBcZD&pretty=0&limit=25&after=Q2c4U1pXNTBYM0YxWlhKNVgzTjBiM0o1WDJsa0R5TXhNVFF5TnpJd05Ea3pPRGc1T0RNNkxUTTNPRGt5TnpBM016RTJOemMyTURJeU5BOE1ZAWEJwWDNOMGIzSjVYMmxrRHg4eE1UUXlOekl3TkRrek9EZAzVPRE5mTVRnd09EVXlPVEE1TXprM05UWXpEd1IwYVcxbEJscmRLMzBC",
    
		
