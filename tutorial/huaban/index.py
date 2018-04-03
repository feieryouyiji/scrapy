import requests

download_dir = '/home/demlution/Pictures/huaban/'
url = 'http://img.hb.aicdn.com/af264a867d16063730dd49ad1de70e79d515776e28a8-CSC7iH_fw658'
r = requests.get(url)
content = r.content
filename = r.url.split('/')[-1][0:12] + '.jpg'
with open(download_dir + filename, 'wb') as f:
    f.write(content)