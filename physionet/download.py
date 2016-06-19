import os
import urllib2
import requests
from bs4 import BeautifulSoup as BSoup

extensions = ['atr', 'dat', 'hea']
# the_path = 'https://www.physionet.org/physiobank/database/ltstdb/'
# the_path = 'https://www.physionet.org/physiobank/database/aami-ec13/'
# the_path = 'https://www.physionet.org/physiobank/database/incartdb/'
# the_path = 'https://www.physionet.org/physiobank/database/nstdb/'
the_path = 'https://www.physionet.org/physiobank/database/mitdb/'

# Save to tmp/ directory
savedir = 'tmp'
if not os.path.exists(savedir):
    os.makedirs(savedir)

# With this format
savename = savedir + '/{}.{}'

# Find all interesting files on that site:
soup = BSoup(urllib2.urlopen(the_path).read())

# Find all links pointing to .dat files
hrefs = []
for a in soup.find_all('a', href=True):
    href = a['href']
    # Download datafiles with markers given
    if href[-4::] == '.dat':
        hrefs.append(href[:-4])

print 'found {} data sets'.format(len(hrefs))

# Path to the file on the internet
down_path = the_path + '{}.{}'

for data_id in hrefs:
    print 'going for:', data_id
    for ext in extensions:
        webpath = down_path.format(data_id, ext)
        datafile = urllib2.urlopen(webpath)

        # Save locally
        filepath = savename.format(data_id, ext)
        with open(filepath, 'wb') as out:
            out.write(datafile.read())

        print webpath, 'saved to', filepath
