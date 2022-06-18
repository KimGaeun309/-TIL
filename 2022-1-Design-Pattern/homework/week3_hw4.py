# 4. 자유롭게 상황을 설정 후 Prototype Pattern을 적용한 클래스를 
# 설계해보고 인스턴스를 생성하는 코드를 작성하시오.
#    ex) 게임프로그램에서 캐릭터를 다루는 클래스를 구현하고자 할때,  prototype 패턴을 적용해보겠다. 등
# 5. 4번에 대해 왜 그러한 상황을 설정하였고, Prototype
#  Pattern이 적절한가에 대해 
# 남에게 설명한다는 생각으로 정리하시오.


# 프로토타입의 객체를 계속 복사해와서 커스텀해야 하는 상황을 생각하다가
# 음료를 주문하고 추가 요구 사항을 입력해야 하는 상황을 떠올렸습니다.
# 이 프로그램은 고객이 음료를 주문하고 추가 요구 사항을 입력할 때마다 영수증을 출력한 후
# 그 객체를 order_list 라는 리스트에 차례대로 저장해 두었다가 주문을 끝냈을 때 
# 주문 수량과 함께 총 금액을 출력해주는 프로그램입니다.

# 음료 종류는 한정되어 있으므로 주문받을 때마다 미리 만들어둔 그에 해당하는 음료 객체를 복사해온 다음,
# detail에 추가 사항을 저장해 커스텀하면 되므로, Prototype Pattern은 적절합니다.


from abc import *
import copy

class Drink(metaclass = ABCMeta):
    @abstractmethod
    def receipt(self):
        pass

    @abstractmethod
    def setDetail(self):
        pass
    
    @abstractmethod
    def clone(self):
        pass

class Americano(Drink):
    menu = ""
    detail = "No detail"
    price = 4000

    def __init__(self, iced:str):
        self.menu = iced + " Americano"
        if iced == "Ice":
            self.price += 500

    def setDetail(self, detail:str="No detail"):
        self.detail = detail


    def receipt(self, number:int):
        print("--------------------------------")
        print("Menu     :", self.menu)
        print("Price    :", self.price)
        print("Detail   :", self.detail)
        print("Number   :", number)
        print("--------------------------------")

    def clone(self):
        return copy.deepcopy(self)


class MilkTea(Drink):
    detail = "No detail"
    price = 5000
    menu = ""

    def __init__(self, tea_type:str):
        self.menu = tea_type + " Milk Tea"

    def setDetail(self, detail:str):
        self.detail = detail

    def receipt(self, number:int):
        print("--------------------------------")
        print("Menu     :", self.menu)
        print("Price    :", self.price)
        print("Detail   :", self.detail)
        print("Number   :", number)
        print("--------------------------------")

    def clone(self):
        return copy.deepcopy(self)

class Manager:
    def __init__(self):
        self.showcase = {"a":1}

    def register(self, name:str, proto:Drink):
        self.showcase[name] = proto

    def create(self, protoName):
        p = self.showcase[protoName]
        return p.clone()



manager = Manager()
iceAmericano = Americano("Ice")
hotAmericano = Americano("Hot")

EarlGreyMilkTea = MilkTea("Earl Grey")
DarjeelingMilkTea = MilkTea("Darjeeling")

manager.register("IA", iceAmericano)
manager.register("HA", hotAmericano)
manager.register("EGMT", EarlGreyMilkTea)
manager.register("DMT", DarjeelingMilkTea)

order_num = 0
order_list = [0 for _ in range(100)]


while True:
    if order_num >= 100:
        break
    if input("Stop? (y/n) ") == 'y':
        break
    drink = input("Which Drink? (Americano / Milk Tea) ")
    if drink == "Americano":
        if input("Iced(+500)? (y/n) ") == 'n':
            # 핫 아메리카노
            order_list[order_num] = manager.create("HA")
        else:
            order_list[order_num] = manager.create("IA")
            # 아이스 아메리카노

    else:
        tea_type = input("tea type? (Earl Grey / Darjeeling) ")
        if tea_type == "Darjeeling":
            # 다즐링 밀크티
            order_list[order_num] = manager.create("DMT")
        else:
            # 얼그레이 밀크티
            order_list[order_num] = manager.create("EGMT")

    if input("detail order? (y/n) ") == 'y':
        detail_order = input("> ")
        order_list[order_num].setDetail(detail_order)
    
    
    order_list[order_num].receipt(order_num + 1)
    order_num += 1

sale_sum = 0
ia_cnt = 0
ha_cnt = 0
em_cnt = 0
dm_cnt = 0

for i in range(100):
    if order_list[i] == 0: break
    
    if order_list[i].menu == "Ice Americano": ia_cnt += 1
    elif order_list[i].menu == "Hot Americano": ha_cnt += 1
    elif order_list[i].menu == "Earl Grey Milk Tea": em_cnt += 1
    elif order_list[i].menu == "Darjeeling Milk Tea": dm_cnt += 1

    sale_sum += order_list[i].price

print()
print("================================")
print("메뉴                 판매 수량")
print("Ice Americano        ",  ia_cnt)
print("Hot Americano        ",  ha_cnt)
print("Earl Grey Milk Tea   ",  em_cnt)
print("Darjeeling Milk Tea  ",  dm_cnt)
print("================================")
print("오늘 판매 총액은     ", sale_sum)
print("================================")
