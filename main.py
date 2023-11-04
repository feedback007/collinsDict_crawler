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
from collections import Counter

CS_QUERY_URL_COLLIN = 'https://www.iciba.com/word?w='
#每天有限制

def queryCollins(word):
    #word=word.replace(' ', '%20').replace("'",'%27')
    word=urllib.parse.quote(word)
    fileName=r'King_dict\\'+word+'.json'
    if os.path.exists(fileName):
        return  True
    print(word)
    ssl._create_default_https_context = ssl._create_unverified_context
    html =urlopen(CS_QUERY_URL_COLLIN + word)
    response = html.read().decode('utf-8')
    bsObj = BeautifulSoup(response, 'html.parser')

    content = bsObj.find(id='__NEXT_DATA__')
    v = False
    if content is None:
        return False
    content.encode('gb2312')
    # print(content)

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

def download_mp3(mp3_url,file_name):
    print(file_name)
    # 下载mp3文件
    urllib.request.urlretrieve(mp3_url, file_name)

    # # 保存mp3文件到指定路径
    # shutil.move('music.mp3', 'path/to/save/music.mp3')
def download_youdao_voice(word):
    word = urllib.parse.quote(word)
    #https://dict.youdao.com/dictvoice?audio=clam&type=1
    #https://dict.youdao.com/dictvoice?audio=clam&type=2
    en_url='https://dict.youdao.com/dictvoice?audio={0}&type=1'.format(word)
    en_file_name=r'voice/en/'+word+'.mp3'
    if not os.path.exists(en_file_name):
        download_mp3(en_url,en_file_name)
    am_url = 'https://dict.youdao.com/dictvoice?audio={0}&type=2'.format(word)
    am_file_name = r'voice/am/' + word + '.mp3'
    if not os.path.exists(am_file_name):
        download_mp3(am_url, am_file_name)


def write_cvs(file_name,data):
    with open(file_name, 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

if __name__ == '__main__':
    # download_youdao_voice('clam')
    # exit(0)
    #读取cvs文件
    data =load_CSV_data()

    # #查询重复 结果有93个重复，属于一词多义。只有902个单词语音。
    # duplicates = [item for item, count in Counter(data).items() if count > 1]
    # print(duplicates)
    # print(len(duplicates))

    iCnt=0
    for word in data:
        iCnt=iCnt+1
        # print('{0},{1}'.format(iCnt, word))
        download_youdao_voice(word)#下载语音
        queryCollins(word)#下载解释和例句



# pip install -t C:\Users\Administrator\AppData\Local\Programs\Python\Python39\Lib\site-packages   beautifulsoup4
