# 사용자 정의 함수 
# 형식 : def 함수명() :

'''def open_account():
    print("새로운 계좌를 개설합니다.")

open_account()  #앞에 정의한 open_account() 함수 호출


#def 함수명(전달값1, 전달값2, ...) :
    #return 반환값1


#출금 계좌

def open_account():
    print("새로운 계좌를 개설합니다.")

open_account()

def deposit(balance, money): #입금 처리 함수
    print("{}원을 입금했습니다. 잔액은 {}원입니다.".format(money,balance+money))
    return balance+money


def withdraw_night(balance,money):
    commision=100
    print("업무시간 외에 {}원을 인출하였습니다.".format(money))
    return commision, balance-money-commision

balance = 0
balance = deposit(balance, 1000)

commision, balance = withdraw_night(balance, 500)
print("수수료 {}원이며, 잔액은 {}원입니다.".format(commision, balance))



def withdraw(balance, money):
    if balance>=money :
        print("{}원을 인출합니다. 현재 잔액은 {}원입니다.".format(money,balance-money))
        return balance-money #출금 후 잔액 반환
        
    else :
        print("잔액이 부족합니다. 다시 시도하세요.")
        return balance #기존 잔액 반환
    
balance = 0
balance = deposit(balance, 1000)   #입금

balance= withdraw(balance, 2000)  #2000원 출금시도
balance = withdraw(balance, 500)   #500원 출금시도



def profile(name, age=20, main_lang="파이썬"):
    print("이름 : {}\t나이 : {}\t 주 사용 언어 : {}".format(name,age,main_lang))
    
profile("찰리")
profile("찰리",22)
profile("찰리",25,"자바")
'''

def profile(name, age, lang1,lang2,lang3,lang4,lang5):
    print("이름 : {}\t나이 : {}\t ".format(name,age,), end=" ")
    print(lang1,lang2,lang3,lang4,lang5)
    
profile("찰리",20,"파이썬","자바","C","C++","C#")
profile("푸스",21,"코틀린","스위프트","","","")

#형식 : print("출력할내용, sep="",end"\n", file=None, flush=False)





    
    
