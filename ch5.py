#subway =[10,20,30]
#print(subway)

subway=["푸","피글렛","티거"]
subway.append("이요르")

subway.insert(1,"루")
print(subway)

print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

subway.clear() #모두 내림
print(subway)

subway =["푸","피글렛","티거"]
subway.append("푸")
print(subway)
print(subway.count("푸"))

num_list=[5,2,4,3,1]
num_list.sort()  # 오름차순 정렬
print(num_list)

num_list.reverse()  #순서 뒤집기
print(num_list)

mixlist=["푸",20,True]
print(mixlist)

numlist=[5,3,4,8,7]
mixlist.extend(numlist)
print(mixlist)


# 딕셔너리
# 형식 : 딕셔너리명 = {key1: value1, key2: value2}

empty_dict={} #빈 딕셔너리 생성하기

cabinet = {3:"푸", 100:"피글렛"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(5))
print("hi")
# print(cabinet[5])


print(cabinet.get(5,"사용가능"))

print(3 in cabinet)
print(5 in cabinet)

print("곰" in "곰돌이")

cabinet = {"A-3" : "푸", "B-100": "피글렛"}
print(cabinet)
cabinet["A-3"]="티거"  #key에 해당하는 값이 있을 때 -> 값 변경
cabinet["C-20"] = "이요르" #key에 해당하는 값이 없을 때 -> 값 추가

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys()) #key 만 출력
print(cabinet.values()) #value만 출력

print(cabinet.items()) #key, value 둘다 출력


cabinet.clear()
print(cabinet)


#튜플
#리스트의 읽기 전용 버전
#튜플은 리스트와 달리 처음 정의할때를 제외하고 값의 변경이나 추가,삭제가 불가능하다.

#형식 : 튜플명 = (값1, 값2 ...)

menu = ("돈가스", "치즈돈가스")
print(menu[0])
print(menu[1])

name = "피글렛"
age = 20
hobby = "코딩"
print(name,age,hobby)

#name,age,hobby)=("피글렛",20,"코딩")
#print(name,age,hobby)

(departure, arrival)=("김포","제주")
print(departure, ">", arrival)

#세트
myset={1,2,3,3,3}
print(myset)

java={"푸","피글렛","티거"}
python= set(["푸","이요르"])

#empty_set=set()
print(java&python)
print(java.intersection(python))

print(java | python)  #세트는 데이터의 순서를 보장하지않는다. 결과가 매번 달라진다.
print(java.union(python))

python.add("티거")
print(python)
java.remove("피글렛")
print(java)

# 자료구조 변환하기
# 리스트를 튜플로 ,튜플을 세트로, 세트를 리스트로

menu = {"커피","우유","주스"}  #딕셔너리는 key:value 이다
print(menu)
print(type(menu))

menu= list(menu) # 리스트로 변환
print(menu)
print(type(menu))



menu=tuple(menu)
print(menu)
print(type(menu))

menu=set(menu)
print(menu, type(menu))

from random import *

id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(id)
print("-- 당첨자 발표 --")
print("치킨 당첨자 :",randint(1,20))
print("커피 당첨자 :",sample(id,3))
print("-- 축하합니다! --")
# 중복발생 ...



# 답지
from random import *

users=range(1, 21)
users= list(users)
shuffle (users)

winners=sample(users,4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다! --")



print("신청한 과목은 다음과 같습니다.")

Object=["자료구조","알고리즘","자료구조","운영체제"]
Object=set(Object)
Object=list(Object)
print(Object)





