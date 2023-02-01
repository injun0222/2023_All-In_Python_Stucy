import pandas as pd
import numpy as np 
#================================
# 황인준

#<예제 1-2> 시리즈 인덱스 : 시리즈의 생성, 시리즈의 index와 values

list_data = ['2019-01-02', 3.14, 'ABC', 100, True] 
#list_data 리스트 정의 및 원소 대입
sr = pd.Series{list_data}
# sr변수에 pandas의 시리즈 변환 함수 객체.Series{} 사용
# 이 코드에서는 Series{리스트}형태로, 리스트를 시리즈로 변환
# 별도의 인덱스 지정은 없었음
print(sr)
"""
0   2019-01-02
1   3.14
2   ABC
3   100
4   True
dtype: object
"""
idx = sr.index
# 시리즈객체.index를 이용하여 시리즈의 인덱스 값 배열에 접근, 시리즈의 인덱스를 변수idx에 할당
val = sr.values
# 시리즈객체.index를 이용하여 시리즈의 데이터 값 배열에 접근, 시리즈의 데이터를 변수val에 할당
print(idx)
#RangeIndex(start=0,stop=5,step=1)
print('\n')
print(val)
#['2019-01-02', 3.14, 'ABC', 100, True]
#================================
#<예제 1-7> 행삭제 : 데이터프레임의 생성, 데이터프레임의 삭제함수 drop
# exam_data 딕셔너리 생성, DataFrame() 함수로 exam_data를 데이터프레임 변환, 변수 df에 저장 
exam_data = {'수학' : [ 90, 80, 70] 영어 : [ 98, 89, 95], 
음악 : [ 85, 95, 100], '체육' : [ 100, 90,90]} 

df = pd.DataFrame (exam_data, index=['서준', '우현', '인아']} 
#데이터프레임 생성 후, df.index=['서준', '우현', '인아'] 하면?                   
print (df) 
print('\n')
"""
df데이터프레임의 구조

    수학 영어 음악 체육
서준  90  98   85  100
우현  80  89   95   90
인아  70  95  100   90

"""

# 데이터프레임 df를 복제하여 변수 df2에 저장. df2의 1개 행(row) 삭제 
df2 = df[:] 
df2.drop('우현', inplace=True) 
#df2.drop('우현', axis=0, inplace=True)와 같은결과다. 행을 삭제하기때문에, axis=0이 생략되었다.
#열을 삭제할 떄에는 axis=1을 넣어준다. inplace=True를 입력하여 drop함수로 반환된 새로운 데이터프레임을 기존 변수인 df2에 넣어준다.                   
print (df2) 
print('\n') 
"""
    수학 영어 음악 체육
서준  90  98   85  100
인아  70  95  100   90

"""
                   
# 데이터프레임 df를 복제하여 변수 df3에 저장. df3의 2개 행(row) 삭제 
dfs = df[:] 
df3.drop(['우현', '인아'], axis=0, inplace=True) 
print(df3) 
"""
    수학 영어 음악 체육
서준  90  98   85  100

"""

#================================
#<예제 1-16> 특정 열을 행 인덱스로 설정 : 데이터프레임의 생성, 인덱스 설정 함수 set_index()
# DataFrame() 함수로 데이터프레임 변환 변수 df에 저장 
exam data {'이름' : [ '서준', '우현', '인아'], #딕셔너리 exam_data 생성
           '수학' : [90, 80, 70], 
           '영어' : [98, 89, 95], 
           '음악' : [ 85, 95, 100],
           '체육' : [100, 90, 90]} 

df = pd.DataFrame (exam_data) #생성한 딕셔너리를 데이터프레임으로 변환 후 df에 할당
"""
df데이터프레임의 구조

  이름 수학 영어 음악 체육
0 서준  90  98   85  100
1 우현  80  89   95   90
2 인아  70  95  100   90

"""                   
print (df) 
print('\n') 


# 특정 열 (column)을 데이터프레임의 행 인덱스 (index)로 설정 
# 객체.set_index로 반환되는 데이터프레임은 새로운 데이터프레임이다. 원래 변수값에 다시 할당하여 변환하거나,
# inplace=True를 사용해야 원래 변수를 수정 가능                
ndf = df.set_index (['이름']}  # 행 인덱스를 변경 후 ndf변수에 할당
print (ndf) 
"""
ndf 데이터프레임의 구조 : 기존 데이터프레임에서 행index를 '이름' 열으로 변경

    수학 영어 음악 체육
이름   
서준  90  98   85  100
우현  80  89   95   90
인아  70  95  100   90

->> 열은 [이름,수학,영어,음악,체육]에서 [수학,영어,음악,체육]이 된다.
"""                        
print('\n') 
ndf2 = ndf.set_index ('음악') 
print (ndf2) 
"""
ndf2 데이터프레임의 구조 : ndf 데이터프레임에서 행index를 '음악' 열으로 변경

    수학 영어 체육
음악
85   90   98  100
95   80   89   90
100  70   95   90

->> 열은 [수학,영어,음악,체육]에서 [수학,영어,체육]이 된다.
"""         
print('\n') 
ndf3 = ndf.set_index (['수학', '음악']) 
print (ndf3) 
"""
ndf3 데이터프레임의 구조 : ndf2 데이터프레임에서 행index에 '수학' 열을 추가 -> 멀티인덱스

          영어 체육
음악 수학
85   90    98  100
95   80    89   90
100  70    95   90

->> 열은 [수학,영어,체육]에서 [영어,체육]이 된다.
"""        

#================================
#<예제 1-24> 연산 메소드 사용 - 시리즈 연산 : 시리즈의 생성, 연산 메소드, fill_value 옵션으로 NaN값 제거

# 딕셔너리 데이터로 판다스 시리즈 만들기 
student1 - pd.Series({'국어' : np.nan, '영어' : 80, '수학' : 90}) #student1 시리즈 : 국어:Nan, 영어:80, 수학:90
student2 = pd.Series ({'수학' : 80, '국어' : 90})                 #student2 시리즈 : 국어:90, 영어:NaN, 수학:80

print (student1) 
print('\n') 
"""
student1
국어      Nan
영어      80.0
수학      90.0
dtype: float64
"""
print (student2) 
print('\n') 
"""
student2
수학      80
국어      90
dtype: int64
"""
                    
# 두 학생의 과목별 점수로 사칙연산 수행 (연산 메소드 사용) 
# fill_value = 0 옵션을 사용하여, NaN 값을 0으로 바꾼 후 계산한다.
sr_add = student1.add(student2, fill_value=0)  # 덧셈
sr_sub = student1.sub(student2, fill_value=0)  # 뺄셈
sr_mul = student1.mul(student2, fill_value=0)  # 곱셈
sr_div = student1.div(student2, fill value=0)  # 나눗셈 


# 사칙연산 결과를 데이터프레임으로 합치기 (시리즈 - 데이터프레임) 
result = pd.DataFrame ([sr_add, sr_sub, sr_mul, sr_div],  
                        index= ['덧셈', '벨셈, 곱셈', '나눗셈']) 
print (result)
"""
          국어       수학         영어
덧셈      90.0    170.000   80.000000
뺄셈     -90.0     10.000   80.000000
곱셈       0.0   7200.000    0.000000
나눗셈     0.0      1.125         inf

"""

#================================
#예제 1
#라이브러리 불러오기
from bs4 import BeautifulSoup #크롤링 라이브러리
import requests #html소스 가져오는 패키지 라이브러리, 원하는 UPL 정보
import re #정규표현식으로 가져오는 라이브러리
import pandas as pd
# 위키피디아 미국 ETF 웹 페이지에서 필요한 정보를 스크래핑하여 딕셔너리 형태로 변수 etfs에 저장
url = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
resp= requests.get(url) #url 추출
soup = BeautifulSoup(resp.text, 'lxml') 
"""
resp에 가져온 
#HTML 문서를 lxml 파서를 통해서 BeautifulSoup 객체로 만들어 준 것이다.
따라서 soup은 해당 url의 모든 HTML 정보를 가지고 있게 된다.
"""
rows = soup.select('div > ul > li') #상위태그이름>자식태그>자식태그

etfs = {}
for row in rows:

  try:
    etf_name = re.findall('^(.*) \(NYSE', row.text) #패턴 문자열 찾기. (찾을꺼,찾는곳)
    etf_market = re.findall('\((.*)\|', row.text)
    etf_ticker = re.findall ('NYSE Arca\|(.*)\)', row.text)

    if (len(etf_ticker) > 0) & (len(etf_market) > 0):
        etfs [etf_ticker[0]] = [etf_market[0], etf_name[0]]
  except AttributeError as err:
    pass

# etfs 딕셔너리 출력
print(etfs)
print('\n')

# etfs 딕셔너리를 데이터프레임으로 변환
df = pd.DataFrame(etfs)
print(df)

#================================           
#=============================================================================================
# 이준형
                    
                    <예제 1-1> 딕셔너리 > 시리즈 변환

#pandas 불러오기
import pandas as pd

#key:value 쌍으로 딕셔너리를 만들고, 변수 dict_data에 저장
dict_data = {'a':1, 'b': 2, 'c': 3}               //dictionary

#판다스 Series() 함수로 dictionary를 Series로 변환, 변수 sr에 저장
sr = pd.Series(dict_data)

#sr의 자료형 출력
print(type(sr))
print('\n')
#변수 sr에 저장되어 있는 시리즈 객체를 출력
print(sr)
-------------------------
a    1
b    2
c    3                       //series
dtype: int64
----------------------

<예제1-2> 시리즈 인덱스

#pandas 불러오기
import pandas as pd

#리스트를 시리즈로 변환하여 변수 sr에 저장
list_data = ['2019-01-02', 3.14, 'abc', 100, True]
sr = pd.Series(list_data)
print(sr)

idx = sr.index
val = sr.values
print(idx)
print('\n')
print(val)

---------------------
0    2019-01-02
1          3.14
2           abc
3           100
4          True
dtype: object
RangeIndex(start=0, stop=5, step=1)


['2019-01-02' 3.14 'abc' 100 True]
----------------------

<예제 1-3> 시리즈 원소 선택

#pandas 불러오기
import pandas as pd

#투플(tuple)을 시리즈로 변환(인덱스 옵션 지정)
tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr)

#원소를 한개 선택
print(sr[0]) #sr의 1번째 원소를 선택(정수형 위치 인덱스)
print(sr['이름']) #'이름' 라벨을 가진 원소를 선택(인덱스 이름)

#여러개의 원소를 선택
print(sr[[1,2]])
print('\n')
print(sr[['생년월일', '성별']])

#여러개의 원소를 선택(인덱스 범위 지정)
print(sr[1:3])
print('\n')
print(sr['생년월일': '학생여부'])
--------------------------------------------
이름              영인
생년월일    2010-05-01
성별               여
학생여부          True
dtype: object
영인
영인
생년월일    2010-05-01
성별               여
dtype: object


생년월일    2010-05-01
성별               여
dtype: object
생년월일    2010-05-01
성별               여
dtype: object


생년월일    2010-05-01
성별               여
학생여부          True
dtype: object
-------------------------------

<예제 1-4> 딕셔너리 > 데이터프레임 변환

#pandas 불러오기
import pandas as pd

#열이름을 key로 하고, 리스트를 value로 갖는 딕셔너리 정의(2차원 배열)
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

#pandas DataFrame() 함수로 딕셔너리를 데이터프레임으로 변환. 변수 df에 저장
df = pd.DataFrame(dict_data)

#df의 자료형 출력
print(type(df))
print('\n')
#변수 df에 저장되어 있는 데이터프레임 객체를 출력
print(df)
----------------------------
<class 'pandas.core.frame.DataFrame'>


   c0  c1  c2  c3  c4
0   1   4   7  10  13
1   2   5   8  11  14
2   3   6   9  12  15
----------------------------

<예제 1-5> 행 인덱스/ 열 이름 설정

#pandas 불러오기
import pandas as pd

#행 인덱스/ 열 이름 지정하여 데이터 프레임 만들기
df = pd.DataFrame([[15,'남','덕영중'], [17, '여', '수리중']], index=['준서', '예은'], columns=['나이', '성별', '학교'])

#행 인덱스, 열 이름 확인하기
print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)

#행 인덱스, 열 이름 변경하기
df.index=['학생1', '학생2']
df.columns=['연령', '남녀', '소속']

print(df) # 데이터 프레임
print('\n')
print(df.index) #행 인덱스
print('\n')
print(df.columns) #열 이름
----------------------------------
 나이 성별   학교
준서  15  남  덕영중
예은  17  여  수리중


Index(['준서', '예은'], dtype='object')


Index(['나이', '성별', '학교'], dtype='object')
     연령 남녀   소속
학생1  15  남  덕영중
학생2  17  여  수리중


Index(['학생1', '학생2'], dtype='object')


Index(['연령', '남녀', '소속'], dtype='object')
-------------------------------------------------------

<예제 1-6> 행 인덱스/ 열 이름 변경

#pandas 불러오기
import pandas as pd

#행 인덱스/ 열 이름 지정하여 데이터 프레임 만들기
df = pd.DataFrame([[15,'남','덕영중'], [17, '여', '수리중']], index=['준서', '예은'], columns=['나이', '성별', '학교'])

#데이터 프레임 df출력
print(df)
print('\n')

#열 이름 중, '나이'를 연령으로, '성별'을 '남녀'로, '학교'를 '소속'으로 바꾸기
df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace = True)

#df의 행 인덱스 중에서, '준서'를 '학생1'로, '예은'을 '학생2'로 바꾸기
df.rename(index={'준서':'학생1', '예은':'학생2'}, inplace=True)
print(df)
--------------------
 나이 성별   학교
준서  15  남  덕영중
예은  17  여  수리중


     연령 남녀   소속
학생1  15  남  덕영중
학생2  17  여  수리중
-------------------------------

<예제 1-7> 행 삭제

#pandas 불러오기
import pandas as pd

#DataFrame() 함수로 데이터 프레임 변환, 변수 df에 저장
exam_data = {'수학' : [90,80,70], '영어' : [98,89,95],
             '음악' : [85,95,100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

#dataframe df를 복제하여 변수 df2에 저장. df2의 1개 행(row) 삭제
df2 = df[:]
df2.drop('우현', inplace=True)
print(df2)
print('\n')

#dataframe df를 복제하여 변수 df3에 저장. df3의 2개 행(row) 삭제
df3 = df[:]
df3.drop(['우현', '인아'], axis=0, inplace=True)
print(df3)
print('\n')
-------------------
수학  영어   음악   체육
서준  90  98   85  100
우현  80  89   95   90
인아  70  95  100   90


    수학  영어   음악   체육
서준  90  98   85  100
인아  70  95  100   90


    수학  영어  음악   체육
서준  90  98  85  100
-----------------------------

<예제 1-8> 열 삭제

#pandas 불러오기
import pandas as pd

#DataFrame() 함수로 데이터 프레임 변환, 변수 df에 저장
exam_data = {'수학' : [90,80,70], '영어' : [98,89,95],
             '음악' : [85,95,100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

#dataframe df를 복제하여 변수 df4에 저장. df4의 1개 열(column) 삭제
df4 = df[:]
df4.drop('수학', axis=1, inplace=True)
print(df4)
print('\n')

#dataframe df를 복제하여 변수 df5에 저장. df5의 2개 열(column) 삭제
df5 = df[:]
df5.drop(['영어', '음악'], axis=1, inplace=True)
print(df5)
print('\n')
--------------
수학  영어   음악   체육
서준  90  98   85  100
우현  80  89   95   90
인아  70  95  100   90


    영어   음악   체육
서준  98   85  100
우현  89   95   90
인아  95  100   90


    수학   체육
서준  90  100
우현  80   90
인아  70   90
---------------------

<예제 1-9> 행 선택

#pandas 불러오기
import pandas as pd

#DataFrame() 함수로 데이터 프레임 변환, 변수 df에 저장
exam_data = {'수학' : [90,80,70], '영어' : [98,89,95],
             '음악' : [85,95,100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

#행 인덱스를 사용하여 행 1개 선택
label1 = df.loc['서준']
position1 = df.iloc[0]
print(label1)
print('\n')
print(position1)

#행 인덱스를 사용하여 2개 이상의 행 선택
label2 = df.loc[['서준', '우현']]
position2 = df.iloc[[0,1]]
print(label2)
print('\n')
print(position2)

#행 인덱스 범위를 지정하여 행 선택
label3 = df.loc['서준' : '우현']
position3 = df.iloc[0:1]
print(label3)
print('\n')
print(position3)
----------------------

수학  영어   음악   체육
서준  90  98   85  100
우현  80  89   95   90
인아  70  95  100   90


수학     90
영어     98
음악     85
체육    100
Name: 서준, dtype: int64


수학     90
영어     98
음악     85
체육    100
Name: 서준, dtype: int64
    수학  영어  음악   체육
서준  90  98  85  100
우현  80  89  95   90


    수학  영어  음악   체육
서준  90  98  85  100
우현  80  89  95   90
    수학  영어  음악   체육
서준  90  98  85  100
우현  80  89  95   90


    수학  영어  음악   체육
서준  90  98  85  100
------------------------------------

<예제 1-10> 열 선택

#pandas 불러오기
import pandas as pd

#DataFrame() 함수로 데이터 프레임 변환, 변수 df에 저장
exam_data = {'수학' : [90,80,70], '영어' : [98,89,95],
             '음악' : [85,95,100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data)
print(type(df))
print('\n')

#수학 점수 데이터만 선택. 변수 math1에 저장
math1 = df['수학']
print(math1)
print(type(math1))
print('\n')

#영어 점수 데이터만 선택, 변수 english에 저장
english = df.영어
print(english)
print(type(english))

#음악, 체육 점수 데이터를 선택, 변수에 저장
music_gym = df[['음악', '체육']]
print(music_gym)
print(type(music_gym))
print('\n')

#수학 점수 데이터만 선택, 변수에 저장
math2 = df[['수학']]
print(math2)
print(type(math2))
-----------------------------------------------
<class 'pandas.core.frame.DataFrame'>


0    90
1    80
2    70
Name: 수학, dtype: int64
<class 'pandas.core.series.Series'>


0    98
1    89
2    95
Name: 영어, dtype: int64
<class 'pandas.core.series.Series'>
    음악   체육
0   85  100
1   95   90
2  100   90
<class 'pandas.core.frame.DataFrame'>


   수학
0  90
1  80
2  70
<class 'pandas.core.frame.DataFrame'>
---------------------------------------------

<예제 1-11> 

#pandas 불러오기
import pandas as pd

#DataFrame() 함수로 데이터 프레임 변환, 변수 df에 저장
exam_data = {'이름' : ['서준', '우현', '인아'], '수학' : [90,80,70], '영어' : [98,89,95],
             '음악' : [85,95,100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data)

#이름 열을 새로운 인덱스로 지정하고, df객체에 변경 사항 반영
df.set_index('이름', inplace = True)
print(df)

#데이터 프레임 df의 특정 원소 1개 선택('서준'의 음악 점수)
a = df.loc['서준', '음악']
print(a)
b = df.iloc[0,2]
print(b)

#데이터 프레임 df의 특정 원소 2개 이상 선택('서준'의 음악, 체육 점수)
c = df.loc['서준', ['음악', '체육']]
print(c)
d = df.iloc[0,[2,3]]
print(d)
e = df.loc['서준', '음악':'체육']
print(e)
f = df.iloc[0, 2:]

#df 2개이상의 행과 열에 속하는 원소들 선택('서준', '우현'의 음악, 체육 점수)
g = df.loc[['서준', '우현'], ['음악', '체육']]
print(g)
h = df.iloc[[0,1],[2,3]]
print(h)
i = df.loc['서준':'우현', '음악':'체육']
print(i)
j = df.iloc[0:2, 2:]
-------------------------
수학  영어   음악   체육
이름                  
서준  90  98   85  100
우현  80  89   95   90
인아  70  95  100   90
85
85
음악     85
체육    100
Name: 서준, dtype: int64
음악     85
체육    100
Name: 서준, dtype: int64
음악     85
체육    100
Name: 서준, dtype: int64
    음악   체육
이름         
서준  85  100
우현  95   90
    음악   체육
이름         
서준  85  100
우현  95   90
    음악   체육
이름         
서준  85  100
우현  95   90
------------------------

<예제 1-12> 열 추가

#pandas 불러오기
import pandas as pd

#DataFrame() 함수로 데이터 프레임 변환, 변수 df에 저장
exam_data = {'이름' : ['서준', '우현', '인아'], '수학' : [90,80,70], '영어' : [98,89,95],
             '음악' : [85,95,100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

#데이터프레임 df에 국어점수 열 추가. 데이터값은 80지정
df['국어'] = 80
print(df)
------------------
이름  수학  영어   음악   체육
0  서준  90  98   85  100
1  우현  80  89   95   90
2  인아  70  95  100   90


   이름  수학  영어   음악   체육  국어
0  서준  90  98   85  100  80
1  우현  80  89   95   90  80
2  인아  70  95  100   90  80
----------------------------------------------

<예제 1-13> 행 추가

#pandas 불러오기
import pandas as pd

#DataFrame() 함수로 데이터 프레임 변환, 변수 df에 저장
exam_data = {'이름' : ['서준', '우현', '인아'], '수학' : [90,80,70], '영어' : [98,89,95],
             '음악' : [85,95,100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

#새로운 행 추가 - 같은 원소 값 입력
df.loc[3] = 0
print(df)
print('\n')

#새로운 행 추가 - 원소 값 여러개의 배열 입력
df.loc[4] = ['동규', 90, 80,70,60]
print(df)
print('\n')

#새로운 행 추가 - 기존 행 복사
df.loc['행5'] = df.loc[3]
print(df)
------------------------------
이름  수학  영어   음악   체육
0  서준  90  98   85  100
1  우현  80  89   95   90
2  인아  70  95  100   90


   이름  수학  영어   음악   체육
0  서준  90  98   85  100
1  우현  80  89   95   90
2  인아  70  95  100   90
3   0   0   0    0    0


   이름  수학  영어   음악   체육
0  서준  90  98   85  100
1  우현  80  89   95   90
2  인아  70  95  100   90
3   0   0   0    0    0
4  동규  90  80   70   60


    이름  수학  영어   음악   체육
0   서준  90  98   85  100
1   우현  80  89   95   90
2   인아  70  95  100   90
3    0   0   0    0    0
4   동규  90  80   70   60
행5   0   0   0    0    0
-----------------------------------

<예제 1-14> 원소 값 변경

#pandas 불러오기
import pandas as pd

#DataFrame() 함수로 데이터 프레임 변환, 변수 df에 저장
exam_data = {'이름' : ['서준', '우현', '인아'], '수학' : [90,80,70], '영어' : [98,89,95],
             '음악' : [85,95,100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data)

#이름 열을 새로운 인덱스로 지정하고, df 객체에 변경사항 반영
df.set_index('이름', inplace = True)
print(df)
print('\n')

#데이터프레임 df의 특정 원소 변경. 서준의 체육 점수
df.iloc[0][3] = 80
print(df)
print('\n')

df.loc['서준']['체육'] = 90
print(df)
print('\n')

df.loc['서준', '체육'] = 100
print(df)

#원소 여러개 변경. 서준의 음악, 체육 점수
df.loc['서준', ['음악', '체육']] = 50
print(df)
print('\n')

df.loc['서준', ['음악', '체육']] = 100, 50
print(df)
-----------------------
수학  영어   음악   체육
이름                  
서준  90  98   85  100
우현  80  89   95   90
인아  70  95  100   90


    수학  영어   음악  체육
이름                 
서준  90  98   85  80
우현  80  89   95  90
인아  70  95  100  90


    수학  영어   음악  체육
이름                 
서준  90  98   85  90
우현  80  89   95  90
인아  70  95  100  90


    수학  영어   음악   체육
이름                  
서준  90  98   85  100
우현  80  89   95   90
인아  70  95  100   90
    수학  영어   음악  체육
이름                 
서준  90  98   50  50
우현  80  89   95  90
인아  70  95  100  90


    수학  영어   음악  체육
이름                 
서준  90  98  100  50
우현  80  89   95  90
인아  70  95  100  90
---------------------------------

<예제 1-15> 행, 열 바꾸기

#pandas 불러오기
import pandas as pd

#DataFrame() 함수로 데이터 프레임 변환, 변수 df에 저장
exam_data = {'이름' : ['서준', '우현', '인아'], '수학' : [90,80,70], '영어' : [98,89,95],
             '음악' : [85,95,100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

#데이터프레임 df를 전치하기(메소드 활용)
df = df.transpose()
print(df)
print('\n')

#데이터프레임 df를 다시 전치하기(클래스 속성 활용)
df = df.T
print(df)
--------------------------
이름  수학  영어   음악   체육
0  서준  90  98   85  100
1  우현  80  89   95   90
2  인아  70  95  100   90


      0   1    2
이름   서준  우현   인아
수학   90  80   70
영어   98  89   95
음악   85  95  100
체육  100  90   90


   이름  수학  영어   음악   체육
0  서준  90  98   85  100
1  우현  80  89   95   90
2  인아  70  95  100   90
---------------------------------------

<예제 1-16> 특정 열을 행 인덱스로 설정

#pandas 불러오기
import pandas as pd

#DataFrame() 함수로 데이터 프레임 변환, 변수 df에 저장
exam_data = {'이름' : ['서준', '우현', '인아'], '수학' : [90,80,70], '영어' : [98,89,95],
             '음악' : [85,95,100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

#특정 열을 데이터프레임의 행 인덱스로 설정
ndf = df.set_index(['이름'])
print(ndf)
print('\n')
ndf2 = ndf.set_index('음악')
print(ndf2)
print('\n')
ndf3 = ndf.set_index(['수학','음악'])
print(ndf3)
--------------------
이름  수학  영어   음악   체육
0  서준  90  98   85  100
1  우현  80  89   95   90
2  인아  70  95  100   90


    수학  영어   음악   체육
이름                  
서준  90  98   85  100
우현  80  89   95   90
인아  70  95  100   90


     수학  영어   체육
음악              
85   90  98  100
95   80  89   90
100  70  95   90


        영어   체육
수학 음악          
90 85   98  100
80 95   89   90
70 100  95   90
---------------------------

<예제 1-17> 새로운 배열로 행 인덱스 재지정

import pandas as pd

#딕셔너리 정의
dict_data = {'c0' :[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9],
             'c3':[10,11,12], 'c4':[13,14,15]}

#딕셔너리를 데이터프레임으로 변환. 인덱스를 r0, r1, r2로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

#인덱스를 r0, r1, r2, r3, r4로 재지정
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index)
print(ndf)
print('\n')

#reindex로 발생한 NaN값을 숫자 0으로 채우기
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf2 = df.reindex(new_index, fill_value=0)
print(ndf2)
------------------
c0  c1  c2  c3  c4
r0   1   4   7  10  13
r1   2   5   8  11  14
r2   3   6   9  12  15


     c0   c1   c2    c3    c4
r0  1.0  4.0  7.0  10.0  13.0
r1  2.0  5.0  8.0  11.0  14.0
r2  3.0  6.0  9.0  12.0  15.0
r3  NaN  NaN  NaN   NaN   NaN
r4  NaN  NaN  NaN   NaN   NaN


    c0  c1  c2  c3  c4
r0   1   4   7  10  13
r1   2   5   8  11  14
r2   3   6   9  12  15
r3   0   0   0   0   0
r4   0   0   0   0   0
-----------------------------

<예제 1-18> 정수형 위치 인덱스로 초기화

import pandas as pd

#딕셔너리 정의
dict_data = {'c0' :[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9],
             'c3':[10,11,12], 'c4':[13,14,15]}

#딕셔너리를 데이터프레임으로 변환. 인덱스를 r0, r1, r2로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

#행 인덱스를 정수형으로 초기화
ndf = df.reset_index()
print(ndf)
------------------------------
c0  c1  c2  c3  c4
r0   1   4   7  10  13
r1   2   5   8  11  14
r2   3   6   9  12  15


  index  c0  c1  c2  c3  c4
0    r0   1   4   7  10  13
1    r1   2   5   8  11  14
2    r2   3   6   9  12  15
-------------------------------

<예제 1-19> 데이터프레임 정렬

import pandas as pd

#딕셔너리 정의
dict_data = {'c0' :[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9],
             'c3':[10,11,12], 'c4':[13,14,15]}

#딕셔너리를 데이터프레임으로 변환. 인덱스를 r0, r1, r2로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

#내림차순으로 행 인덱스 정렬
ndf = df.sort_index(ascending=False)
print(ndf)
----------------
c0  c1  c2  c3  c4
r0   1   4   7  10  13
r1   2   5   8  11  14
r2   3   6   9  12  15


    c0  c1  c2  c3  c4
r2   3   6   9  12  15
r1   2   5   8  11  14
r0   1   4   7  10  13
-------------------------------

<예제 1-20> 열 기준 정렬

import pandas as pd

#딕셔너리 정의
dict_data = {'c0' :[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9],
             'c3':[10,11,12], 'c4':[13,14,15]}

#딕셔너리를 데이터프레임으로 변환. 인덱스를 r0, r1, r2로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

#c1 열을기준으로 내림차순 정렬
ndf = df.sort_values(by='c1', ascending=False)
print(ndf)
-------------------
c0  c1  c2  c3  c4
r0   1   4   7  10  13
r1   2   5   8  11  14
r2   3   6   9  12  15


    c0  c1  c2  c3  c4
r2   3   6   9  12  15
r1   2   5   8  11  14
r0   1   4   7  10  13
-----------------------------

<예제 1-21> 시리즈를 숫자로 나누기

import pandas as pd

#딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(student1)
print('\n')

#학생의 과목별 점수를 200으로 나누기
percentage = student1/200

print(percentage)
print('\n')
print(type(percentage))
------------------------------
국어    100
영어     80
수학     90
dtype: int64


국어    0.50
영어    0.40
수학    0.45
dtype: float64


<class 'pandas.core.series.Series'>
--------------------------------------------

<예제 1-22> 시리즈 사칙연산

import pandas as pd

#딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90, '영어':80})
print(student1)
print('\n')
print(student2)
print('\n')

#두 학생의 과목별 점수로 사칙연산 수행
add = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1/student2
print(type(division))
print('\n')

#사칙연산 결과를 데이터프레임으로 합치기(시리즈 > 데이터프레임)
result = pd.DataFrame([add, subtraction, multiplication, division], 
                      index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)
----------------------
국어    100
영어     80
수학     90
dtype: int64


수학    80
국어    90
영어    80
dtype: int64


<class 'pandas.core.series.Series'>


              국어        수학      영어
덧셈    190.000000   170.000   160.0
뺄셈     10.000000    10.000     0.0
곱셈   9000.000000  7200.000  6400.0
나눗셈     1.111111     1.125     1.0
-------------------------------------------------

<예제 1-23> NaN값이 있는 시리즈 연산

#라이브러리 불러오기
import pandas as pd
import numpy as np

#딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})
print(student1)
print('\n')
print(student2)
print('\n')

#두 학생의 과목별 점수로 사칙연산 수행
add = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1/student2
print(type(division))
print('\n')

#사칙연산 결과를 데이터프레임으로 합치기(시리즈 > 데이터프레임)
result = pd.DataFrame([add, subtraction, multiplication, division], 
                      index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)
---------------------
국어     NaN
영어    80.0
수학    90.0
dtype: float64


수학    80
국어    90
dtype: int64


<class 'pandas.core.series.Series'>


     국어        수학  영어
덧셈  NaN   170.000 NaN
뺄셈  NaN    10.000 NaN
곱셈  NaN  7200.000 NaN
나눗셈 NaN     1.125 NaN
-------------------------------------

<예제 1-24> 연산메소드 사용 > 시리즈 연산

#라이브러리 불러오기
import pandas as pd
import numpy as np

#딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})
print(student1)
print('\n')
print(student2)
print('\n')

#두 학생의 과목별 점수로 사칙연산 수행(연산 메소드 사용)
sr_add = student1.add(student2, fill_value=0) #덧셈
sr_sub = student1.sub(student2, fill_value=0) #뺄셈
sr_mul = student1.mul(student2, fill_value=0) #곱셈
sr_div = student1.div(student2, fill_value=0) #나눗셈

#사칙연산 결과를 데이터프레임으로 합치기(시리즈 > 데이터프레임)
result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div], 
                      index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)
----------------------
국어     NaN
영어    80.0
수학    90.0
dtype: float64


수학    80
국어    90
dtype: int64


       국어        수학    영어
덧셈   90.0   170.000  80.0
뺄셈  -90.0    10.000  80.0
곱셈    0.0  7200.000   0.0
나눗셈   0.0     1.125   inf
--------------------------------

<예제 1-25> 데이터프레임에 숫자 더하기

#라이브러리 불러오기
import pandas as pd
import seaborn as sns #seaborn 라이브러리에서 제공하는 데이터셋 중에서 타이타닉 데이터셋

#titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age', 'fare']]
print(df.head())
print('\n')
print(type(df))
print('\n')

#데이터프레임에 숫자 10 더하기
addition = df + 10
print(addition.head())
print('\n')
print(type(addition))
---------------------------------
 age     fare
0  22.0   7.2500
1  38.0  71.2833
2  26.0   7.9250
3  35.0  53.1000
4  35.0   8.0500


<class 'pandas.core.frame.DataFrame'>


    age     fare
0  32.0  17.2500
1  48.0  81.2833
2  36.0  17.9250
3  45.0  63.1000
4  45.0  18.0500
---------------------------------

<예제 1-26> 데이터프레임끼리 더하기

#라이브러리 불러오기
import pandas as pd
import seaborn as sns

#titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age', 'fare']]
print(df.tail()) #마지막 5행 표시
print('\n')
print(type(df))
print('\n')

#데이터프레임에 숫자 10 더하기
addition = df + 10
print(addition.tail())
print('\n')
print(type(addition))
print('\n')

#데이터프레임끼리 연산하기(addition - df)
subtraction = addition - df
print(subtraction.tail())
print('\n')
print(type(subtraction))
--------------------------------
age   fare
886  27.0  13.00
887  19.0  30.00
888   NaN  23.45
889  26.0  30.00
890  32.0   7.75


<class 'pandas.core.frame.DataFrame'>


      age   fare
886  37.0  23.00
887  29.0  40.00
888   NaN  33.45
889  36.0  40.00
890  42.0  17.75


<class 'pandas.core.frame.DataFrame'>


      age  fare
886  10.0  10.0
887  10.0  10.0
888   NaN  10.0
889  10.0  10.0
890  10.0  10.0

<class 'pandas.core.frame.DataFrame'>
------------------------------------------------

<예제 2-1> CSV 파일 읽기

#라이브러리 불러오기
import pandas as pd

#파일 결로(파이썬 파일과 같은 폴더)를 찾고, 변수 file_path에 저장
file_path = './read_csv_sample.csv'

#read_csv() 함수로 데이터프레임 변환, 변수에 저장
df1 = pd.read_csv(file_path)
print(df1)
print('\n')

#read_csv() 함수로 데이터프레임 변환. 변수에 저장, header=None 옵션
df2 = pd.read_csv(file_path, header=None)
print(df2)
print('\n')

#read_csv() 함수로 데이터프레임 변환. 변수에 저장, index_col=None 옵션
df3 = pd.read_csv(file_path, index_col=None)
print(df3)
print('\n')

#read_csv() 함수로 데이터 프레임 변환, 변수에 저장, index_col='c0' 옵션
df4 = pd.read_csv(file_path, index_col='c0')
print(df4)
-------------------
FileNotFoundError: [Errno 2] No such file or directory: './read_csv_sample.csv'
-------------------

<예제 2-2> Excel 파일 읽기

import pandas as pd

#read_excel() 함수로 데이터프레임 변환
df1 = pd.read_excel('./남북한발전전력량.xlsx') #header=0(default 옵션)
df2 = pd.read_excel('./남북한발전전력량.xlsx', header = None)#header=None옵션

#데이터프레임 출력
print(df1)
print('\n')
print(df2)
----------------
FileNotFoundError: [Errno 2] No such file or directory: './남북한발전전력량.xlsx'
----------------

<예제 2-3> JSON 파일 읽기

import pandas as pd

#read_json() 함수로 데이터프레임 변환
df1 = pd.read_json('./read_json_sample.json')

print(df)
print('\n')
print(df.index)
------------------
------------------

<예제 2-4> 웹에서 표 정보 읽기

import pandas as pd

#HTML 파일 경로 or 웹페이지 주소를 url변수에 저장
url = './sample.htmml'

#html 웹페이지의 표를 가져와서 데이터프레임으로 변환
tables = pd.read_html(url)

#표 개수 확인
print(len(tables))
print('\n')

#tables 리스트의 원소를 iteration하면서 각각 화면 출력
for i in range(len(tables)):
    print("tables[%s]" % i)
    print(tables[i])
    print('/n')

#파이썬 패키지 정보가 들어있는 두 번재 데이터프레임을 선택하여 df변수에 저장 
df = tables[1]

#name열을 인덱스로 지정
df.set_index(['name'], inplace=True)
print(df)
----------------------
----------------------

<예제 2-5> 미국 ETF 리스트 가져오기


#라이브러리에서 불러오기
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

#위키피디아 미국 ETF 웹페이지에서 필요한 정보를 스크래핑하여 딕셔너리 형태로 변수 etfs에 저장
url = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')
rows = soup.select('div> ul> li')

etfs = {}
for row in rows:
    
    try:
        etf_name = re.findall('^(.*) \(NYSE', row.text)
        etf_market = re.findall('\((.*)\|', row.text)
        etf_ticker = re.findall('NYSE Arca\|(.*)\)', row.text)
        
        if(len(etf_ticker)>0) & (len(etf_market)>0):
            etfs[etf_ticker[0]] = [etf_market[0], etf_name[0]]
            
    except AttributeError as err:
           pass
 
#etfs 딕셔너리 출력
print(etfs)
print('\n')

#etfs 딕셔너리를 데이터프레임으로 변환
df = pd.DataFrame(etfs)
print(df)           
         
#=============================================================================================                    
#=============================================================================================
#김태현
                    
import pandas as pd

dict_data = {'a':1, 'b':2, 'c':3}#딕셔너리 선언

sr = pd.Series(dict_data)#series 메서드 : dictionary를 series로 변환

print(type(sr))
print('n')
print(sr)

import pandas as pd

list_data = ['123', 3.14, "ABC", 100, True] 
sr = pd.Series(list_data)#list를 series로 변환
print(sr)

import pandas as pd

tup_data = ('a', '200', True, 3.14)
sr = pd.Series(tup_data, index=['A', 'B','C', 'D'])#tuple을series로, index에 이름 부여.
print(sr)

import pandas as pd

tup_data = ('a', '200', True, 3.14)
sr = pd.Series(tup_data, index=['A', 'B','C', 'D'])#tuple을series로, index에 이름 부여.
print(sr)
print(sr[0])
print(sr['A'])
print(sr[1:3])#index번호 1,2,3 호출
print(sr['A','C'])#a ~ c 까지의 index


#1-4
import pandas as pd

dict_data = {'c0':[1,2,3],'c1':[1,2,4], 'c2':[1,6,3], 'c3':[6,2,3]}
df = pd.DataFrame(dict_data)#dictionary 자료형을 dateframe으로 변환
print(type(df))
print('\n')
print(df)

#1-5
import pandas as pd

df = pd.DataFrame([[1,2,3],[1,2,4]], 
                  index = ['A','B'], 
                  columns = ['1st','2nd','3rd'])#행과 열에 이름을 지정하여 데이터 프레임 만들기

print(type(df))
print('\n')
print(df)

df.index = ['X','Y']
df.columns = ['1','2','3']
print(type(df))
print('\n')
print(df.index)
print('\n')
print(df.columns)

#1-6
import pandas as pd
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], 
                   index=['준서', '예은'],
                   columns=['나이', '성별', '학교'])

print(df)
print('\n')

df.rename(columns={'나이':'연령', '성별':'남여', '학교':'소속'}, inplace=True)#열 이름을 변경, :앞이 변경전, 뒤가 변경 후
df.rename(index={'준서':'학생1', '예은':'학생2' }, inplace=True)#행 이름을 변경
print(df)

#1-7,8
import pandas as pd

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])#dictionary를 dateframe으로.
print(df)
print('\n')

df2 = df[:]#df를 복사하여 df2에 저장
df2.drop('우현', inplace=True)#df2는 df1에서 우현의 row를 제거한 것
print(df2)
print('\n')

df3 = df[:]
df3.drop(['우현', '인아'], axis=0, inplace=True)#axis는 축 옵션, 0일 때 행을 삭제, 1일 때 열을 삭제

df4 = df[:]
df4.drop('수학', axis=1, inplace=True)#수학에 해당하는 열을 삭제, 열을 삭제할 땐 axis=1을 작성해야한다.
print(df4)
print('\n')

df5=df[:]
df5.drop(['영어','음악'], axis =1, inplace=True )
print(df5)

#1-9 슬라이싱 - 행 선택
import pandas as pd

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])#dictionary를 dateframe으로.
print(df)
print('\n')

labell = df.loc['서준']#이름 기반으로 행 선택
positional = df.iloc[0]#정수형 index 기반으로 행 선택
print(labell)
print('\n')
print(positional)

labell2 = df.loc[['서준', '우현']]#이름 기반으로 각 각 2개의 행 선택
positional2 = df.iloc[[0,1]]#정수형 index기반으로 각 각 2개의 행 선택
print(labell2)
print('\n')
print(positional2)

labell3 = df.loc['서준':'우현']#이름기반으로 범위를 지정할 때 마지막 값이 포함된다.
positional3 = df.iloc[0:1]#index 기반으로 범위를 지정할 때는 마지막 값이 제외된다.
print(labell3)
print('\n')
print(positional3)

#1-10 슬라이싱 - 열 선택
import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print(type(df))#자료형은 dataframe이다 
print('\n')

math1 = df['수학']#수학에 해당하는 열 데이터만 선택하여 math1이라는 변수에 저장한다.
print(math1)
print(type(math1))#자료형은 series이다. 
print('\n')

eng = df.영어
print(eng)
print(type(eng))

music_pe = df[['음악','체육']]
print(music_pe)
print(type(music_pe))
print('\n')

math2 = df[['수학']]
print(math2)
print(type(math2))

#슬라이싱

import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

df.iloc[ : :2 ]#처음부터 끝까지 슬라이싱 간격을 2로 하여 행을 선택한다

df.iloc[0:3:2]

df.iloc[ : :-1]#역순으로 행 선택하기

#1-11 원소 선택

import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

df.set_index('이름', inplace=True)#set_index메서드 -> 이름 열을 새로운 행 인덱스로 지정한다

print(df)
print('\n')
a = df.loc['서준', '음악']#이름 기반 위치에서, 서준 행의 음악 열에 해당하는 원소
print(a)
print('\n')

b = df.iloc[0,2]#index기반 위치에서, 1번째 행의 3번째 열에 해당하는 원소
print(b)
print('\n')

c= df.loc['서준',['음악','체육']]
print(c)
print('\n')

d = df.iloc[0,[2,3]]
print(d)

e = df.loc['서준', '음악':'체육']#서준 행에서 음악부터 체육에 해당하는 범위의 원소
print(e)
print('\n')

f = df.iloc[0,2: ]#1번째 행에서 3번째 열부터 끝 열까지의 범위에 해당하는 원소
print(f)
print('\n')

g = df.loc[['서준', '우현'], ['음악', '체육']]#
print(g)
print('\n')

h = df.iloc[[0, 1], [2, 3]]#
print(h)
print('\n')

i = df.loc['서준':'우현', '음악':'체육']#이름 기반 범위 지정(끝값 포함)
print(i)
print('\n')

j = df.iloc[0:2, 2:]#index기반 범위 지정(끝 값 미포함)
print(j)

#1-12 열 추가 
import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

df['국어'] = 80 #새로운 열 추가, 모든 국어열의 값이 80
print(df)

#1-13 행 추가
import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

df.loc[3] = 0 #새로운 행 추가 : 4번째 행의 모든 값이 0
print(df)
print('\n')

df.loc[4] = ['동규',90,80,70,60] #새로운 행 추가 : 배열 형태로 행을 추가한다
print(df)
print('\n')

df.loc['5행'] = df.loc[3]#기존 행을 복사해서 추가한다
print(df)

#1-14 원소의 값 변경

import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

df.set_index('이름', inplace=True)#이름 열을 새로운 인덱스로 지정하고 df객체에 변경사항 반영
print(df)
print('\n')

df.iloc[0][3] = 80 #1번째 행, 4번째 열의 원소를 80으로 바꾼다
print(df)
print('\n')

df.iloc[0][3] = 80
print(df)
print('\n')

df.loc['서준']['체육'] = 90
print(df)
print('\n')

df.loc['서준', '체육'] = 100
print(df)
print('\n')

df.loc['서준', ['음악', '체육']] = 50 #여러개의 원소의 값을 바꾼다
print(df)
print('\n')

df.loc['서준', ['음악', '체육']] = 100, 50
print(df)

#1-15 행과 열 바꾸기 (전치시키기)
import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

df = df.transpose()#dataframe을 전치시키려면 기존 객체에 새로운 객체를 할당시켜줘야 한다
print(df)
print('\n')

df = df.T#다른 방법
print(df)

#1-16 특정 열을 행 인덱스로 설정하기

import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data) #dictionary를 dataframe으로
print(df)
print('\n')

ndf = df.set_index(['이름'])#특정 열을 행 index로 설정하기
print(ndf)
print('\n')

ndf2 = ndf.set_index('음악')
print(ndf2)
print('\n')

ndf3 = ndf.set_index(['수학','음악'])
print(ndf3)

#1-17 행 인덱스 재배열

import pandas as pd
#dictionary지정
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])#dictionary를 dateframe으로, 행의 이름을 지정
print(df)
print('\n')

new_index = ['r0','r1','r2','r3','r4'] #새로운 index의 list
ndf = df.reindex(new_index)#새로운 index를 위의 list로 지정
print(ndf)#새로운 list의 값이 채워지지 않았기 때문에 Nan으로 표시된다
print('\n')

new_index = ['r0','r1','r2','r3','r4'] #새로운 index의 list
ndf2 = df.reindex(new_index, fill_value=0)#Nan값을 0으로 채운다
print(ndf2)
print('\n')

#1-18정수형 위치 인덱스로 초기화

import pandas as pd
#dictionary지정
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])#dictionary를 dateframe으로, 행(index)의 이름을 지정
print(df)
print('\n')

ndf = df.reset_index()#이름이 지정된 행을 정수형으로 초기화하는 메서드
print(ndf)

#1-19,20 정렬
import pandas as pd

# 딕셔서리를 정의
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 딕셔서리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r2]로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

ndf = df.sort_index(ascending=False)#내림차순으로 행index 정렬, false는 내림차순, True는 오름차순
print(ndf)

ndf2 = df.sort_index(by='c1', ascending=False)#c1 열의 값을 기준으로 행index들이 내림차순으로 정렬된다.
print(ndf2)

#1-21 시리즈 산술 연산
import pandas as pd

#dictionary를 series로
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(student1)
print('\n')

percen = student1/200#series의 모든 값을 200으로 나눈다
print(percen)
print('\n')
print(type(percen))#실수형 자료

#1-22
import pandas as pd

stu1 = pd.Series({'국어':100, '영어':80, '수학':90})
stu2 = pd.Series({'수학':80, '국어':90, '영어':80})

print(stu1)
print('\n')
print(stu2)
print('\n')

#series 끼리의 산술연산 : 같은 위치에서 산술연산이 이루어진다
add = stu1 + stu2
sub = stu1 - stu2
mult = stu1 * stu2
div = stu1/stu2
print(type(div))

res = pd.DataFrame([add, sub, mult, div], index=['+','-','*','/'])
print(res)


#1-23 nan값이 있을 때 연산
import pandas as pd
import numpy as np

stu1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})#numpy 라이브러리에서 nan값 가져오기
stu2 = pd.Series({'수학':80, '국어':90})

print(stu1)
print('\n')
print(stu2)
print('\n')

add = stu1 + stu2 #nan과 어떤 정수를 더하면 0+정수 라고 생각하기 쉽지만, 그렇지 않음에 주의!
sub = stu1 - stu2
mult = stu1 * stu2
div = stu1/stu2

print(type(div))
print('\n')


result = pd.DataFrame([add, sub, mult, div], 
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)#nan을 포함한 연산은 모두 nan으로 처리한다.

#1-24 연산 메서드 : 공통 index가 없거나 nan이 포함된 경우 nan이 반환되는 것을 방지하기 위한 메서드

import pandas as pd
import numpy as np

stu1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})#numpy 라이브러리에서 nan값 가져오기
stu2 = pd.Series({'수학':80, '국어':90})

print(stu1)
print('\n')
print(stu2)
print('\n')

sr_add = stu1.add(stu2, fill_value=0)
sr_sub = stu1.add(stu2, fill_value=0)
sr_mult = stu1.mul(stu2, fill_value=0)#영어라는 공통 index가 없으면 그 자리에 0을 넣어서 연산한다
sr_div = stu1.div(stu2, fill_value=0) #0으로 나누면 inf가 반환된다

res = pd.DataFrame([sr_add,sr_sub, sr_mult, sr_div], index=['덧셈','뺄셈', '곱셈', '나눗셈'])
print(res)

#1-25 데이터프레임에 숫자 더하기

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')#seaborn 라이브러리에 내장되어 있는 데이터
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print('\n')
print(type(df))
print('\n')

import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.tail())          #마지막 5행을 표시
print('\n')
print(type(df))
print('\n')
 
addition = df + 10
print(addition.tail())    #마지막 5행을 표시
print('\n')
print(type(addition))
print('\n')

subtraction = addition - df
print(subtraction.tail())   #마지막 5행을 표시
print('\n')
print(type(subtraction))

#2-1 csv파일 읽기
# 파일의 경로를 하나의 변수에 저장한다. /와\를 잘 구분해야 함.

import pandas as pd


file_path = 'C:/Users/user/Desktop/물리학 프로그래밍/05000266/part2/read_csv_sample.csv'

df1 = pd.read_csv(file_path)#csv파일을 dataframe으로 저장
print(df1)
print('\n')


df2 = pd.read_csv(file_path, header=None)#header옵션이 없으면 첫 행이 열 이름이 된다.
print(df2)
print('\n')


df3 = pd.read_csv(file_path, index_col=None)#index column옵션이 없으면 자동으로 정수형 인덱스가 지정된다
print(df3)
print('\n')


df4 = pd.read_csv(file_path, index_col='c0') #c0열이 index column이 된다
print(df4)

#2-2 엑셀 읽기

import pandas as pd


file_path = 'C:/Users/user/Desktop/물리학 프로그래밍/05000266/part2/남북한발전전력량.xlsx'
df1 = pd.read_excel(file_path, engine='openpyxl')# header=0 기본 옵션
df2 = pd.read_excel(file_path, engine='openpyxl', 
                    header=None)  # header=None 옵션

# 데이터프레임 출력
print(df1)
print('\n')
print(df2)

#2-3jason 파일
import pandas as pd

# read_json() 함수로 데이터프레임 변환 
df = pd.read_json('C:/Users/user/Desktop/물리학 프로그래밍/05000266/part2/read_json_sample.json')  
print(df)
print('\n')
print(df.index)

#2-4 웹에서 가져오기

import pandas as pd

# HTML 파일 경로 or 웹 페이지 주소를 url 변수에 저장
url ='C:/Users/user/Desktop/물리학 프로그래밍/05000266/part2/sample.html'

tables = pd.read_html(url)#웹페이지 주소를 읽어 dataframe으로

print(len(tables))# 표의 갯수 확인
print('\n')

for i in range(len(tables)):
    print("tables[%s]" % i)
    print(tables[i])
    print('\n')

df = tables[1] 

df.set_index(['name'], inplace=True)
print(df)

#2-5 bs4로 받은 객체를 pandas로 처리하기 

import requests #request 모듈
from bs4 import BeautifulSoup as bs #beautifulsoup모듈
import pandas as pd 

page = requests.get("https://library.gabia.com/") #get 메서드 : 해당 url의 html을 요청받을 수 있다
soup = bs(page.text, "html.parser") #응답받은 html내용을 beautifulsoup객체로 반환한다 

elements = soup.select('div.esg-entry-content a.eg-grant-element-0')#html에서 esg-entry-content태그의 하위에 존재하는 a 태그 하위의 span 태그를 선택한다

titles = [] #빈 리스트 
links = []
for index, element in enumerate(elements, 1): #enumerate함수 : index와 원소에 동시에 접근하며 for문 돌리기 ->index와 원소로 이루어진 튜플을 반환한다 
        titles.append(element.text)
        links.append(element.attrs['href']) #attrs메서드 : href에 해당하는 클래스(링크)를 반환


df = pd.DataFrame()
df['titles'] = titles
df['links'] = links

#df.to_excel('./library_gabia.xlsx', sheet_name='Sheet1')#데이터프레임을 엑셀로

print(df)                    
#=============================================================================================                    
#=============================================================================================
         
#=============================================================================================                    
#=============================================================================================
         
#=============================================================================================                    
#=============================================================================================
                    
#=============================================================================================                    
#2주차 Part2-3 ~ Part 3끝까지
#황인준
<예제 2-10> Excelwriter 활용
# 판다스 DataFrame() 함수로 데이터프레임 변환. 변수 df1, df2에 저장  딕셔너리 -> 데이터프레임
data1 = {'name' : [ 'Jerry', 'Riah', 'Paul'],
         'algol' : [ "A", "A+", "B"],
         'basic' : [ "C", "B", "B+"],
          'c++' : [ "B+", "C", "C+"]}

data2 = {'c0':[1,2,3], 
         'c1':[4,5,6], 
         'c2':[7,8,9], 
         'c3':[10,11,12], 
         'c4':[13,14,15]}

df1 = pd.DataFrame(data1)         
df1.set_index('name', inplace=True)      #name 열을 인덱스로 지정
print(df1)
print('\n')
"""
      algol basic c++
name                 
Jerry     A     C  B+
Riah     A+     B   C
Paul      B    B+  C+
"""           
                    
df2 = pd.DataFrame(data2)
df2.set_index('c0', inplace=True)        #c0 열을 인덱스로 지정
print(df2)
"""
    c1  c2  c3  c4
c0                
1    4   7  10  13
2    5   8  11  14
3    6   9  12  15
"""           
                    
                    
# df1을 'sheet1'으로, df2를 'sheet2'로 저장 (엑셀파일명은 "df_excelwriter.xlsx")
writer = pd.ExcelWriter("./df_excelwriter.xlsx")
df1.to_excel(writer, sheet_name="sheet1")
df2.to_excel(writer, sheet_name="sheet2")
writer.save()                    
"""
해당 코드 실행 시, FutureWarning: save is not part of the public API, usage can give unexpected results and will be removed in a future version  writer.save()
에러가 발생함.
해당 에러는 파일이 수정되면 변경될수 있다는것으로, writer.save()를 writer.close()로 바꾸면 해결 가능
"""

#================================
<예제 3-1> 데이터 살펴보기
                    
# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None) #header=None : 첫 행부터 다 데이터. 열이름을 따로 설정해줌

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 데이터프레임 df의 내용을 일부 확인 
print(df.head())     # 처음 5개의 행, 기본값이 5행 head()안에 몇 행 불러올지 지정 가능
print('\n')
print(df.tail())     # 마지막 5개의 행, 기본값이 5행 tail()안에 몇 행 불러올지 지정 가능
"""
    mpg  cylinders  displacement  ... model year  origin                       name
0  18.0          8         307.0  ...         70       1  chevrolet chevelle malibu
1  15.0          8         350.0  ...         70       1          buick skylark 320
2  18.0          8         318.0  ...         70       1         plymouth satellite
3  16.0          8         304.0  ...         70       1              amc rebel sst
4  17.0          8         302.0  ...         70       1                ford torino

[5 rows x 9 columns]


      mpg  cylinders  displacement  ... model year  origin             name
393  27.0          4         140.0  ...         82       1  ford mustang gl
394  44.0          4          97.0  ...         82       2        vw pickup
395  32.0          4         135.0  ...         82       1    dodge rampage
396  28.0          4         120.0  ...         82       1      ford ranger
397  31.0          4         119.0  ...         82       1       chevy s-10

[5 rows x 9 columns]
"""
# pd.set_option('display.max_columns', None) 함수로, 중략되는 열을 전부 다 표시 가능. columns를 rows로 바꿔서 행도 전부 표시 가능.                    
# df의 모양과 크기 확인: (행의 개수, 열의 개수)를 투플로 반환 #투플: 읽기만 되는 리스트
print(df.shape) #(row , column) 의 형태로 몇행 몇열짜리 데이터베이스인지 반환
print('\n')
"""
(398, 9)
"""
# 데이터프레임 df의 내용 확인 
print(df.info())
print('\n')
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 398 entries, 0 to 397
Data columns (total 9 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   mpg           398 non-null    float64
 1   cylinders     398 non-null    int64  
 2   displacement  398 non-null    float64
 3   horsepower    398 non-null    object 
 4   weight        398 non-null    float64
 5   acceleration  398 non-null    float64
 6   model year    398 non-null    int64  
 7   origin        398 non-null    int64  
 8   name          398 non-null    object 
dtypes: float64(4), int64(3), object(2)
memory usage: 28.1+ KB
None

"""
# 데이터프레임 df의 자료형 확인 
print(df.dtypes)
print('\n')
"""
mpg             float64
cylinders         int64
displacement    float64
horsepower       object
weight          float64
acceleration    float64
model year        int64
origin            int64
name             object
dtype: object

"""
# 시리즈(mog 열)의 자료형 확인 
print(df.mpg.dtypes)
print('\n')
"""
float64
"""
# 데이터프레임 df의 기술통계 정보 확인 
print(df.describe())
print('\n')
print(df.describe(include='all'))
"""
              mpg   cylinders  ...  model year      origin
count  398.000000  398.000000  ...  398.000000  398.000000
mean    23.514573    5.454774  ...   76.010050    1.572864
std      7.815984    1.701004  ...    3.697627    0.802055
min      9.000000    3.000000  ...   70.000000    1.000000
25%     17.500000    4.000000  ...   73.000000    1.000000
50%     23.000000    4.000000  ...   76.000000    1.000000
75%     29.000000    8.000000  ...   79.000000    2.000000
max     46.600000    8.000000  ...   82.000000    3.000000

[8 rows x 7 columns]


               mpg   cylinders  ...      origin        name
count   398.000000  398.000000  ...  398.000000         398
unique         NaN         NaN  ...         NaN         305
top            NaN         NaN  ...         NaN  ford pinto
freq           NaN         NaN  ...         NaN           6
mean     23.514573    5.454774  ...    1.572864         NaN
std       7.815984    1.701004  ...    0.802055         NaN
min       9.000000    3.000000  ...    1.000000         NaN
25%      17.500000    4.000000  ...    1.000000         NaN
50%      23.000000    4.000000  ...    1.000000         NaN
75%      29.000000    8.000000  ...    2.000000         NaN
max      46.600000    8.000000  ...    3.000000         NaN

[11 rows x 9 columns]

"""                    
#================================
                    
#================================
                    
#================================
                    
#================================
                    
#================================
                    
#================================
                    
#================================
                    
#============================================================================================= 
#김태현                    
#============================================================================================= 
#박연주                    
#============================================================================================= 
#이준형                    
#=============================================================================================                     
                    
                    
                    
