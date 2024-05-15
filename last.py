#예외 처리 : try-except 문

#try : 
    # 명령 1, 2 ....
#except 오류 종류 :
    #예외 처리 명령1 2 ....
'''try :
    print("나누기 전용 계산기입니다.")
    num1 = int(input("숫자를 입력하세요:"))
    num2 = int(input("숫자를 입력하세요:"))
    print(" {} / {} ={}입니다.".format(num1,num2,int(num1 / num2)))
    
except ValueError :
    print("오류 발생! 잘못된 값을 입력했습니다.")
    
except ZeroDivisionError as err:
    print(err)
    
# 실습 문제 : 치킨 주문하기


class SoldOutError(Exception):
    pass




chicken = 10 # 남은 치킨 수
waiting = 1  # 대기번호


while True:
    try:
        print("[남은 치킨 : {}]".format(chicken))
        order = int(input("치킨을 몇마리 주문하시겠습니까?"))
        if order > chicken :    #남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else: 
            print("[대기번호 {}] {} 마리를 주문했습니다.".format(waiting, order))
            waiting += 1  #대기번호 1증가
            chicken -= order #주문 수 만큼 남은 치킨 감소
            
        if chicken == 0:   #if 문을 아래로 다시한번 써도 되는구나 ...
            raise SoldOutError
            
    
    except ValueError :
        print("값을 잘못 입력했습니다.")
    
    except SoldOutError:
        print ("재료가 소진돼 더 이상 주문을 받지 않습니다.")
        break
        
'''



def save_battery(level):
    try:
        
        
        print(f"배터리 잔량 : {level} %")  #배터리 잔량표시
        if level > 30:
            print("일반 모드로 사용합니다.")
        elif level >5 :
            print("절전 모드로 사용합니다.")
        else :
            raise Exception("배터리가 부족해 스마트폰을 종료합니다.")
            
    except Exception as e :
        print(e)

    
    
save_battery(75)
save_battery(25)
save_battery(3)
     
