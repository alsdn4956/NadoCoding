# 문자열

'''
sentence1 = "나는 소년입니다."
print(sentence1)

sentence2= "파이썬은 쉬워요."
print(sentence2)

print(type(sentence1))

print(sentence1,( type(sentence1)))



#인덱스란? 여러 문자로 구성된 문자열의 n번째 문자라고 할 때, n번째가 바로 인덱스이다.
# 즉 인덱스는, 데이터의 순서 또는 위치를 나타낸다.

# 형식 : 변수명[인덱스]

jumin= "990229-1234567"
print("성별 주민번호 :"+jumin[7])  #인덱스는 0부터 시작! 0 1 2 3 4 ~
# 슬라이싱
# 형식 : 변수명[시작 인덱스:종료 인덱스] 시작 인덱스부터 종료 인덱스 직전까지
jumin = "990229-1234567"
print("연 : ", jumin[0:2])   #0,1
print("연 : ", jumin[2:4])   #2,3
print("연 : ", jumin[4:6])   #4,5

print("생년월일 : ",jumin[:6])
print("생년월일 : ",jumin[7:])
print("생년월일 : ",jumin[:])


fruit ="apple"
print(fruit[:-1])


lower() 문자열을 소문자로 upper 대문자로 
islower() 소문자 인지 확인 isupper

replace() 문자열 바꾸기
index() 찾는 문자열의 인덱스(없으면 오류발생)
find() 찾는 문자열의 인덱스(없으면 -1반환)
count() 문자열이나온 횟수


# 형식 : 문자열 혹은 변수.함수()

python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[1].islower())
print(python[3].isupper())
print(python.replace("Python", "Java"))


find = python.find("n")
print(find)
find = python.find("n", find +1)
print(find)


python = "Python is Amazing"

print(python.count("n"))
print(python.count("v"))

print(len(python))

#문자열 포매팅
# 1. 서식 지정자 사용하기   
# %d 정수 %f 실수 %c 문자(character) %s 문자열(string)

# 형식 : print("문자열 서식지정자 문자열" % 값)

print("나는 %d살 입니다." % 20)
print("나는 %s을 좋아합니다." %"사람")
print("Apple은 %c로 시작해요." %"A")
print("나는 %s살 입니다." %20)

# 값이 여럿일 때
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

#형식 : print("문자열{인덱스}문자열{인덱스} ...".format(값1, 값2, ...))

print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))

print("나는 {age}살이며, {color}색을 좋아해요".format(age=45,color="초록"))

# f-문자열 사용하기
# 형식 : print(f"문자열{변수명1}문자열{변수명2}

age =20
color ="빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
'''
print("백문이 불여일견\n백견이 불여일타.")

print("저는 \"나도코딩\"입니다.")
      
#python 3.6.9

'''
url = "http://naver.com"
#url = "http://daum.net"
#url = "http://google.com"
#url = "http://youtube.com"

my_pass = url.replace("http://", "")    #naver.com
my_pass= my_pass[:my_pass.index(".")]   #naver
my_pass= my_pass[0:3] + str(len(my_pass)) + str(my_pass.count("e"))+"!"
print("{}의 비밀번호는 {}입니다.".format(url, my_pass))
'''


#Self Check

sentence = "the early bird catches the worm."
#sentence = "Actions Speak Louter Than Words."
#sentence = "PRATICE MAKES PERFECT."

sentence = sentence[0].upper() + sentence[1:].lower()
print(sentence)
