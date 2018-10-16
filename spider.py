import json
import requests

baseUrl = 'https://api.sou-yun.com/api/Biography?'

def Main():
    with open('./data.json', 'r', encoding='utf-8') as f:
        datas = json.loads(f.read())['Traces']
        for data in datas:
            if data.__contains__('RequestUri'):
                name = data['Title'].split(' <span')[0]
                request(name, data['RequestUri'])


def saveFile(fileName, content):
    f = open('./output/' + fileName + '.json', 'w')
    f.write(content)

def request(name, query):
    ret = requests.get(baseUrl + query)
    saveFile(name, ret.text)

        
Main()
