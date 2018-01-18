import bs4
import requests

def getPrice(Url):
    rs = requests.get(Url)
    rs.raise_for_status()

    soup = bs4.BeautifulSoup(rs.text, 'html.parser')
    ele = soup.select('#prcIsum')
    return ele[0].text.strip()


price = getPrice('https://www.ebay.com/itm/NEW-PS4-Monster-Hunter-World-Collectors-Edition-DLC-PlayStation-4-JAPAN-IMPORT/162812830120?hash=item25e866a1a8:g:dG0AAOSwAaJaOlRF')
print('The price is ' + price)