import requests   # import la bibliothèque requests
from bs4 import BeautifulSoup    # import la bibliothèque bs4

url = "https://meteofrance.com/previsions-meteo-france/paris/75000"   
response = requests.get(url)   # envoi la requête

content = response.content
soup = BeautifulSoup(content, 'html.parser')  # utilisez 'html.parser' au lieu de 'html'

temperature = soup.find( 'strong', class_='temp').text  # utilisez .text pour obtenir le texte et .strip() pour enlever les espaces
#ressenti = soup.find('span', class_='ressenti')
#etat_ciel = soup.find('span', class_='etat-ciel')

print("Météo à Paris: ")
print("Température :"+ temperature) 
#print("ressenti: " + ressenti)
#print("etat_ciel: " + etat_ciel)