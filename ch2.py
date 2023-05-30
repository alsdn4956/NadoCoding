'''print(-10)
print(3.14)
print( 6*3)
print(6 +(5*3))

# 문자열(string)
print("풍선")
print("작은 나비")
print("자바" * 4)

# 불 자료형
print( 5> 10)
print(10 > 5)

print(not True)
print(not False)

# 5는 10보다 크지 않다
print(not (5 > 10))

#변수
#형식 : 변수명 = 값

name = "해피"
animal = "고양이"
age = 2  #숫자는 따옴표 없이 그냥 4
hobby = "축구"
is_male = True

print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 " + animal +"인데, 이름이 " + name +"예요.")
print(name + "는 " +str(age) +"살이고, " + hobby +"을 아주 좋아해요.")  #숫자를 문자열과 결합해서 오류 발생. +로 연결할 때는 값의 형태인 자료형이 같아야함. 그래서 str(age)로!

# 쉼표로 연결하기
# +연산자말고 쉼표로도 사용 가능. 쉼표는 형변환 x, 값과 값 사이에 빈칸을 하나 포함.

print(name,"는",age,"살이고",hobby,"을 아주 좋아해요.")



# 형변환하기
print(int(3.5))
print(float(3.5))
print(float(3))

# type()
print(type(3))
print(type(3.5))
print(type(str(3)))

number = 3
print(number) '''
'''
# 실습문제 : 역 이름 출력하기
station = "사당"
#station = "신도림"
#station = "인천공항"

print(station+"행 열차가 들어오고 있습니다.")
'''

#셀프체크
status = "상품준비"
#status = "배송 중"
#status = "배송 완료"
print("주문상태 : "+ status)






