# 3. 연산자
'''
printnt(1+1)
print(5*2)
print(6/3)    #-> 나누기 결과는 실수 2.0으로 나옴


print( 2** 3)   #거듭제곱
print( 10% 3 )   #나머지
print(10//3)  #10을 3으로 나눈 몫인 3

print(10 > 3)
print( 4>=7 )
print (10<3)
print (5<=5)
print( 3==3)
print(4!=5)

print( (3>0) and (5>4))


number = 2+3*4
print(number)
number= number +2   # 변수로 연산하기 (2+3*4)2 

#number = number + 2 = number +=2
#number = number - 2 = number -= 2
number = 2+3*4
print(number)

number += 2
print(number)

number -= 2
print(number)

number *= 2
print(number)


#  3.4 함수로 연산하기


abs(x)  = absolute  x의 절댓값
pow(x,y) x를 y만큼 거듭제곱한 값
round(x , d) x를 반올림한 값, d는 표시할 소수점 이하 자릿수 

print(abs(-5))
print(pow(3, 2))
print(max( 5,12,46,78,34))
print(min(4,2,4,78,99,1))
print(round(3.14))
print(round(3.789,2))

# math  모듈
# floor() 내림, ceil() 올림, sqrt() 제곱근

# **형식 =  from 모듈명 import 기능
#ex> from 모듈명 import * = 모든 기능 가져다 쓰겠다는 의미


from math import *

result = floor(4.99)
print(result)

result = ceil(3.14)
print(result)

result = sqrt(16)
print(result)


# 형식  = import 모듈명
# 이때는 모듈명을 점.으로 연결해서 적어야 함.
import math

result = math.floor(4.2)
print(result)
result = math.ceil(7.1)
print(result)
result = math.sqrt(64)
print(result)



from random import *

print(random())
print(random())
print(random())

print(random() *10)
print(int(random() *10))
print(int(random()*10) +1)
# 1부터 45 까지 정수 범위 안에서 로또 번호를 뽑으려 한다.
print(int(random()*45)+1)


#randrange(시작 숫자, 끝 숫자)  -> 범위를 설정할 수 있다. 끝 숫자 미포함
#randint(시작 숫자, 끝 숫자) -> 끝 숫자 포함
'''


from random import *
print("오프라인 스터디 모임 날짜는 매월 ", randint(4, 28), "일로 선정 되었습니다.")



# 답지
'''
from random import * 
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 "+ str(date) + "일로 선정 되었습니다.")
'''



#Self Check

'''C =30
print("섭씨 온도 : ",C)
C= (C*9 /5) + 32
print("화씨 온도 : ",C)



X = 10
print("섭씨 온도 : ",X)
X= (X*9/5) +32
print("화씨 온도 : ",X)
'''

celsius = 10
fahrenheit = (celsius *9 / 5) + 32
print("섭씨 온도 : ", celsius)
print("화씨 온도 : ", fahrenheit)
