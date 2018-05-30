import requests
import json

access_token = "EAACEdEose0cBAOX7I9hkwBzafljrIROsLEZC0lDQfs2Y9OpNL4p1kuPZA7DskHZBZBny3n4ZAbhTz9XbobgUDbHyqKM3QRgaSDox7Pe6G9PiV8dvNw2zaPlhrDFJ0klYjWhZCrDw0YfYsingIDqepxZBPZCaB8q70cZABIp4ZBzSfkSy6dmRMJv5SvPeaxTa6HTKCOlbyCms60UAZDZD"
base_url ="https://graph.facebook.com/v3.0"


sql_id = base_url+"/me/likes?&access_token="+access_token

sql_post = base_url+"/me/posts?limit=100&fields=message,id&access_token="+access_token


posts = requests.get(sql_post)

if posts.status_code == 200:
	data = posts.json()

for post in data["data"]:

	print(post["id"])
	if post.has_key("message"):
		print(post["message"])