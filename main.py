# MAIN PROGRAM

import pprint
import requests
from bs4 import BeautifulSoup
import nltk

# nltk.download('punkt')
# nltk.download('stopwords')

####################
# 1.미드 대본 수집 #
####################
url = 'https://fangj.github.io/friends/season/0101.html'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

sentence_list = doc.select('p > font')

words = []  # 영단어장
for i, sentence in enumerate(sentence_list):
    print('=====================================================================================')
    sentence_txt = sentence.get_text().strip()
    start_idx = sentence_txt.find(':')
    clean_sentence = sentence_txt[start_idx+2:]
    pprint.pprint('1 > {}'.format(clean_sentence))

    #########################
    # 2.단어만 추출(전처리) #
    #########################
    # conda install -c anaconda nltk
    # 자연어 처리 => NLTK
    # 2-1.토큰화(Tokenization)
    token_list = nltk.word_tokenize(clean_sentence)
    print('2 >> {}'.format(token_list))

    # 2-2.불용어(StopWord) 제거
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.append('..')
    stopwords.append('...')
    stopwords.append('.....')
    stopwords.append('``')

    clean_list = []
    for token in token_list:
        if token.lower() not in stopwords:
            clean_list.append(token)
    print('3 >>> {}'.format(clean_list))

    # 2-3. Length 1 이하인 token 제거
    # lambda식을 활용한 Code
    len_filter_list = list(filter(lambda x: len(x) > 1, clean_list))
    print('4 >>>> {}'.format(len_filter_list))

    # 2-4.(')포함 된 Token 제거
    clean_filter_list = list(filter(lambda x: "'" not in x, len_filter_list))
    print('5 >>>>> {}'.format(clean_filter_list))

    # 2-5. ('-')포함 된 Token 제거
    clean_list = list(filter(lambda x : "-"not in x, len_filter_list))
    print('6 >>>>>> {}'.format(clean_list))
    words.extend(clean_list)

    print(words)
















##################################
# 3.빈도수 순으로 나열 및 시각화 #
##################################

#########################################
# 4.다음 영어사전 단어정보 수집 및 매칭 #
#########################################

##################
# 5.Excel 저장 #
##################

#######################
# 6.시각화(WordCloud) #
#######################
