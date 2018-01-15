#! python3

import requests
rs = requests.get('http://automatetheboringstuff.com/files/rj.txt')


# to check if link is ok in shell, only raise exception on error
rs.raise_for_status() 


#this print the length of the downloaded link as a string.
print('The article is ' + str(len(rs.text)) + ' words long.') 

#this print out the text itself, from 0 till the 500 character.
#print(rss.text[:500]) 

#To write it to a file, you can use a for loop with the iter_content() method.
#You can specify how many byte of "chunk" is written into it, 100000 is generally a good size.
pyFile = open('RJ.txt', 'wb') #wb means write binary
for chunk in rs.iter_content(100000):
	pyFile.write(chunk)

pyFile.close()


'''
The for loop and iter_content() stuff may seem complicated compared to the open()/write()/close() workflow you’ve been using to write text files, 
but it’s to ensure that the requests module doesn’t eat up too much memory even if you download massive files. 
You can learn about the requests module’s other features from http://requests.readthedocs.org/.
'''