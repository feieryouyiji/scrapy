import requests

download_dir = '/home/demlution/Pictures/huaban/'
url = 'http://pic24.nipic.com/20120924/11023088_123250360000_2.jpg'
r = requests.get(url)
content = r.content
filename = r.url.split('/')[-1][0:12] + '.jpg'
with open(download_dir + filename, 'wb') as f:
    f.write(content)