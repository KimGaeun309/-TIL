# 컴퓨터전자시스템공학부 202000376 김가은

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


result = []

for sido1 in range(1, 17+1):
    for sido2 in range(1, 1000):
        try:       
            Kyochon_url = f"https://www.kyochon.com/shop/domestic.asp?sido1={sido1}&sido2={sido2}&txtsearch="
            html = urllib.request.urlopen(Kyochon_url)
            soupKyochon = BeautifulSoup(html, 'html.parser')
            shopList = soupKyochon.select("div.shopSchList > ul.list > li > a > span")

            for i in range(len(shopList)):
                store = shopList[i].strong.string
                shoptext = shopList[i].em.text.strip()
                addrList = shoptext[:shoptext.index('(')].strip().split(' ')
                sido = addrList[0]
                gungu = addrList[1]
                store_address = ' '.join(s for s in addrList)
                result.append([store]+[sido]+[gungu]+[store_address])
            
        except:
            break
        

kyochon_tbl = pd.DataFrame(result, columns = ('store', 'sido', 'gungu', 'store_address'))
kyochon_tbl.to_csv("kyochon.csv", encoding="cp949", mode="w", index=True)
