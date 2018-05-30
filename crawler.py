import requests
import json
import os
from file_generator import FileGenerator
#cada 2 horas tenho que renovar o token
access_token = "EAACEdEose0cBAGDEyzdKZCLwEHymOXsxccuRwNhUeoT16YEEXnDvc5iBhksTroZA5CZBLLjqaifmva7F4p3vZCfvoHyLSzksPnjS70uN9pG2LfeeMsiSzmULrNsDNpLmWuCwp60n17V0GjQCqtVAM7yG2GZAPKVAL58SuZAL5sqLq80dePZCIfOb8n2BSeITzcZD"
base_url ="https://graph.facebook.com/v3.0"


#lista de sqls
sql_likes = base_url+"/me/likes?&access_token="+access_token

sql_post = base_url+"/me/posts?limit=100&fields=message,id&access_token="+access_token


#aqui, irei criar uma classe com métodos para cada sql 
def likes():
	res = requests.get(sql_likes)

	if res.status_code == 200:
		data = res.json()

	page_liked_by_me = set()
	for page in data["data"]:
		page_liked_by_me.add(page["name"])
		


posts = requests.get(sql_post)

if posts.status_code == 200:
	data = posts.json()

file = FileGenerator()

for post in data["data"]:

	message = ""
	print(post["id"])
	if "message" in post:
		message = post["message"]

	file.write_file(post["id"]+message)



