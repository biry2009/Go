# -*- coding:utf-8 -*-   
#获取并打印google首页的html  

import urllib2
from bs4 import BeautifulSoup

current_price = ""
promo_price = ""

headers = { 'Accept-Language':'en-US,en;q=0.5',
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

f = open("/Users/Bing/Desktop/wiki.txt", "r")
fp = open("/Users/Bing/Desktop/table.txt", "w")


for line in f:
    line=line.strip('\n')
    url = "https://www.godaddy.com/tlds/" + line[1:] + "-domain"
    alink = "<a href=\"" +str(url)+"\"" +"target=_blank >" + "Registe a" +line +"domain</a>"

    try:
    	req = urllib2.Request(url,None, headers)
        html = urllib2.urlopen(req).read()
        soup = BeautifulSoup(html,"lxml")


        if soup.find('span',{"class":"text-purchase"}) is not None:
        	current_price = soup.find('span',{"class":"text-purchase"}).string

        if soup.strike is not None:
        	promo_price = soup.strike.string
        else:
        	promo_price = current_price

        if promo_price is not None:
            fp.write("<tr><td>"+str(line)+"</td>"+"<td>"+promo_price.encode('utf-8')+"</td><td>"+current_price.encode('utf-8')+"</td><td>"+alink+"</td></tr>\n")



    except urllib2.URLError,e:
        pass
f.close()
fp.close()