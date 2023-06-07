# 제어문
# 형식: if 조건:
              #실행할 명령
'''
weather= "비"
if weather == "비" :
    print("우산을 챙기세요")

weather = "맑음"
if weather == "비":
    print("우산을 챙기세요")



weather = "맑음"
if weather =="비":
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else :
    print("준비물이 필요 없어요.") 
    
weather = input("오늘 날씨는 어때요?")
if weather == "맑음":
    print("굳")
elif weather == "비":
    print("우산 ㄱ")
else:
    print("나가자")
# if weather == "비" or weather == "눈" 이렇게 조건 변경을 해줄 수 있다.


temp = int(input("오늘 기온은 어때요?"))

if 30 <= temp:
    print("너무더워")
elif 10 <= temp < 30 :
    print("굳")
else:
    print("추우니 야외활동 금지")


# 반복문 : for문과 while문
# for문 형식 : for 변수 in 반복대상 :
                            #실행할 명령1 ~~
    
for waitingno in [1,2,3,4,5]:
    print("대기번호 : {0}".format(waitingno))  #{0} 값에 waitingno 값이 들어감.
# 형식 : range(숫자),   ragne(시작 숫자, 끝 숫자),    range(시작 숫자, 끝 숫자, 간격)

for waitingno in range(1,6):  #0,1,2,3,4
    print("대기번호 : {0}".format(waitingno))
    
for waitingno in range(1,6,2):  #0,1,2,3,4
    print("대기번호 : {0}".format(waitingno))


orders = ["토르","아이언맨","헐크"]

for customers in orders:
    print("{0}님, 커피가 준비됐습니다. 픽업대로 와주세요.".format(customers))

#while문

customer = "토르"
index = 5

while index >=1 :  #부르는 횟수가 1이상일 때만 실행 !!
    print("{}님, 커피가 준비됐습니다.".format(customer))
    index -= 1 #횟수 1회 차감
    print("{}번 남았습니다.".format(index))
    
    if index == 0:
        print("폐기 처분합니다.")
'''
customer = "토르"
person = None

while person != customer:
    print("{}님, 커피가 준비됐습니다.".format(customer))
    person= input("이름이 어떻게 되세요?")
    


     
