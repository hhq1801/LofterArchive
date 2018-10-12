import requests
from bs4 import BeautifulSoup

numb = int(input())
id=[]
for i in range(numb):
    id.append(input())
out = ['\\', '/', ':', '*', '?', '#', '\”', '<', '>', '|', '\n']
#保存文件的时候文件名中不能有\/:*?#"<>|这些符号
for k in range(len(id)):
    a = requests.get('http://a.lofter.com/post/' + id[k])
    soup = BeautifulSoup(a.content.decode('utf-8'), 'lxml')
    title = soup.find('title')
    for text in title:
        print(text)
        for symbol in out:
            if symbol in text:
                text = text.replace(symbol, '_')
        try:
            f = open('D:\{}.html'.format(text + '_' + str(id[k])), 'w', encoding='utf-8')
        except:
            f = open('D:\{}.html'.format(str(k)), 'w', encoding='utf-8')
    for text in soup:
        p = str(text)
        f.write(p + '\t')
