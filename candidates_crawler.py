

# varrer às páginas públicas dos candidatos
# estipular um período de varredura

#Suposta lista -> exemplo -> depois coletar realmente quais serão os candidatos
#Luiz Inácio Lula, Ciro Gomes, Aécio Neves, Marina Silva, Álvaro Dias, Cristovam, José Serra, Geraldo Alckmin, Jair Bolsonaro, Ronaldo Caíado

#PEGAR TUDO DE UMA VEZ
	#GET graph.facebook.com
	#/photos?ids={user-id-a},{user-id-b}
'''
	CRIAR um arquivo para candidato.
'''

'''Página oficial ID: 
	Luiz Inácio Lula:
	LINKS: //www.facebook.com/2018lula/  --- ID = 303993023389132
		  //www.facebook.com/Lula-Oficial-114272049388983/ --- ID = 114272049388983
          //www.facebook.com/PresidenteLula13/ ---  ID = 1273688872753126
          //www.facebook.com/Lula/  --- ID = 267949976607343

	Ciro Gomes:
	LINKS:
		//www.facebook.com/cirogomesoficial/  --- ID = 1216504185136925
		//www.facebook.com/TimeCiroGomes/   --- ID = 1453548241604118
		//www.facebook.com/oCiroGomes/     --- ID = 1624304177798362
		//www.facebook.com/CIROGBRASILEIRO/ --- ID = 1642911379256060

	Aécio Neves:
	LINKS:
		//www.facebook.com/AecioNevesOficial/ --- ID = 411754008869486
		//www.facebook.com/aecionevesdacunha/  --- ID = 96990998628
		//www.facebook.com/Aécio-Neves-45-Presidente-2018-886650364687404/  --- ID = 886650364687404

	Marina Silva:
	LINKS:
		//www.facebook.com/marinasilva.oficial/  --- ID = 126351747376464
		//www.facebook.com/nossamarina/  --- ID = 196282877151977
		//www.facebook.com/Marina-Silva-Presidente-2018-652587981427008/ --- ID = 652587981427008

	Álvaro Dias:
	LINKS:
		//www.facebook.com/ad.alvarodias/?ref=br_rs --- ID = 199599520097304
		//www.facebook.com/Presidente.Alvaro.Dias/ --- ID = 1801560020115618
		//www.facebook.com/eleitoresdealvarodias/  --- ID = 584005138358006

	Cristovam:
	LINKS:

	José Serra:
	LINKS:

	Geraldo Alckmin:
	LINKS:

	Jair Bolsonaro:
	LINKS:
		//www.facebook.com/jairmessias.bolsonaro/  --- ID = 211857482296579
		//www.facebook.com/bolsonaropresidente2018sim/ --- ID = 471964666469200
		//www.facebook.com/movimentobrasiladireita/  --- ID = 402760906551545

	Ronaldo Caíado:
	LINKS:
'''

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
    
		
