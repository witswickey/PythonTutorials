import bs4
import os
import requests

totalpagesize = 2121


def startscrap():
    os.makedirs('D:/XKCD', exist_ok=True)
    for pagesize in range(totalpagesize, 1, -1):
        res = requests.get('https://xkcd.com/%s' % pagesize)
        res.raise_for_status()
        res.status_code = requests.codes.ok
        xkcddata = bs4.BeautifulSoup(res.text)
        elem = xkcddata.select('#comic img')
        # print(elem)
        if elem == []:
            print('Image not found')
        else:
            downloadurl = 'http:' + elem[0].get('src')
            print(('Downloading .. %s' % downloadurl))
            try:
                res = requests.get(downloadurl)
                res.raise_for_status()
                imageFile = open(os.path.join('D:/XKCD', os.path.basename(downloadurl)), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
            except:
                pass

    print('Done')


startscrap()
