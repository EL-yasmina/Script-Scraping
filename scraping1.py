import requests   # import la bibliothèque requests
from bs4 import BeautifulSoup    # import la bibliothèque bs4

url = "https://fr.wikipedia.org/wiki/Test_de_performance"   
response = requests.get(url)   # envoi la requête

content = response.content
soup = BeautifulSoup(content, 'html.parser')  # utilisez 'html.parser' au lieu de 'html'

#print(content)

typeTest = soup.find_all("span", class_="mw-headline")
print(typeTest)

