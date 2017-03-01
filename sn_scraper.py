#!/usr/bin/env python
from datetime import datetime
from lxml import html
import requests

page = requests.get("http://www.snow-forecast.com/resorts/Mount-Baker/6day/mid")
tree = html.fromstring(page.content)

temp = tree.xpath('//div[@class="forecast-mid-header"]/ul/li/em/nobr')
updateTime = temp[0].text
updateDate = temp[1].text
updateAt = datetime.strptime("{} {}".format(updateDate, updateTime), "%d %b %Y %I %p")

print(updateAt)
