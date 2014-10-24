# -*- coding:utf-8 -*-

import urllib2
import json
from city import city
cityname = raw_input("Which city do you like to search > ")
while cityname not in city :
    cityname = raw_input("Which city do you like to search > ")

citycode = city.get(cityname)
if citycode :
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
    content = urllib2.urlopen(url).read()
    data = json.loads(content) #将json格式转化为真正的字典
    result = data["weatherinfo"]
    str_temp = ("%s\n%s ~ %s") % (result["weather"], result["temp1"], result["temp2"])
    print str_temp

