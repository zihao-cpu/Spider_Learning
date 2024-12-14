import requests
import ddddocr
from lxml import etree

UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'



headers = {
    'User-Agent': UA
}
url = 'https://sh.58.com/ershoufang/p%d/?PGTID=0d30000c-0000-2835-00cc-80c06ddd3dce&ClickID=1'
pageNum = 1
fp = open('58.txt', 'w', encoding='utf-8')
for page in range(1, 10):
    pageUrl = format(url % pageNum)
    print(pageUrl)
    response = requests.get(pageUrl, headers=headers).text
    tree = etree.HTML(response)
    houses = tree.xpath('//section[@class="list"]/div')
    for house in houses:
        title=house.xpath('./a/div[2]//h3/text()')
        fp.write(title + '\n')

