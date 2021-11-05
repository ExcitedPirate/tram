import requests

print('Beginning MITRE ATTACK Update...')

url = 'https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json'
r = requests.get(url)

with open('data/attack/enterprise-attack.json', 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
