from docopt import docopt
import sys
import lxml
import requests
from bs4 import BeautifulSoup


def extracter(url, filePath):
    try:
        html = requests.get(url, timeout=3)
        html_soup = BeautifulSoup(html.text, 'lxml')
        links = html_soup.findAll('a')
        links.pop(0)
        try:
            fo = open(filePath, 'w')
            for link in links:
                temp_link = link.get('href')
                final_link = url+temp_link
                fo.write(final_link)
                fo.write('\n')
            fo.close()
            print(f'Operation Successful, Check {filePath} file for links.')
        except IOError:
            print('Can\'t create output file.')
            sys.exit()
    except requests.Timeout:
        print('Connection Timed out...Please check if you can access given URL.')
        sys.exit()
    except requests.ConnectionError:
        print('Please check your Internet connection')
        sys.exit()
