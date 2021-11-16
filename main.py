#MAIN PROGRAM

import pprint
import requests
from bs4 import BeautifulSoup

###################
#1. 미드 대본을 수집#
###################

url = 'https://fangj.github.io/friends/season/0101.html'
result = requests.get(url)
doc = BeautifulSoup(result.text,'html.parser')

sentence_list = doc.select('p> font')

for i,sentence in enumerate(sentence_list):
    print('==========================================================')
    sentence_txt = sentence.get_text().strip()
    start_inx = sentence_txt.find(':')
    clean_sentence = sentence_txt[start_inx+2:]
    pprint.pprint('1 > {}'.format(clean_sentence))



#####################
#2. 단어만 추출(전처리)#
#####################

#############################
#3. 빈도수 순으로 나열 및 시각화#
#############################

###################################
#4. 다음 영어사전 단어정보 수집 및 매칭#
###################################

##############
#5. Excel 저장#
##############

#####################
#6. 시각화(WordCloud)#
#####################