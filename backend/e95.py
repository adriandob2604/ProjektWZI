import requests
from bs4 import BeautifulSoup
from engine import Session, Stacja
session = Session()
def get_e95():
    official_list = []
    i = 1
    while True:
        url = f"https://cenapaliw.pl/stationer/e95/wszystko/wszystko/{i}"
        i += 1
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
        paired_data = list(zip(cleaned_data[::2], cleaned_data[1::2]))
        # Price update date
        small = soup.find_all('small')[:-1]
        dates = [date.text.strip() for date in small if "/" in date.text.strip()]
        # Adress
        td = soup.find_all('td')
        td_text = [t.find(string=True, recursive=False) for t in td if t.find(string=True, recursive=False) not in ["\n", None, "Więcej cen po reklamie:"]]

        for j in range(len(paired_data)):
            if paired_data[j] not in official_list:
                name, adres, price, actual_date = paired_data[j][0], td_text[j], paired_data[j][1], dates[j]
                if price == "Brak danych":
                    session.commit()
                    session.close()
                    return
                existing_station = session.query(Stacja).filter_by(name=name, adres=adres).first()
                if existing_station:
                    existing_station.price = price
                    existing_station.actual_date = actual_date
                else:
                    stacja = Stacja(name=name, adres=adres, price=price, actual_date=actual_date)
                    session.add(stacja)
    session.commit()
    session.close()

get_e95()