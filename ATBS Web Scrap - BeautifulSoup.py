#! Python3

#Module we need to import in this code
import bs4
import requests


#Example 1 - I'll be getting the price of a PS4 Pro Monster Hunter Bundle from eBay
def getPrice(Url):
    rs = requests.get(Url) #def rs to get the item of the url
    rs.raise_for_status()  #set to raise any exception on error

    pull = bs4.BeautifulSoup(rs.text, 'html.parser') #def pull into using the bs4 module and parse html into text
    ele = pull.select('#prcIsum') 
    return ele[0].text.strip()


price = getPrice('https://www.ebay.com/itm/NEW-PS4-Monster-Hunter-World-Collectors-Edition-DLC-PlayStation-4-JAPAN-IMPORT/162812830120?hash=item25e866a1a8:g:dG0AAOSwAaJaOlRF')

print('For example one:' + '\n' + 'The price is ' + price)


#Example 2 - I'll get the price from a local game retailer

# now the title are save in order of an dictionary, Url > ProductCSS > PriceCSS
P1 = ['http://www.impulse.com.my/playstation/ps4-console/playstation-4-pro-1tb-asia-set-black-1-years-warranty.html', '#content > h1', '#content > div.product-info > div.right > div.price > span.price-new']
P2 = ['http://www.impulse.com.my/playstation/ps4-console/playstation-4-pro-1tb-asia-set-star-wars-battlefront-2-bundle-1-years-warranty-eta-17-11-2017.html', '#content > h1', '#content > div.product-info > div.right > div.price > span.price-new']
P3 = ['http://www.impulse.com.my/playstation/ps4-console/playstation-4-slim-500gb-asia-set-black-1-year-warranty.html', '#content > h1', '#content > div.product-info > div.right > div.price > span.price-new']
P4 = ['http://www.impulse.com.my/playstation/ps4-console/playstation-4-slim-500gb-asia-set-hits-2-bundle-1-year-warranty.html', '#content > h1', '#content > div.product-info > div.right > div.price > span.price-new']


def getit(x):
    TC = e2TitleCheck(x)
    PC = e2PriceCheck(x)
    print('%s is currently priced at %s' % (TC, PC))

def e2PriceCheck(x):
    e2Url = x[0]
    e2Price = x[2]
    e2rs = requests.get(e2Url) #def rs to get the item of the url
    e2rs.raise_for_status()  #set to raise any exception on error

    roll = bs4.BeautifulSoup(e2rs.text, 'html.parser') #def pull into using the bs4 module and parse html into text
    gprice = roll.select(e2Price)
    return gprice[0].text.strip()

def e2TitleCheck(x):
    e2Url = x[0]
    e2Title = x[1]
    e2rs = requests.get(e2Url) #def rs to get the item of the url
    e2rs.raise_for_status()  #set to raise any exception on error

    roll = bs4.BeautifulSoup(e2rs.text, 'html.parser') #def pull into using the bs4 module and parse html into text
    gtitle = roll.select(e2Title)
    return gtitle[0].text.strip()

print('For example two:')
print(getit(P1))
print(getit(P2))
print(getit(P3))
print(getit(P4))
