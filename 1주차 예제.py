import pandas as pd
import numpy as np 
#================================
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


#================================                   
