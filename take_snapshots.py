# Takes a snapshot of all the cameras

import urllib
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

path = "/home/pi/webcam/"
base_url = 'http://www.wunderground.com'


base_url = 'http://www.wunderground.com'
url = 'http://www.wunderground.com/history/airport/KMDW/2014/11/17/MonthlyHistory.html?req_city=NA&req_state=NA&req_statename=NA'
response = requests.get(url)

soup = BeautifulSoup(response.content)
image_relative_url = soup.find('div', id='history-graph-image').img.get('src')
image_url = urljoin(base_url, image_relative_url)
print (image_url)

urllib.request.urlretrieve(image_url, path + "test3.jpg")

#urllib.request.urlretrieve("https://s0.2mdn.net/6192912/Ad_Dev1_728x90.jpg", path + "test2.jpg")
#urllib.request.urlretrieve("http://192.168.1.50/image/jpeg.cgi", path + "test1.jpg")

