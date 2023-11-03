import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl
import json

CS_QUERY_URL_COLLIN = 'https://www.iciba.com/word?w='

def queryCollins(word):
    fileName=r'json\\'+word+'.json'
    word=word.replace(' ', '%20')
    ssl._create_default_https_context = ssl._create_unverified_context
    html = urlopen(CS_QUERY_URL_COLLIN + word)
    response = html.read().decode('utf-8')
    #print(response)
    bsObj = BeautifulSoup(response, 'html.parser')

    content = bsObj.find(id='__NEXT_DATA__')
    if content is None:
        return list()
    content.encode('gb2312')
    # print(content)
    lst = list()
    for part in content.children:
        item = re.sub(r'<.*?>', '', str(part))
        j= json.loads(item)
       # print(j)
        data = json.dumps(j,ensure_ascii=False)
        with open(fileName, mode='w', encoding='utf-8') as f:
            f.write(data)

        lst += list(filter(lambda x: len(x.strip()) != 0, item.split('\n')))
    return lst


if __name__ == '__main__':
    # if len(sys.argv) > 1:
    word = 'go'  # ' '.join(sys.argv[1:])
    ret = queryCollins(word)
    # if len(ret) == 0:
    #     print('\033[1;31m *** No result *** \033[0m')
    # for line in ret:
    #     if line.isdigit():
    #         print('\033[1;31m' + line + '\033[0m')
    #     else:
    #         print(line)
# else:
#     print('Usage: dict WORD/PHRASE')

# pip install -t C:\Users\Administrator\AppData\Local\Programs\Python\Python39\Lib\site-packages   beautifulsoup4
