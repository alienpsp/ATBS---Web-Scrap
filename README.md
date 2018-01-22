#ATBS---Web-Scrap

Automate The Boring Stuff (ATBS) - Web-Scrap is a new repo for me to learn and practice on GitHub familiarization and Python web scraping from ATBS by Al Swegart.

This repo covers 3 python module example from ATBS - Requests & BeautifulSoup4


Requests
 - A third party module for downloading web pages and files
 - requests.get() returns a Response object.
 - raise_for_status() Response method will raise an exception if downloads failed.
 - you can save a downloaded file to your hard drive with calls to iter_content() method
 - more info on https://requests.readthedocs.org

Beautiful Soup 4 (bs4)
- HTML can be parsed with BeautifulSoup Module
- Pass the string with the HTML to the bs4.BeautifulSoup() function to get a Soup object
- The Soup object has a select() method that can be passed a string of the CSS selector for HTML tag
- Get CSS selector string from browser's developer tools by right clicking the element and copy CSS path
- select() method will return a list of matching Element object
*hint* any changes in the web or the css block might render this code useless until you redo the code to scrap from the new css env

Beautiful Soup will be covered over 2 examples, 

Example one shows how I take an url and with requests module and selecting the css block using bs4, then print out the price it scrap from the targeted url.

Example two shows the same concept, the only difference is I scrap multipage pages in a go, on the beginning of example2, I make a library to store the details.

From there, I created 3 functions,
- Scrap the price from the targeted url
- Scrap the title from the targeted url
- Retrieve both data from the functions above and print it out in a string

This automation will shorten your time for you to get similar data over multiple site, for example if you are constantly retrieving price list or inventory update from tens or hundreds of pages.


