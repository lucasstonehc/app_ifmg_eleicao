import requests
import json
import os
from file_generator import FileGenerator
#cada 2 horas tenho que renovar o token

class Crawler(object):


	def __init__(self): #construtor
		self.access_token = "EAACEdEose0cBAGDEyzdKZCLwEHymOXsxccuRwNhUeoT16YEEXnDvc5iBhksTroZA5CZBLLjqaifmva7F4p3vZCfvoHyLSzksPnjS70uN9pG2LfeeMsiSzmULrNsDNpLmWuCwp60n17V0GjQCqtVAM7yG2GZAPKVAL58SuZAL5sqLq80dePZCIfOb8n2BSeITzcZD"
		self.base_url ="https://graph.facebook.com/v3.0"
		self.sql_lists = set()

	def sqllinecommand(self):
		#lista de comandos get api facebook
		sql_likes = self.base_url+"/me/likes?&access_token="+self.access_token
		sql_post = self.base_url+"/me/posts?limit=100&fields=message,id&access_token="+self.access_token

		self.sql_lists.add(sql_likes)
		self.sql_lists.add(sql_posts)

	def likes(self):
		response = requests.get(self.sql_lists[0])

		if response.status_code == 200:
			data = response.json()

		page_liked_by_me = set()
		for page in data["data"]:
			page_liked_by_me.add(page["name"])
	

	def posts(self):	

		response = requests.get(self.sql_lists[1])

		if response.status_code == 200:
			data = response.json()

		for post in data["data"]:
			message = ""
			print(post["id"])
			if "message" in post:
				message = post["message"]


