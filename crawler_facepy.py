from facepy import GraphAPI

oauth_access_token = "EAACEdEose0cBAK4ZBgCdb0bqbye5dqK4Xy4201HYFZA76iU4RYF4KxAZANp0Kgh3OB3hg1GpUw7hje2wFI7lEZAmrU45JUdjT8y7DhvjuxVBpx94hEIUnHBqfTSaawLJEvlctIw1QOtkByIsMESjbYrcZCdUtOWMaAMswAdkJi4kTzmTkqu1UiKKYSy5qDfFn8cZBIpN1OlQZDZD"

graph = GraphAPI(oauth_access_token)

me_posts = graph.get('me/posts?limit=100&fields=id,message')

for data in me_posts["data"]:
	
	print(data["id"],data["message"])
	if data["message"] != None:
		print(data["message"])
	

##users = graph.search(type='user',q='Mark Zuckerberg', ) 

##for user in users['data']:
	##print('%s %s' % (user['id'],user['name'].encode()))

