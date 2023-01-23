import pandas as pd
================================
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
================================
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
서준  90  80   85  100
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
서준  90  80   85  100
인아  70  95  100   90

"""
                   
# 데이터프레임 df를 복제하여 변수 df3에 저장. df3의 2개 행(row) 삭제 
dfs = df[:] 
df3.drop(['우현', '인아'], axis=0, inplace=True) 
print(df3) 
"""
    수학 영어 음악 체육
서준  90  80   85  100

"""

================================
#예제 1


================================
