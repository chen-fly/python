#coding = utf-8
import urllib
import re

#f = urllib.urlopen("http://www.douyu.com")
f = urllib.urlopen("https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C3%C0%C5%AE&fr=ala&ala=1&alatpl=cover&pos=0&hs=2&xthttps=111111")
htmlCode = f.read()

#imageList = re.findall('src="(.*?\.(jpg|png))"', htmlCode)
imageList = re.findall('"thumbURL":"(.*?\.(jpg|png))"', htmlCode)

t = open("123.txt", 'w')
#t.write(htmlCode)
#t.close()

i = 1

#print(len(imageList))

for a in imageList:
    imgUrl = a[0]
    img = a[1]
    
    t.write(imgUrl + '\n')
    #print(imgUrl)
    urllib.urlretrieve(imgUrl, '%d.jpg'%i)
    i += 1
    
t.close()