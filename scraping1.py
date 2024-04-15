import requests   # import la bibliothèque requests
from bs4 import BeautifulSoup    # import la bibliothèque bs4

url = "https://fr.wikipedia.org/wiki/Java"   
response = requests.get(url)   # envoi la requête

content = response.content
soup = BeautifulSoup(content, 'html.parser')  # utilisez 'html.parser' au lieu de 'html'

#print(content)

typeTest = soup.find( class_="mw-page-title-main")
print(typeTest.text)

