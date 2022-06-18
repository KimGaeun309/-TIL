
class Client:
    def __init__(self, name, ID, pw, sex, age, point):
        self.goods = Goods.getInstance()
        self.basket = {}
        self.name = name
        self.ID = ID
        self.pw = pw
        self.sex = sex
        self.age = age
        self.point = point
    def printClient(self):
        print("<< Print Client Information >>")
        print(f"name    : {self.name}")
        print(f"ID      : {self.ID}")
        print(f"sex     : {self.sex}")
        print(f"age     : {self.age}")
        print(f"point   : {self.point}")
    def addToBasket(self, goods_name, count=1):
        if goods_name in self.basket:
            self.basket[goods_name] += count
        else:
            self.basket[goods_name] = count
    def delFromBasket(self, goods_name, count=-1):
        if count == -1: 
            if goods_name in self.basket:
                del self.basket[goods_name]
        else: 
            if goods_name in self.basket:
                self.basket[goods_name] -= count
                if self.basket[goods_name] <= 0:
                    del self.basket[goods_name]
    def printBasket(self): 
        for k in self.basket.keys():
            self.goods.printData(k)
            print(f"(count   : {self.basket[k]})")
            print()
    def tryBuy(self): 
        price = 0
        for k in self.basket.keys():
            price += (self.goods.data[k][0] * self.basket[k])
        return self.point - price  
    def buyBasket(self): 
        left_point = self.tryBuy()
        if left_point < 0:
            print(f"You need more points. {-left_point}")
            return left_point
        self.point = left_point
        for k in self.basket.keys():
            self.goods.data[k][1] += 1 
            if self.sex == 'female':
                self.goods.data[k][2] += 1 
            else:
                self.goods.data[k][3] += 1 
            self.goods.data[k][4] = self.goods.data[k][4] * ( (self.goods.data[k][1] - 1) / self.goods.data[k][1]) + self.age * (1 / self.goods.data[k][1]) 
        self.basket = {}
    def buyPoint(self, method, amount):
        payment = {"method" : method, "amount" : amount}
        if (cash_handler.handle(payment) == False):
            print("Failed Charging Points")
        else:
            self.point += amount

class ClientBuilder:
    def __init__(self):
        self.name = None
        self.ID = None
        self.pw = None
        self.sex = None
        self.age = None
        self.point = None
    def setName(self, name):
        self.name = name
        return self
    def setId(self, ID):
        self.ID = ID
        return self
    def setPw(self, pw):
        self.pw = pw
        return self
    def setSex(self, sex):
        self.sex = sex
        return self
    def setAge(self, age):
        self.age = age
        return self
    def setPoint(self, point):
        self.point = point
        return self
    def build(self):
        client = Client(self.name, self.ID, self.pw, self.sex, self.age, self.point)
        return client
    
class Goods:
    _instance = None
    def __init__(self):
        self.data = {} 
    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = Goods()
        return cls._instance 
        
    def printData(self, goods_name):
        print(f"name                        : {goods_name}")
        print(f"price                       : {self.data[goods_name][0]}")
        print(f"# people purchased          : {self.data[goods_name][1]}")
        if self.data[goods_name][1] == 0:
            female = 0
            male = 0
        else:
            female = self.data[goods_name][2] / self.data[goods_name][1]
            male = self.data[goods_name][3] / self.data[goods_name][1]
        if female > male:
            print(f"high preference for women   : {female*100:.1f} %")
        elif male > female:
            print(f"high preference for men     : {male*100:.1f} %")
        else:
            print("equal preference between men and women")
        print(f"average age                 : {self.data[goods_name][4]:.1f}")
        print()
    def printEveryData(self):
        print("<< Print Goods Information >>")
        for k in self.data.keys():
            self.printData(k)



class Handler:
    def __init__(self):
        self.next_handler = None
    def setNext(self, handler):
        self.next_handler = handler
    def handle(self, req):
        if self.next_handler:
            return self.next_handler.handle(req)
        print("All handlers failed")
        return False

class CashHandler(Handler):
    def handle(self, req):
        if req['method'] == 'cash':
            print(f"processing cash {req['amount']} won")
        else:
            super().handle(req)

class CreditHandler(Handler):
    def handle(self, req):
        if req['method'] == 'creditCard':
            print(f"processing creditCard {req['amount']} won")
        else:
            super().handle(req)

class DebitCardHandler(Handler):
    def handle(self, req):
        if req['method'] == 'debitCard':
            print(f"processing debitCard {req['amount']} won")
        else:
            super().handle(req)

class Setting:
    global cash_handler
    global credit_handler
    global debit_handler
    global clients
    cash_handler = CashHandler()
    credit_handler = CreditHandler()
    debit_handler = DebitCardHandler()
    clients = []
    def __init__(self):
        self.goods = Goods.getInstance()
        self.cash_handler = cash_handler
        self.credit_handler = credit_handler
        self.debit_handler = debit_handler
        self.client_builder = ClientBuilder()
    def preset(self):
        self.cash_handler.setNext(self.credit_handler)
        self.credit_handler.setNext(self.debit_handler)
        
        self.goods.data['mugcup'] = [3000, 0, 0, 0, 0]
        self.goods.data['diary'] = [4000, 0, 0, 0, 0]
        self.goods.data['note'] = [2000, 0, 0, 0, 0]
        self.goods.data['pencil'] = [500, 0, 0, 0, 0]
        self.goods.data['letter'] = [500, 0, 0, 0, 0]
        self.goods.data['file'] = [700, 0, 0, 0, 0]
        self.goods.data['pencil case'] = [3500, 0, 0, 0, 0]
        self.goods.data['memo'] = [1000, 0, 0, 0, 0]
        self.goods.data['sharp pencil'] = [1500, 0, 0, 0, 0]
        self.goods.data['eraser'] = [600, 0, 0, 0, 0]
        self.goods.data['alblum'] = [6000, 0, 0, 0, 0]

        clients.append(self.client_builder.setName('Minjoon').setId('minjoon20').setPw('1111').setSex('male').setAge(20).setPoint(5000).build())
        clients.append(self.client_builder.setName('Seoyeon').setId('seoyeon20').setPw('2222').setSex('female').setAge(20).setPoint(5000).build())
        clients.append(self.client_builder.setName('Seojoon').setId('seojoon10').setPw('3333').setSex('male').setAge(10).setPoint(5000).build())
        clients.append(self.client_builder.setName('Haeun').setId('haeun10').setPw('4444').setSex('female').setAge(10).setPoint(5000).build())
        clients.append(self.client_builder.setName('Cherlsoo').setId('cherlsoo40').setPw('5555').setSex('male').setAge(40).setPoint(5000).build())
        clients.append(self.client_builder.setName('Younghee').setId('younghee40').setPw('6666').setSex('female').setAge(40).setPoint(5000).build())


setting = Setting()
setting.preset()


flag = True

while flag:
    print("ID: ", end='')
    my_id = input()
    idx = -1
    for i in range(len(clients)):
        if clients[i].ID == my_id: idx = i; break;
    if idx == -1: print("Wrong ID"); continue;
    print("PW: ", end='')
    my_pw = input()
    if clients[idx].pw != my_pw: print("Wrong PW"); continue;
    print("logged in")
    print()
    print("<< Instructions >>")
    print("myinfo : print my information")
    print("goods : print Goods information")
    print("basket : print Basket")
    print("add : add to Basket")
    print("delete : delete from Basket")
    print("purchase : purchase everything from Basket")
    print("charge : charge up points")
    print("logout : logout")
    print("quit : quit")
    print()

    while True:
        print("-------------------------")
        print("Instruction: ", end='')
        instruction = input()
        if instruction == "myinfo":
            clients[idx].printClient()
        elif instruction == "goods":
            clients[idx].goods.printEveryData()
        elif instruction == "basket":
            clients[idx].printBasket()
        elif instruction == "add":
            print("which? ", end='')
            good = input()
            if good not in clients[idx].goods.data:
                print("Wrong Name")
                continue
            print("how much? ", end='')
            count = int(input())
            clients[idx].addToBasket(good, count)
        elif instruction == "delete":
            print("which? ", end='')
            good = input()
            if good not in clients[idx].goods.data:
                print("Wrong Name")
                continue
            print("all? (y/n) ", end='')
            if input() == 'y':
                clients[idx].delFromBasket(good)
            else:
                print("how much? ", end='')
                count = int(input())
                clients[idx].delFromBasket(good, count)
        elif instruction == "purchase":
            clients[idx].buyBasket()
        elif instruction == "charge":
            print("method (cash, creditCard, debitCard): ", end='')
            method = input()
            if method != 'cash' and method != 'creditCard' and method != 'debitCard':
                print("Wrong Name")
                continue
            print("amount: ", end='')
            amount = int(input())
            clients[idx].buyPoint(method, amount)
        elif instruction == "logout":
            break
        elif instruction == "quit":
            flag = False
            break
        else:
            print("Wrong Instruction")
        
