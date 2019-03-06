import os
import urllib.request
import re

from bs4 import BeautifulSoup


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return html

def get_ip(html,max,s,i):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('tr',attrs={'class':'odd'})
    f = open(r'C:\Users\傲\Desktop\iplist.txt', 'a')
    for each in links:
        if max>s:
            a = each.find_all('td')
            c = str(a[5])[4:-5]+'://'+str(a[1])[4:-5]+':'+str(a[2])[4:-5]
            try:
                response = urllib.request.urlopen('https://www.baidu.com/', timeout=2)
                f.write(c)
                f.write('\n')
                s+=1
                print(c)
            except:
                print('error')
                continue
        else:
            exit()
    f.close()
    get_ip(open_url(url+str(i+1)),max,s,i+1)


if __name__ == '__main__':
    max = int(input("请输入要获取的ip数量："))
    s=0
    url = 'http://www.xicidaili.com/nn/'
    if not os.path.exists(r'C:\Users\傲\Desktop\iplist.txt'):
        get_ip(open_url(url),max,s,i=1)
    else:
        os.remove(r'C:\Users\傲\Desktop\iplist.txt')


