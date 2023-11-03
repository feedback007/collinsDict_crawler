import os
import sys
import  urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl
import json
import csv
import pandas as pd

CS_QUERY_URL_COLLIN = 'https://www.iciba.com/word?w='
#每天有限制

def queryCollins(word):
    fileName=r'dict\\'+word+'.json'
    #word=word.replace(' ', '%20').replace("'",'%27')
    word=urllib.parse.quote(word)
    ssl._create_default_https_context = ssl._create_unverified_context
    html =urlopen(CS_QUERY_URL_COLLIN + word)
    response = html.read().decode('utf-8')
    #print(response)
    bsObj = BeautifulSoup(response, 'html.parser')

    content = bsObj.find(id='__NEXT_DATA__')
    if content is None:
        return list()
    content.encode('gb2312')
    # print(content)
    v = False
    for part in content.children:
        item = re.sub(r'<.*?>', '', str(part))
        j= json.loads(item)
       # print(j)
        data = json.dumps(j,ensure_ascii=False)
        with open(fileName, mode='w', encoding='utf-8') as f:
            f.write(data)
        v = True
        #lst += list(filter(lambda x: len(x.strip()) != 0, item.split('\n')))
    return v

def load_CSV_data():
    filename='1000_words.csv'
    data = []
    # df = pd.read_csv(filename, encoding="utf-8")
    # data=df.tolist()
    # print(df)
    return  read_csv(filename)
def read_csv(file_name):
    data = []
    with open(file_name) as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            data.append(row[0])
       # print(data)
    return  data
def write_cvs(file_name,data):
    with open(file_name, 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

if __name__ == '__main__':
    #读取cvs文件
    data =load_CSV_data()
    iCnt=0
    for word in data:
        iCnt=iCnt+1
        print('{0},{1}'.format(iCnt,word))
        # if '?' in word:
        #     word= word[1:len(word)-1]
        #     print(word)
        wordJsonFile=r'dict/'+word+'.json'
        if not os.path.exists(wordJsonFile):
        #if word not in succeedData:
            try:
                queryCollins(word)
            except:
                pass
            finally:
                pass
    #     if iCnt%100==0:
    #         write_cvs(logDataName, succeedData)
    # write_cvs(logDataName,succeedData)

    # # if len(sys.argv) > 1:
    # word = 'can’t'  # ' '.join(sys.argv[1:])
    # ret = queryCollins(word)

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
