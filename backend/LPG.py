import requests
from bs4 import BeautifulSoup
from engine import Session, LPG
session = Session()

def lpg():
    i = 1
    while True:
        url = f"https://cenapaliw.pl/stationer/lpg/wszystko/wszystko/${i}"
        try:
            response = requests.get(url=url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Problem z pobieraniem danych: {e}")
            break
        soup = BeautifulSoup(response.text, 'html.parser')
        info = [b.text for b in soup.find_all('b')]
        # Station name, price
        cleaned_data = [item for item in info if 'zł' in item or 'Aby' not in item]
        name_price = list(zip(cleaned_data[::2], cleaned_data[1::2]))
        # Price update date
        small = soup.find_all('small')[:-1]
        date = [date.text.strip() for date in small if "/" in date.text.strip()]
        # Adress
        td = soup.find_all('td')
        adress = [t.find(string=True, recursive=False) for t in td]
        for i in range(len(name_price)):
            name, adres, price, actual_date = name_price[i][0], adress[i], name_price[i][1], date[i] 
            if adres is not None:
                if price == "Brak danych":
                    session.commit()
                    session.close()
                    return
            stacja = LPG(name, adres, price, actual_date)
            if not session.query(LPG).filter(name=name).first():
                session.add(stacja)
            else:
                first_station = session.query(LPG).filter_by(name=name, adres=adres).first()
                first_station['price'] = price
                first_station['actual_date'] = actual_date
    session.commit()
    session.close()
print(lpg())