#subway =[10,20,30]
#print(subway)

'''subway=["푸","피글렛","티거"]
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
'''

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
