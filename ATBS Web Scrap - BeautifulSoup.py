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
print('The price is ' + price)


#Example2 Work in Progress
#Example 2 - I'll get the price from an active price changing title and one of my watchlist title from steam
def getPrice(Url):
    rs = requests.get(Url) #def rs to get the item of the url
    rs.raise_for_status()  #set to raise any exception on error

    pull = bs4.BeautifulSoup(rs.text, 'html.parser') #def pull into using the bs4 module and parse html into text
    ele = pull.select('#prcIsum') 
    return ele[0].text.strip()

print('%s is currently priced at %s' %(Title, Price))

Rocket league
body > div.responsive_page_frame.with_header > div.responsive_page_content > div.responsive_page_template_content > div.game_page_background.game > div.page_content_ctn > div.page_title_area.game_title_area.page_content > div.apphub_HomeHeaderContent > div > div.apphub_AppName
#game_area_purchase > div:nth-child(1) > div > div.game_purchase_action > div > div.game_purchase_price.price

Faster Than Light
body > div.responsive_page_frame.with_header > div.responsive_page_content > div.responsive_page_template_content > div.game_page_background.game > div.page_content_ctn > div.page_title_area.game_title_area.page_content > div.apphub_HomeHeaderContent > div > div.apphub_AppName
#game_area_purchase > div:nth-child(1) > div > div.game_purchase_action > div > div.game_purchase_price.price






