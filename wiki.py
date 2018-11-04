import requests


request = requests.get('https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch=9%20rue%20Las%20Cases&formatversion=2&prop=revisions&rvprop=content&format=json&formatversion=2')
return_json_API = request.json()#get json file

print(type(return_json_API))

#for element in return_json_API:
  #  print(element)
print(return_json_API["query"]["search"][0]["snippet"])

search_JSON = return_json_API["query"]


search_JSONII = search_JSON["search"]
search_JSONIII = search_JSONII[0]

wiki = search_JSONIII["snippet"]



#print(wiki)
print(type(wiki))