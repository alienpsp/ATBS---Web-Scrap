#ATBS---Web-Scrap

Automate The Boring Stuff (ATBS) - Web-Scrap is a new repo for me to learn and practice on GitHub familiarization and Python web scraping from ATBS by Al Swegart.

This repo covers 3 python module example from ATBS - Requests, BeautifulSoup4, Selenium

Requests
 - A third party module for downloading web pages and files
 - requests.get() returns a Response object.
 - raise_for_status() Response method will raise an exception if downloads failed.
 - you can save a downloaded file to your hard drive with calls to iter_content() method
 - more info on https://requests.readthedocs.org

Beautiful Soup 4
- HTML can be parsed with BeautifulSoup Module
- Pass the string with the HTML to the bs4.BeautifulSoup() function to get a Soup object
- The Soup object has a select() method that can be passed a string of the CSS selector for HTML tag
- Get CSS selector string from browser's developer tools by right clicking the element and copy CSS path
- select() method will return a list of matching Element object
*hint* any changes in the web or the css block might render this code useless until you redo the code to scrap from the new css env