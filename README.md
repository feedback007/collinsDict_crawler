# collinsDict_crawler
# 抓取金山词典内的collins英英解释

## 运行环境 python=3.9  BeautifulSoup=4.12.2 
### 2023.11.5 V0.03 
1、通过有道js接口，下载英音和美音，存放在voice/en,am 目录下。
2、通过查重发现单词有重复93个。
3、下一步，整理日常常用单词和对话
### 2023.11.4 V0.02  
1、抓取600常用单词的解释并保存json
2、备注：这个网址是金山词霸，每天有限制
### 2023.11.3 V0.01  
测试固定单词，抓取json并保存

## 金山词典的优点：有例句，英英解释
### json结构解析如下，标签含义
symbols 发音和解释
ph_am 美式发音
ph_en 英式发音
ph_other 其他
cetFour
cetSix
collins
derivation
ee_mean
err_words
ee_mean 英英释义
exchanges 词态变化
new_sentence   实用场景例句
phrase 词组搭配
sameAnalysis 同义词辨析
synonym 同义词  
antonym 反义词
trade_means 行业词典
slang 常用俚语
真题例句
kaoyan 考研
identity_dic_new 
gaokao  高考
