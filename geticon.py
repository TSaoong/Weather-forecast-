import os
import requests
from bs4 import BeautifulSoup
import re

def get_HTMLtext(URL):
    '''获取一个网页'''
    res = requests.get(URL)
    try:
        res.raise_for_status()
        res.encoding = "utf8"
        return res.text
    except:
        print("错误")

def deal_with_HTML(response):
    """获取图片地址，天气类型"""
    list_1 = []
    list_3 = []
    dict = {}
    soup = BeautifulSoup(response,"html.parser")
    #print(str(soup.find_all("a"))+"\n")
    for i in soup.find_all("img"):
        #print((re.findall(r"www.weather.com.cn/m/i/icon_weather.*.gif",i.attrs["src"])))
        list_1.append((re.findall(r"www.weather.com.cn/m/i/icon_weather.*.gif",i.attrs["src"])))
    list_2 = list(filter(None,list_1))
    for j in soup.find_all("p"):
        #print(j.string)
        if j.string == "\xa0":
            continue
        else:
            list_3.append(j.string)
        list_4 = list(filter(None,list_3))
    #print(list_4)
    for n in range(len(list_4)):
        dict["".join((list_2[n]))] = list_4[n]
    #print(dict)
    return dict

def save_pictrue(url,name):
    """保存图片"""
    root = "E:\\016-python\\requests\\"
    path = root +name +"-"+"".join(url).split("/")[-1]
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):    
        kv = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get("http://" +url, headers = kv)
        r.raise_for_status()
        with open (path,"wb") as f: 
            f.write(r.content)
            f.close()
            print("保存成功")
    else:
        print("文件已经存在")

URL = "http://www.weather.com.cn/static/html/legend.shtml"   
response = get_HTMLtext(URL)
data = deal_with_HTML(response)
for key,valcue in data.items():
    url = ("".join(key))
    name = valcue
    #print(name)
    #print(url)
    #save_pictrue(url,)
    save_pictrue(url,name)