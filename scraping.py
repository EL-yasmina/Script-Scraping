import requests   # import la bibliothèque requests
from bs4 import BeautifulSoup    # import la bibliothèque bs4

url = "https://meteofrance.com/previsions-meteo-france/paris/75000"    
response = requests.get(url)   # envoi la requête
#print(response)
content = response.content
soup = BeautifulSoup(content, 'html.parser')  # utilisez 'html.parser' au lieu de 'html'
#print(soup)
temperature = soup.find(id="primary_content")
#ressenti = soup.find('span', class_='ressenti')
#etat_ciel = soup.find('span', class_='etat-ciel')


print(temperature) 
#print("ressenti: " + ressenti)
#print("etat_ciel: " + etat_ciel)