from bs4 import BeautifulSoup
from urllib import request
def get_info(url):
    req = request.Request(url)
    req.add_header('User-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    with request.urlopen(req) as f:
        html = f.read()
        soup = BeautifulSoup(html,'html.parser')
        titleTag = soup.select('.todaymessbox h3 a')
        contentTag = soup.select('.todaymessbox span')
        print(titleTag)
        for item in titleTag:
            print(item.attrs['href'])
            print(item.string)

        for item in contentTag:
            print(item.string)


def get_sub_info(url):
    req = request.Request(url)
    req.add_header('User-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    with request.urlopen(req) as f:
        html = f.read()
        print(html)
        soup = BeautifulSoup(html, 'html.parser')
        titleTag = soup.select('.main_wrap_l h1')
        contentTag = soup.select('.TRS_Editor div span')
        for item in titleTag:
            print(item.string)
        for item in contentTag:
            print(item.string)

def get_toutiao(url):
    req = request.Request(url)
    req.add_header('User-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    with request.urlopen(req) as f:
        html = f.read()
        soup = BeautifulSoup(html, 'html.parser')
        titleTag = soup.select('ul.rlist li a')
        for item in titleTag:
            print(item.string)
            print(item.attrs['href'])

url = 'http://www.nmg.gov.cn/'
# url = 'http://www.nmg.gov.cn/fabu/xwdt/jrtt/201801/t20180124_658061.html'
url = 'http://www.nmg.gov.cn/fabu/xwdt/jrtt/'
get_toutiao(url)
# get_sub_info(url)
