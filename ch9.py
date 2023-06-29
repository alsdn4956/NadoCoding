#클래스** 
'''  
name = "보병" #이름
hp = 40 #체력
damage = 5 #공격력

print("{} 유닛을 생성했습니다.".format(name))
print("체력 {}, 공격력 {}\n".format(hp,damage))


tank_name = "탱크" #이름
tank_hp = 150 #체력
tank_damage = 35 #공격력

print("{} 유닛을 생성했습니다.".format(tank_name))
print("체력 {}, 공격력 {}\n".format(tank_hp,tank_damage))



    
tank2_name = "탱크" #이름
tank2_hp = 150 #체력
tank2_damage = 35 #공격력

print("{} 유닛을 생성했습니다.".format(tank2_name))
print("체력 {}, 공격력 {}\n".format(tank2_hp,tank2_damage))





# 공격함수 / 공격 부분은 두 유닛이 공통으로 사용. 함수로 정의

def attack(name, location, damage):
    print("{} : {} 방향 적군을 공격합니다. [공격력{}]".format(name,location,damage))
        
attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)


#클래스와 객체 생성하기

# 형식 : class 클래스명 :
    #def 메서드명(self, 전달값1, 전달값2 ..):
    
#형식 : self.변수명= 값

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name #인스턴트 변수 name에 전달값 name 저장
        self.hp = hp #인스턴트 변수 hp에 전달값 hp 저장
        self.damage = damage #인스턴트 변수 damage에 전달값 damage 저장
        
        print("{} 유닛을 생성했습니다.".format(name))
        print("체력 {}, 공격력 {}".format(hp,damage))
        
# 형식 : 객체명 = 클래스명(전달값1, 전달값2 ...)

soldier1= Unit("보병",40,5)
soldier2= Unit("보병",40,5)
soldier3= Unit("탱크",150,35)

#__init__ 은 생성자라고 한다.

# 전투기 : 공중유닛, 은폐 불가
stealth1 = Unit("전투기", 80,5)
#인스턴스 변수 접근
print("유닛 이름 : {}, 공격력 : {}".format(stealth1.name, stealth1.damage))


stealth2= Unit("업그레이드한 전투기", 80,5)

stealth2.cloaking= True

if stealth2.cloaking == True:
    print("{}는 현재 은폐 상태입니다.".format(stealth2.name))
    
#오류발생
#if stealth1.cloaking== True :
 #   print("{}는 현재 은폐 상태입니다.".format(stealth1.name))
'''



#일반 유닛
class Unit :
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed     #지상 이동 속도
        
        
    def move(self,location):
        print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name,location,self.speed))
        
        
              
    
    
    
class AttackUnit(Unit) : #공격 유닛
    def __init__(self, name, hp, damage,speed) : #speed 추가
        Unit.__init__(self,name,hp,speed) #speed 추가
        self.damage = damage
        
 
    def attack(self, location):
        print("{} : {} 방향 적군을 공격합니다. [공격력 {}]".format(self.name,location,self.damage))
    
    
    def damaged(self, damage) : #damage 만큼 유닛 피해
        print("{} : {} 만큼 피해를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{} : 현재 체력은 {}입니다.".format(self.name,self.hp))
    
        if self.hp <= 0 :
            print("{}: 파괴됐습니다.".format(self.name))
        
        
class Flyable:
    def __init__(self,flying_speed): # 비행속도
        self.flying_speed = flying_speed
        
        
    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]".format(name,location,self.flying_speed))
        
        
        
# 공중 공격 유닛

class FlyableAttackUnit(AttackUnit, Flyable) :
    #유닛 이름, 체력, 공격력, 비행속도
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self,name,hp,damage,0) #지상 이동 속도 0
        Flyable.__init__(self,flying_speed)
        
    def move(self,location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
        
                         
        
        
        
        
# 요격기
#interceptor = FlyableAttackUnit("요격기",200,6,5)
#interceptor.fly(interceptor.name, "3시")
        

    
# 호버 바이크 : 지상유닛, 기동성 좋음
hoverbike = AttackUnit("호버 바이크", 80 ,20,10) #지상 이동 속도 10

#우주 순양함 : 공중유닛, 체력 굉장히 좋음, 공격력도 좋음
spacecruiser = FlyableAttackUnit("우주 순양함", 500,25,3) #비행속도 3

hoverbike.move("11시")
spacecruiser.move("9시")


























