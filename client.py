import json

import requests

count = 0

#response = requests.get('http://127.0.0.1:5000/announce/')
#print(response.status_code)
#print(response.text)

main_text = {'announce':[{
        'id': 1,
        'title': '1',
        'description': '`good house',
        "date_created": "1-12-1998",
        'owner': '1'
}
]
}

response = requests.post(f'http://127.0.0.1:8080/announce', json=main_text)
print(response.status_code)
print(response.text)

#response = requests.delete('http://127.0.0.1:5000/announce/1')
#print(response.status_code)
#print(response.text)