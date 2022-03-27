import requests
import random
import pandas as pd
from bs4 import BeautifulSoup as bs

free_proxy_url = 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt' # TODO

# recuoerer le contenu du fichier url proxy
# TODO

proxy= requests.get(free_proxy_url)
# print(proxy.text)

# # Convert the http response to list of proxy
list_proxy= proxy.text.strip().split("\n")
# print(list_proxy)
#definir une fonction kap retounen on proxy de maniere aleatoire
def get_random_proxy(array):
	''' get a random proxy '''
	proxy = random.choice(array)

# 	# to get more info on the proxy format
# 	# More info, visit: https://docs.python-requests.org/en/latest/api/#module-requests
	return{"http":proxy} # {'protocol': 'ip:port'} # TODO
# print(get_random_proxy(list_proxy))

#cherche proxy ki fonctionne yo
def get_working_proxy():
	''' test random proxies, to get one that works'''
	TOTAL_TESTS = 20
	for _ in range(TOTAL_TESTS):
		
		proxy = get_random_proxy(list_proxy) # TODO
		print("test proxy", proxy)
		try:
			requests.get("https://google.com", proxies = proxy) # TODO
			# if it works, return it
			print(proxy,"trouve")
			return proxy
		except Exception as error:
			print(error)

#get_working_proxy()

# # set a custom header objet simule on navigateur pou yo panse son navigateur kap lansel
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36' # TODO
}

# # call and get the proxy
proxy = get_working_proxy()
if proxy:
	tableau=[]
	page=1
	for page in range(10):
		res = requests.get('https://lenouvelliste.com/national?page='+str(page), headers=headers, proxies=proxy) # TODO


		# init the beautiful instance as html parser
		soup = bs(res.text , 'html.parser') # TODO
		Div=soup.find_all("div", {"class":"content_widget"})
		for element in Div:
			titre=element.find("a").text
			#recuperation attribut
			lien=element.find("a")["href"]
			tableau.append({"titre":titre,"url":lien})

			print(titre)
		# After collecting the data needed, convert it to pandas dataframe
	# TODO convertir donnee en dataframe 
		dataframe= pd.DataFrame(tableau)
		# then export it as csv
		dataframe.to_csv('Lamysere.csv') # TODO
else:
	print('No working proxy found. Go buy some instead')
