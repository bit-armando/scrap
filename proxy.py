import requests

proxy_dict = {'http': 'http://45.230.172.182:8080',
              'https': 'https://45.230.172.182:8080'}

print(requests.get('https://www.zenrows.com/blog/python-requests-proxy', proxies=proxy_dict).text)

