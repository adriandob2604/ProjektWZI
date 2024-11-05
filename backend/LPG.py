import requests
from bs4 import BeautifulSoup
from engine import Session, Stacja
session = Session()

def lpg():
    url = "https://cenapaliw.pl/stationer/lpg/wszystko/wszystko/1"
    response = requests.get(url=url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    info = [b.text for b in soup.find_all('b')]
    # Station name, price
    cleaned_data = [item for item in info if 'zł' in item or 'Aby' not in item]
    paired_data = list(zip(cleaned_data[::2], cleaned_data[1::2]))
    # Price update date
    small = soup.find_all('small')[:-1]
    dates = [date.text.strip() for date in small if "/" in date.text.strip()]
    # Adress
    td = soup.find_all('td')
    td_text = [t.find(string=True, recursive=False) for t in td]
    return paired_data



print(lpg())