import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re

url = 'https://sec.report/Document/0001193125-21-072571'

urls = ['https://sec.report/Document/0001193125-21-072571', 'https://sec.report/Document/0001193125-21-031547/',
        'https://sec.report/Document/0001104659-21-037813/', 'https://sec.report/Document/0001193125-21-024746/',
        'https://sec.report/Document/0001193125-21-056708/']
fnames = ['text1.html', 'text2.html', 'text3.html', 'text4.html', 'text5.html']

for i in range(len(urls)):
    req = urllib.request.Request(urls[i], headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(req).read()

    f = open(fnames[i], 'wb')
    f.write(webpage)
    f.close()
for i in range(5):
        with open("https://github.com/rastalord/test_task/edit/main/" + fnames[i]) as fp:
            soup = BeautifulSoup(fp, 'html.parser')

        answ = []
        #num = re.findall(r'(?:\d+\.)?\d+,\d+', str(td))
        data = soup.find_all('td')
        for td in data:
            num = re.findall(r'\d+,\d+,\d+', str(td))
            answ.append(num)
            num = re.findall(r'\d+\.+\d+', str(td))
            answ.append(num)
            num = re.findall(r'\d+-\d+', str(td))
            answ.append(num)
        answ = list(filter(None, answ))
        print(answ)

