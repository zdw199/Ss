import requests
from bs4 import BeautifulSoup

#爬取美图录（https://www.meitulu.com）的图片，
# 开始网页为形如'https://www.meitulu.com/item/8703.html'的一套图的开始网页
start_url='https://www.meitulu.com/item/6861.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

#用于储存的函数
def save_pin(url):
    pin_res=requests.get(url,headers=headers)
    print('第'+str(name_num)+'张图片:'+str(pin_res.status_code))
    with open('{}.jpg'.format(name_num),'wb') as pin:
        pin.write(pin_res.content)

name_num=1 #命名图片的数字
key=1 #判断循环是否生继续的数字
url=start_url
while key:
    #工作部分
    res=requests.get(url,headers=headers)
    print(res.status_code)
    bs=BeautifulSoup(res.text,'html.parser')
    tag_min=bs.find('div',class_='content')
    list1=tag_min.find_all('img')
    for tag_pin in list1:
        url=tag_pin['src']
        save_pin(url)
        name_num+=1
    #判断部分
    tag_pages=bs.find('div',id='pages')
    nextpage=tag_pages.find_all('a',class_='a1')[1]['href']
    nowpage=tag_pages.find('span').text
    key=int(nextpage[-6])-int(nowpage)  #下一页的数字减去当前页，如果是最后一页那么结果为零，跳出循环
    url='https://www.meitulu.com'+nextpage
