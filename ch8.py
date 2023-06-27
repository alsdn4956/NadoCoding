#데이터를 파일로 저장하기 : pickle 모듈

#형식 : dump(저장할 데이터, 저장할 파일명)

import pickle

profile_file = open("profile.pickle", "wb") #바이너리 형태로 저장

profile = {"이름" : "스누피", "나이" : 30, "취미": ["축구","골프","코딩"]}
print(profile)

#파일 한번에 열고 닫기: with문
#형식 : with 작업 as 변수명 : 

for i in range(1,51):
    with open(str(i) + "주차.txt","w", encoding= "utf8") as report_file:
        report_file.write("-{}주차 주간보고 -".format(i))
        report_file.write("\n부서 : ") #줄 바꿈 처리
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")
        
#Self Check

with open("class.txt", "r", encoding="utf8") as f:
    txt= f.read()
    words= txt.split()
    
    for word in words:
        print(word, end=" ")
        if word.endwith("명"): #명으로 끝나면 줄 바꿈
            print()
            
        

