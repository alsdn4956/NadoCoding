

#일반 유닛
class Unit :
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed     #지상 이동 속도
        print("{} 유닛을 생성했습니다.".format(name))
        
        
    def move(self,location):
        #print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name,location,self.speed))
        
    def damaged(self, damage) : #damage 만큼 유닛 피해   #AttackUnit 클래스에서 Unit 클래스로 이동
        print("{} : {} 만큼 피해를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{} : 현재 체력은 {}입니다.".format(self.name,self.hp))
        if self.hp <= 0 :
            print("{}: 파괴됐습니다.".format(self.name))
        
              
    
    
#공격 유닛    
class AttackUnit(Unit) :
    def __init__(self, name, hp, damage,speed) : #speed 추가
        Unit.__init__(self,name,hp,speed) #speed 추가
        self.damage = damage
        
 
    def attack(self, location):
        print("{} : {} 방향 적군을 공격합니다. [공격력 {}]".format(self.name,location,self.damage))
    

#보병 유닛
class Soldier(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"보병",40,5,1)
        
        #강화제: 일정 시간 동안 이동속도와 공격속도 증가, 체력 10 감소
    def booster(self):
        if self.hp>10 :
            self.hp-= 10
            print("{} : 강화제를 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{} : 체력이 부족해 기술을 사용할 수 없습니다.".format(self.name))

            
            
#탱크 유닛
class Tank(AttackUnit):
    #시지 모드 : 탱크를 지상에 고정, 이동불가, 공격력 증가
    siege_developed = False #시즈모드 개발여부, 클래스 변수로 정의
 
    
    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,35,1)
        self.seige_mode= False #시즈모드 (해제상태), 인스턴스 변수로 정의
       
        #시즈 모드 설정
    def set_siege_mode(self):
        if Tank.siege_developed == True :   #시즈모드가 개발되지 않았으면 바로 전환
            return
        #현재 일반 모드일 때
        if self.siege_mode == False:
            print("{} : 시즈 모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.siege_mode = True
            
        #현재 시즈 모드일 때
        else :
            print("{} : 시즈 모드를 해제합니다.".format(self.name_))
            self.damage //=2
            self.siege_mode= False
             
  


#비행 기능        
class Flyable:
    def __init__(self,flying_speed): # 비행속도
        self.flying_speed = flying_speed
        
       
    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]".format(name,location,self.flying_speed))
        
        
        
# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable) :  #다중상속
    #유닛 이름, 체력, 공격력, 비행속도
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self,name,hp,damage,0) #지상 이동 속도 0
        Flyable.__init__(self,flying_speed)
        
    def move(self,location):
        self.fly(self.name, location)
        

        
        
# 전투기 유닛
class Stealth(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "전투기", 80,20,5)
        self.cloaked = False
        
        
        
    def cloaking(self):
        #현재 은폐 모드일 때
        if self.cloaked == True:
            print("{} : 은폐 모드를 해제합니다.".format(self.name))
            self.cloaked = False
            
        #현재 은폐 모드가 아닐 때
        else:
            print("{} : 은폐 모드를 설정합니다.".format(self.name))
            self.cloaked = True
            


   
#건물 유닛
'''class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0) #건물 못 움직이므로 location = 0
        super().__init__(name,hp,0)  #부모클래스 접근, self 없이 사용
        self.location = location
        
        
        
    
supply_depot = BuildingUnit("보급고", 500,"7시")  #위에 건물유닛 배정받음 따라서  name, hp, location 
'''




#interceptor = FlyableAttackUnit("요격기",200,6,5)
#interceptor.fly(interceptor.name, "3시")
        

    
# 호버 바이크 : 지상유닛, 기동성 좋음
#hoverbike = AttackUnit("호버 바이크", 80 ,20,10) #지상 이동 속도 10

#우주 순양함 : 공중유닛, 체력 굉장히 좋음, 공격력도 좋음
#spacecruiser = FlyableAttackUnit("우주 순양함", 500,25,3) #비행속도 3

#hoverbike.move("11시")
#spacecruiser.move("9시")


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
    
    
def game_over():
    print("Player : Good Game")
    print("[Player] 님이 게임에서 퇴장했습니다.")
    

    
    
    
#게임 시작
game_start()

#보병 3기 생성
so1 = Soldier()
so2 = Soldier()
so3 = Soldier()

#탱크 2기 생성
ta1 = Tank()
ta2 = Tank()

#전투기 1기 생성
st1 = Stealth()          #함수를 만들고 시행을 할 때는 변수 설정 후 st1= 실행하고 싶은 함수()



#유닛 일괄 관리(생성된 모든 유닛 추가)
attack_units = []
attack_units.append(so1)
attack_units.append(so2)
attack_units.append(so3)
attack_units.append(ta1)
attack_units.append(ta2)
attack_units.append(st1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

    
Tank.siege_developed = True
print("[알림] 탱크의 시즈 모드 개발이 완료됐습니다.")
    
    


#공격 준비와 전군 공격
# 형식 : isinstance(객체명, 클래스명)


#공격 모드 준비 : (보병: 강화제, 탱크: 시즈모드, 전투기: 은폐 모드)
for unit in attack_units:
    if isinstance(unit, Soldier): #Soldier 클래스의 인스턴스이면 강화제
        unit.booster()
        
    elif isinstance(unit, Tank):  #Tank 클래스의 인스턴스이면 시즈모드
        unit.set_siege_mode()
        
    elif isinstance(unit, Stealth) :#Stealth 클래스의 인스턴스이면 은폐모드
        unit.cloaking()
        
        

        

from random import *        
        
#전군 공격
for unit in attack_units:
    unit.attack("1시")
        
#전군 피해
for unit in attack_units:
    unit.damaged(randint(5,20))  #피해는 5~20 무작위로 받음
    
game_over()










    
    



