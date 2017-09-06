#几节基础课的资源全部整合在一起
#作者：DYBOY
#时间：2017-09-05

import requests

from bs4 import BeautifulSoup
#引入模块资源

res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
for news in soup.select('.news-item'):
    if( len(news.select('h2')) >0 ):
        h2 = news.select('h2')[0].text
        time = news.select('.time')[0].text
        a = news.select('a')[0]['href']
        print(time,h2,a)


#print(res.text)

#html_sample ='<html><body><h1 id="title">Hello World!</h1><a href="#" class="link">This is link1</a><a href="#link2" class="link">This is link2</body></html>'

#soup = BeautifulSoup(html_sample,'html.parser')







#print(soup.text)

#使用select 找出含有 h1 标签的元素
#alink = soup.select('h1')
#print(alink)
#print(alink[0])
#print(alink[0].text)

#使用select 找出含有 a 标签的元素
#alink = soup.select('a')
#print(alink)

#使用select 找出id="title"的内容(id前面需要加上#)
#alink = soup.select('#title')
#print(alink)

#使用select 找出class="link"的内容(class前面需要加上.)
#alink = soup.select('.link')
#print(alink)
#print(alink[0].text)
#print(alink[1].text)
#for link in alink:
    #print(link.text)
#获取a标签的href属性
#for link in alink:
#    print(link['href'])


'''
html_sample2 = '<a href="#" id="testlink" title="link"> hello world!</a><a href="#2" id="testlink2" title="link2"> hello world2!</a>'
soup2 = BeautifulSoup(html_sample2,'html.parser')
print(soup2.select('a')[0]['id'])
print(soup2.select('a')[1]['id'])
'''

