import urllib.request
from pyquery import PyQuery as pq
from requests.exceptions import RequestException
from faker import Factory #它可以生成很多模拟的数据，如user-agent
import requests
import time
f = Factory.create()
headers = {'User-Agent': f.user_agent()}

def get_html(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # 解析乱码的解决情况
            response.encoding = response.apparent_encoding
            html = response.text
            doc = pq(html)  # 设置解析器为“lxml”
            return doc
        else:
            print('获取不到', url, response.status_code)
            return None
    except RequestException as e:
        print('获取不到', url, e)
        return None

def getFile(url):
    file_name = url.split('/')[-1]
    u = urllib.request.urlopen(url)
    f = open(file_name, 'wb')
    while True:
        buffer = u.read()
        if not buffer:
            break
        f.write(buffer)
    f.close()
    print ("Sucessful to download" + " " + file_name)


for i in range(678, 1000):
	url = 'http://wk.yingjiesheng.com/v-000-022-{}.html'.format(str(i))
	doc = get_html(url)
	try:
		href = doc('a').filter('.btn.btn-primary').attr('href')
		print(href)
		if href and '2019' in href:
			# print(href)
			getFile(href)
	except:
		pass
	time.sleep(3)