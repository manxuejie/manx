import requests
url = []
f = open('res1.txt',encoding='utf8')
data = f.read()
response = requests.get(f)
HTML = response.text
lines = HTML.split('\n')
for line in lines:
    if 'url' in line:
        split_ = line.split('(')
        for i in split_:
            if 'http' in i or 'https' in i:
                url = i.split('"')[1]
                if 'com' in url:
                    URLS.append(url)
for url in URLS:
    response = requests.get(url)
    content = response.content
    with open(res.txt) as f:
        f.write(res.text)